"""
sql_analytics_patterns - Reusable, tested SQL templates for analytic windowing, cohorting, and KPI reporting.
"""

__version__ = "0.1.0"

from .dialectaware_sql_template_rend import SqlAnalyticsPatterns
from .types import SqlAnalyticsPatternsOptions, SqlAnalyticsPatternsResult
from .exceptions import SqlAnalyticsPatternsError, ConfigurationError, ValidationError

__all__ = [
    "SqlAnalyticsPatterns",
    "SqlAnalyticsPatternsOptions",
    "SqlAnalyticsPatternsResult",
    "SqlAnalyticsPatternsError",
    "ConfigurationError",
    "ValidationError",
]
