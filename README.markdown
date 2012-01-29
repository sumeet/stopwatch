# stopwatch

A neat stopwatch for Python.

## As a regular object:

```python
    >>> stopwatch = Stopwatch()
    >>> stopwatch.start()
    >>> time.sleep(1)
    >>> stopwatch.time_elapsed
    1.1520211696624756
    >>> time.sleep(1)
    >>> stopwatch.stop()
    >>> stopwatch.total_run_time
    2.055678129196167
```

## As a context manager:

```python
    >>> with Stopwatch() as stopwatch:
    ...     time.sleep(1)
    ...     print stopwatch.time_elapsed
    ...     time.sleep(1)
    1.1520211696624756
    >>> stopwatch.total_run_time
    2.055678129196167
```
