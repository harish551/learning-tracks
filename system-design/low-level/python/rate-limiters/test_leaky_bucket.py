import unittest
import threading
import time

class TestLeakyBucket(unittest.TestCase):

    def setUp(self):
        from leaky_bucket import LeakyBucket
        self.rate_limiter = LeakyBucket(5, 1)

    def test_initial_burst(self):
        """All initial requests should be allowed"""
        for _ in range(5):
            self.assertTrue(self.rate_limiter.allow_request())

    def test_reject_when_full(self):
        for _ in range(6):
            self.rate_limiter.allow_request()
        self.assertFalse(self.rate_limiter.allow_request())

    def test_leak_over_time(self):
        for _ in range(5):
            self.rate_limiter.allow_request()

        time.sleep(2)
        self.assertTrue(self.rate_limiter.allow_request())

    def test_smooth_rate(self):
        """Should not allow burst like token bucket"""
        for _ in range(5):
            self.rate_limiter.allow_request()

        time.sleep(1)

        # Only ~1 request should be allowed
        results = [self.rate_limiter.allow_request() for _ in range(3)]
        self.assertTrue(sum(results) <= 2)

    def test_no_overflow(self):
        """Water should not exceed capacity"""
        for _ in range(8):
            self.rate_limiter.allow_request()

        self.assertTrue(self.rate_limiter.requests <= self.rate_limiter.capacity)

    def test_idle_reset(self):
        """Bucket empties when idle"""
        for _ in range(5):
            self.rate_limiter.allow_request()

        time.sleep(1)
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