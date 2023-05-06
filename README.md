# Demo for missing log format validation

Flask provide a `current_app.logger` for emitting log events rather than directly using `logging.getLogger()` to get a handle.

`current_app.logger` doesn't appear to be detected by ruff's G (flake8-logging-format) linter.
