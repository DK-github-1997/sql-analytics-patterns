#!/usr/bin/env python3
"""Basic usage example for sql_analytics_patterns."""

from sql_analytics_patterns import SqlAnalyticsPatterns, SqlAnalyticsPatternsOptions


def main() -> None:
    # Create with default options
    instance = SqlAnalyticsPatterns()
    result = instance.run()
    print(f"Default run: success={result.success}, data={result.data}")

    # Create with custom options
    options = SqlAnalyticsPatternsOptions(verbose=True)
    instance = SqlAnalyticsPatterns(options)
    result = instance.run()
    print(f"Verbose run: success={result.success}, data={result.data}")


if __name__ == "__main__":
    main()
