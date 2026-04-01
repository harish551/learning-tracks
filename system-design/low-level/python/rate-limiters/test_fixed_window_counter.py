import unittest
import threading
import time

class TestFixedWindow(unittest.TestCase):

    def setUp(self):
        from fixed_window_counter import FixedWindow
        self.rate_limiter = FixedWindow(5, 1)

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