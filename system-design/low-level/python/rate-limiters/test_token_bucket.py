import unittest
import time
import threading

class TestTokenBucket(unittest.TestCase):

    def setUp(self):
        from token_bucket import TokenBucket 
        self.bucket = TokenBucket(capacity=5, refill_rate=1)

    def test_initial_burst(self):
        """All initial tokens should be allowed"""
        for _ in range(5):
            self.assertTrue(self.bucket.allow_request())

    def test_exceed_capacity(self):
        """Should reject after capacity is exhausted"""
        for _ in range(5):
            self.bucket.allow_request()
        self.assertFalse(self.bucket.allow_request())

    def test_refill(self):
        """Tokens should refill over time"""
        for _ in range(5):
            self.bucket.allow_request()

        time.sleep(2)
        self.assertTrue(self.bucket.allow_request())
        self.assertTrue(self.bucket.allow_request())

    def test_no_overflow(self):
        """Tokens should not exceed capacity"""
        time.sleep(10)
        self.assertTrue(self.bucket.tokens <= self.bucket.capacity)

    def test_zero_refill_rate(self):
        """No refill should happen"""
        from token_bucket import TokenBucket
        bucket = TokenBucket(3, 0)

        for _ in range(3):
            self.assertTrue(bucket.allow_request())
        self.assertFalse(bucket.allow_request())

    def test_time_skew(self):
        """Simulate large time jump"""
        self.bucket.last_refill -= 1000
        self.assertTrue(self.bucket.allow_request())
        self.assertTrue(self.bucket.tokens <= self.bucket.capacity)

    def test_concurrent_requests(self):
        """Ensure thread safety"""
        results = []

        def worker():
            results.append(self.bucket.allow_request())

        threads = [threading.Thread(target=worker) for _ in range(20)]
        for t in threads: t.start()
        for t in threads: t.join()

        # At most capacity should be allowed
        self.assertTrue(sum(results) <= 5)

    def test_high_frequency_calls(self):
        """Floating point drift check"""
        results = [self.bucket.allow_request() for _ in range(20)]
        self.assertTrue(sum(results) <= 5)