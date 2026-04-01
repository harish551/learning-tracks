import time
from threading import Lock

class TokenBucket:

    def __init__(self, capacity, refill_rate):
        self.capacity = capacity # max tokens
        self.tokens = capacity # initial fill
        self.refill_rate = refill_rate  # tokens per sec
        self.last_refill = time.time() # track lastfill on every re-fill
        self.lock = Lock()


    def allow_request(self):
        with self.lock:
            now = time.time()
            elapsed = now - self.last_refill

            # refill tokens as per refill rate
            refill = elapsed * self.refill_rate
            self.tokens = min(self.capacity, self.tokens + refill)
            self.last_refill = now

            if self.tokens >= 1:
                self.tokens -= 1
                return True
            return False

