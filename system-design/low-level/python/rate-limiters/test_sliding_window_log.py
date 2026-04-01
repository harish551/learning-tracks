import unittest
import threading
import time

class TestSlidingWindowCounter(unittest.TestCase):

    def setUp(self):
        from sliding_window_log import SlidingWindowLog
        self.rate_limiter = SlidingWindowLog(5, 1)

    def test_initial_burst(self):
        """All initial tokens should be allowed"""
        for _ in range(5):
            self.assertTrue(self.rate_limiter.allow_request())

    def test_exceed_capacity(self):
        """Should reject after capacity is exhausted"""
        for _ in range(5):
            self.rate_limiter.allow_request()
        self.assertFalse(self.rate_limiter.allow_request())

    def test_new_window(self):
        """Request should be allowed after current window"""
        for _ in range(5):
            self.rate_limiter.allow_request()

        time.sleep(2)
        self.assertTrue(self.rate_limiter.allow_request())
        self.assertTrue(self.rate_limiter.allow_request())

    def test_concurrent_requests(self):
        """Ensure thread safety"""
        results = []

        def worker():
            results.append(self.rate_limiter.allow_request())

        threads = [threading.Thread(target=worker) for _ in range(20)]
        for t in threads: t.start()
        for t in threads: t.join()

        # At most capacity should be allowed
        self.assertTrue(sum(results) <= 5)
    def test_reject_when_full(self):
        for _ in range(5):
            self.rate_limiter.allow_request()
        self.assertFalse(self.rate_limiter.allow_request())

    def test_window_expiry(self):
        for _ in range(5):
            self.rate_limiter.allow_request()

        time.sleep(2)
        self.assertTrue(self.rate_limiter.allow_request())

    def test_boundary_condition(self):
        """Classic bug case"""
        self.rate_limiter.allow_request()
        time.sleep(2)

        # Should be allowed if <= is correct
        self.assertTrue(self.rate_limiter.allow_request())

    def test_memory_cleanup(self):
        for _ in range(100):
            self.rate_limiter.allow_request()

        time.sleep(2)
        self.rate_limiter.allow_request()

        self.assertTrue(len(self.rate_limiter.requests) <= self.rate_limiter.capacity)

    def test_high_throughput(self):
        results = [self.rate_limiter.allow_request() for _ in range(50)]
        self.assertTrue(sum(results) <= 5)