import time
import unittest

import stopwatch


class MockSystemClock(object):
    """Represents a system clock with time starting at `0` and incremented
    whenever `sleep()` is called.

    Meant to replace the `time()` and `sleep()` functions in the `time` module.

    >>> clock = MockSystemClock()
    >>> clock.time()
    0
    >>> clock.sleep(1)
    >>> clock.time()
    1
    """

    def __init__(self):
        """Initialize the current system time to `0`."""
        self._system_time = 0

    def time(self):
        """Return the current system time."""
        return self._system_time

    def sleep(self, seconds):
        """Increment the system time by `seconds`."""
        self._system_time += seconds


class StopwatchTestCase(unittest.TestCase):

    def setUp(self):
        """Monkey patch `time.time()` and `time.sleep()` to point to the
        corresponding methods on a new `MockSystemClock` instance.
        """
        self._time_time = time.time
        self._time_sleep = time.sleep

        mock_system_clock = MockSystemClock()
        time.time = mock_system_clock.time
        time.sleep = mock_system_clock.sleep

    def tearDown(self):
        """Restore the `time` module."""
        time.time = self._time_time
        time.sleep = self._time_sleep

    def test_stopwatch_as_object(self):
        """Test using a `Stopwatch` as a regular object."""
        sw = stopwatch.Stopwatch()
        sw.start()
        self.assertEqual(0, sw.time_elapsed)
        time.sleep(1)
        self.assertEqual(1, sw.time_elapsed)
        sw.stop()
        self.assertEqual(1, sw.total_run_time)

    def test_stopwatch_as_context_manager(self):
        """Test using a `Stopwatch` as a context manager."""
        with stopwatch.Stopwatch() as sw:
            sw.start()
            self.assertEqual(0, sw.time_elapsed)
            time.sleep(1)
            self.assertEqual(1, sw.time_elapsed)

        self.assertEqual(1, sw.total_run_time)


if __name__ == '__main__':
    unittest.main()
