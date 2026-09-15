"""Deterministic, standard-library-only test doubles for kernel tests."""

from collections.abc import Iterable
from datetime import datetime, timedelta
from uuid import UUID


class DeterministicUUIDSource:
    """Return a caller-supplied sequence of UUIDs in order."""

    def __init__(self, values: Iterable[UUID]) -> None:
        self._values = iter(values)

    def __call__(self) -> UUID:
        try:
            value = next(self._values)
        except StopIteration as error:
            raise RuntimeError("deterministic UUID sequence exhausted") from error
        if not isinstance(value, UUID):
            raise TypeError("deterministic UUID values must be uuid.UUID instances")
        return value


class DeterministicClock:
    """Hold an explicitly controlled, timezone-aware instant."""

    def __init__(self, initial: datetime) -> None:
        self._current = self._require_aware(initial)

    @property
    def current(self) -> datetime:
        return self._current

    def set(self, instant: datetime) -> None:
        self._current = self._require_aware(instant)

    def advance(self, delta: timedelta) -> None:
        if not isinstance(delta, timedelta):
            raise TypeError("clock delta must be a datetime.timedelta")
        if delta < timedelta(0):
            raise ValueError("clock delta must not be negative")
        self._current += delta

    @staticmethod
    def _require_aware(instant: datetime) -> datetime:
        if not isinstance(instant, datetime):
            raise TypeError("clock instant must be a datetime.datetime")
        if instant.tzinfo is None or instant.utcoffset() is None:
            raise ValueError("clock instant must be timezone-aware")
        return instant


class DeterministicRecoveryEpoch:
    """Hold a test-only integer representation of a monotonic recovery epoch."""

    def __init__(self, initial: int) -> None:
        self._current = self._require_epoch(initial)

    @property
    def current(self) -> int:
        return self._current

    def advance(self, amount: int = 1) -> int:
        if isinstance(amount, bool) or not isinstance(amount, int):
            raise TypeError("recovery epoch advancement must be an integer")
        if amount <= 0:
            raise ValueError("recovery epoch advancement must be positive")
        self._current += amount
        return self._current

    @staticmethod
    def _require_epoch(value: int) -> int:
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError("recovery epoch must be an integer")
        if value < 0:
            raise ValueError("recovery epoch must not be negative")
        return value
