"""Type definitions for sql_analytics_patterns."""

from dataclasses import dataclass, field
from typing import Any, Optional


@dataclass
class SqlAnalyticsPatternsOptions:
    """Configuration options for SqlAnalyticsPatterns.

    Attributes:
        verbose: Enable verbose logging for debugging.
        feature_1: Configuration for: Dialect-aware SQL template rendering (Oracle vs Redshift differences)
        feature_2: Configuration for: Reference datasets + golden-query tests to prevent KPI regressions
        feature_3: Configuration for: Packaged patterns: RFM, basket analysis, cohorts, retention, rolling-window KPIs
    """

    verbose: bool = False
    feature_1: Optional[dict[str, Any]] = None
    feature_2: Optional[dict[str, Any]] = None
    feature_3: Optional[dict[str, Any]] = None


@dataclass
class SqlAnalyticsPatternsResult:
    """Result returned by SqlAnalyticsPatterns operations.

    Attributes:
        success: Whether the operation succeeded.
        data: The result data, if successful.
        error: Error message, if the operation failed.
    """

    success: bool
    data: Any = field(default=None)
    error: Optional[str] = None
