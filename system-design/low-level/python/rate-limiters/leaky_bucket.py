import time
from threading import Lock

class LeakyBucket:

    def __init__(self, capacity, leak_rate):
        self.capacity = capacity
        self.leak_rate = leak_rate
        self.requests = 0
        self.last_check = time.time()
        self.lock = Lock()
    
    def allow_request(self):
        with self.lock:
            now = time.time()

            # leak requests
            elapsed = now - self.last_check
            leaked = elapsed * self.leak_rate
            self.requests = max(0.0, self.requests - leaked)

            self.last_check = now
            # check overflow
            if self.requests + 1 > self.capacity:
                return False # discard request
            
            self.requests += 1
            self.requests = min(self.capacity, self.requests)

            return True

