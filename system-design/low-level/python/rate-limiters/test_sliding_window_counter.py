import unittest
import time

class TestSlidingWindowCounter(unittest.TestCase):

    def setUp(self):
        from sliding_window_counter import SlidingWindowCounter
        self.rate_limiter = SlidingWindowCounter(capacity=5, window_size=2)

    def test_within_limit(self):
        self.assertTrue(self.rate_limiter.allow_request())
        self.assertTrue(self.rate_limiter.allow_request())
        self.assertTrue(self.rate_limiter.allow_request())

    def test_exceed_limit(self):
        for _ in range(5):
            self.rate_limiter.allow_request()
        self.assertFalse(self.rate_limiter.allow_request())

    def test_smooth_transition(self):
        """Should not allow full burst like fixed window"""
        for _ in range(5):
            self.rate_limiter.allow_request()

        time.sleep(1)

        # Should allow only limited requests, not full reset
        allowed = [self.rate_limiter.allow_request() for _ in range(5)]
        self.assertTrue(sum(allowed) < 3)

    def test_window_shift(self):
        for _ in range(5):
            self.rate_limiter.allow_request()

        time.sleep(3)
        self.assertTrue(self.rate_limiter.allow_request())

    def test_large_time_gap(self):
        """Previous window should reset"""
        time.sleep(5)
        self.assertTrue(self.rate_limiter.allow_request())
        self.assertTrue(self.rate_limiter.previous_count == 0)

    def test_no_overflow(self):
        """Ensure effective count never exceeds capacity"""
        for _ in range(10):
            self.rate_limiter.allow_request()

        self.assertTrue(self.rate_limiter.current_count <= self.rate_limiter.capacity)