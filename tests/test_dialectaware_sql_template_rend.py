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

    def test_render_sql_template_oracle_basic(self) -> None:
        instance = SqlAnalyticsPatterns()
        sql = instance.render_sql_template(
            "SELECT CURRENT_TIMESTAMP FROM dual WHERE id = {user_id}",
            dialect="oracle",
            params={"user_id": "42"},
        )
        assert "SYSDATE" in sql
        assert "42" in sql

    def test_render_sql_template_redshift_basic(self) -> None:
        instance = SqlAnalyticsPatterns()
        sql = instance.render_sql_template(
            "SELECT CURRENT_TIMESTAMP FROM my_table WHERE id = {user_id}",
            dialect="redshift",
            params={"user_id": "99"},
        )
        assert "GETDATE()" in sql
        assert "99" in sql

    def test_render_sql_template_missing_param(self) -> None:
        instance = SqlAnalyticsPatterns()
        try:
            instance.render_sql_template(
                "SELECT * FROM t WHERE id = {user_id}",
                dialect="oracle",
                params={},
            )
        except Exception as e:
            assert e.__class__.__name__ == "ValidationError"
            assert "MISSING_PARAM" in str(e) or getattr(e, "code", None) == "MISSING_PARAM"
        else:
            assert False, "Expected ValidationError for missing param"

    def test_render_sql_template_unsupported_dialect(self) -> None:
        instance = SqlAnalyticsPatterns()
        try:
            instance.render_sql_template(
                "SELECT 1",
                dialect="mysql",
            )
        except Exception as e:
            assert e.__class__.__name__ == "ConfigurationError"
            assert "UNSUPPORTED_DIALECT" in str(e) or getattr(e, "code", None) == "UNSUPPORTED_DIALECT"
        else:
            assert False, "Expected ConfigurationError for unsupported dialect"

    def test_render_sql_template_empty_template(self) -> None:
        instance = SqlAnalyticsPatterns()
        try:
            instance.render_sql_template(
                "   ",
                dialect="oracle",
            )
        except Exception as e:
            assert e.__class__.__name__ == "ValidationError"
            assert "EMPTY_FIELD" in str(e) or getattr(e, "code", None) == "EMPTY_FIELD"
        else:
            assert False, "Expected ValidationError for empty template"

    def test_render_sql_template_empty_dialect(self) -> None:
        instance = SqlAnalyticsPatterns()
        try:
            instance.render_sql_template(
                "SELECT 1",
                dialect="   ",
            )
        except Exception as e:
            assert e.__class__.__name__ == "ValidationError"
            assert "EMPTY_FIELD" in str(e) or getattr(e, "code", None) == "EMPTY_FIELD"
        else:
            assert False, "Expected ValidationError for empty dialect"
