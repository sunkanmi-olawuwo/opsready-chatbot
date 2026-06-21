from collections.abc import Iterator
from contextlib import contextmanager
from time import perf_counter


@contextmanager
def local_span(name: str) -> Iterator[dict[str, object]]:
    started = perf_counter()
    span: dict[str, object] = {"name": name, "duration_ms": 0}
    try:
        yield span
    finally:
        span["duration_ms"] = int((perf_counter() - started) * 1000)
