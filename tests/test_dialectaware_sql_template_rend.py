"""Tests for sql_analytics_patterns."""

from sql_analytics_patterns import SqlAnalyticsPatterns, SqlAnalyticsPatternsOptions


class TestSqlAnalyticsPatterns:
    def test_create_instance_with_defaults(self) -> None:
        instance = SqlAnalyticsPatterns()
        assert instance is not None

    def test_create_instance_with_options(self) -> None:
        options = SqlAnalyticsPatternsOptions(verbose=True)
        instance = SqlAnalyticsPatterns(options)
        assert instance.options.verbose is True

    def test_run_successfully(self) -> None:
        instance = SqlAnalyticsPatterns()
        result = instance.run()
        assert result.success is True
        assert result.data is not None

    def test_run_returns_result_type(self) -> None:
        instance = SqlAnalyticsPatterns()
        result = instance.run()
        assert result.error is None
