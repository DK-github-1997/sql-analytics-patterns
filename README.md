# sql_analytics_patterns

Reusable, tested SQL templates for analytic windowing, cohorting, and KPI reporting....

## Installation

```bash
pip install sql_analytics_patterns
```

## Quick Start

```python
from sql_analytics_patterns import SqlAnalyticsPatterns

instance = SqlAnalyticsPatterns()
result = instance.run()
print(result)
```

## Features

- Dialect-aware SQL template rendering (Oracle vs Redshift differences)
- Reference datasets + golden-query tests to prevent KPI regressions
- Packaged patterns: RFM, basket analysis, cohorts, retention, rolling-window KPIs

## API Reference

### `SqlAnalyticsPatterns`

#### Constructor

```python
SqlAnalyticsPatterns(options: SqlAnalyticsPatternsOptions | None = None)
```

#### Methods

- `run()` - Execute the main operation. Returns `SqlAnalyticsPatternsResult`.

## Development

```bash
# Install with dev dependencies
make install

# Run tests
make test

# Lint and type-check
make lint

# Format code
make format

# Build
make build
```

## Publishing

1. Update version in `pyproject.toml` and `src/sql_analytics_patterns/__init__.py`
2. Create a GitHub release with tag `v0.x.0`
3. The GitHub Action will automatically publish to PyPI

## License

MIT
