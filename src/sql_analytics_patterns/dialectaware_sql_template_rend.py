"""Core module for sql_analytics_patterns."""

from .types import SqlAnalyticsPatternsOptions, SqlAnalyticsPatternsResult


class SqlAnalyticsPatterns:
    """Reusable, tested SQL templates for analytic windowing, cohorting, and KPI reporting.

    Example::

        from sql_analytics_patterns import SqlAnalyticsPatterns

        instance = SqlAnalyticsPatterns()
        result = instance.run()
        print(result)
    """

    def __init__(self, options: SqlAnalyticsPatternsOptions | None = None) -> None:
        self.options = options or SqlAnalyticsPatternsOptions()

    def run(self) -> SqlAnalyticsPatternsResult:
        """Execute the main operation (placeholder).

        Returns:
            SqlAnalyticsPatternsResult with the operation outcome.
        """
        return SqlAnalyticsPatternsResult(
            success=True,
            data={"message": "SqlAnalyticsPatterns is working!"},
        )

    def render_sql_template(
        self,
        template: str,
        dialect: str,
        params: dict[str, str] | None = None,
    ) -> str:
        """
        Render a SQL template with dialect-specific adjustments (Oracle or Redshift).

        Args:
            template: The SQL template string, with placeholders in {param} format.
            dialect: Target SQL dialect ('oracle' or 'redshift').
            params: Optional dict of parameters to substitute into the template.

        Returns:
            Rendered SQL string for the specified dialect.

        Raises:
            ValidationError: If template or dialect is invalid.
            ConfigurationError: If dialect is unsupported.

        Example::

            sql = instance.render_sql_template(
                "SELECT * FROM my_table WHERE id = {user_id}",
                dialect="oracle",
                params={"user_id": "42"}
            )
        """
        from ._utils import validate_not_empty
        from .exceptions import ValidationError, ConfigurationError

        template = validate_not_empty(template, "template")
        dialect = validate_not_empty(dialect, "dialect").lower()
        if dialect not in ("oracle", "redshift"):
            raise ConfigurationError(f"Unsupported SQL dialect: {dialect}", code="UNSUPPORTED_DIALECT")

        # Substitute parameters
        sql = template
        if params:
            try:
                sql = sql.format(**params)
            except KeyError as e:
                raise ValidationError(f"Missing template parameter: {e.args[0]}", code="MISSING_PARAM")

        # Dialect-specific adjustments
        if dialect == "oracle":
            sql = self._apply_oracle_adjustments(sql)
        elif dialect == "redshift":
            sql = self._apply_redshift_adjustments(sql)
        return sql

    def _apply_oracle_adjustments(self, sql: str) -> str:
        """
        Internal: Apply Oracle-specific SQL adjustments.
        """
        # Example: Oracle uses double quotes for identifiers, SYSDATE for current timestamp
        sql = sql.replace("CURRENT_TIMESTAMP", "SYSDATE")
        return sql

    def _apply_redshift_adjustments(self, sql: str) -> str:
        """
        Internal: Apply Redshift-specific SQL adjustments.
        """
        # Example: Redshift uses GETDATE() for current timestamp
        sql = sql.replace("CURRENT_TIMESTAMP", "GETDATE()")
        return sql
