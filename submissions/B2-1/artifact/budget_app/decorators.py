from __future__ import annotations

import logging
from functools import wraps
from time import perf_counter
from typing import Any, Callable, TypeVar

F = TypeVar("F", bound=Callable[..., Any])


def logged_and_timed(function: F) -> F:
    """Log operation outcomes and elapsed time without mixing logs into CLI output."""

    @wraps(function)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        started = perf_counter()
        try:
            result = function(*args, **kwargs)
        except Exception:
            logging.getLogger("budget_app").exception("%s failed", function.__name__)
            raise
        logging.getLogger("budget_app").info("%s completed in %.4fs", function.__name__, perf_counter() - started)
        return result

    return wrapper  # type: ignore[return-value]
