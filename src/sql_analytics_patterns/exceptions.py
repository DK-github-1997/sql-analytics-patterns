"""Custom exceptions for sql_analytics_patterns."""

from __future__ import annotations


class SqlAnalyticsPatternsError(Exception):
    """Base exception for all SqlAnalyticsPatterns errors.

    Attributes:
        message: Human-readable error description.
        code: Optional machine-readable error code.
    """

    def __init__(self, message: str, code: str | None = None) -> None:
        super().__init__(message)
        self.code = code


class ConfigurationError(SqlAnalyticsPatternsError):
    """Raised when the SDK is misconfigured."""


class ValidationError(SqlAnalyticsPatternsError):
    """Raised when input validation fails."""


class TimeoutError(SqlAnalyticsPatternsError):
    """Raised when an operation exceeds its time limit."""
