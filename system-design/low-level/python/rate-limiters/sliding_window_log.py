import time
from threading import Lock
from collections import deque

class SlidingWindowLog:

    def __init__(self, capacity, window_size):
        self.capacity = capacity # max requests per window
        self.window_size = window_size  # window size in seconds
        self.requests = deque() # track requests and it's timestamps
        self.lock = Lock()
    
    def allow_request(self):
        with self.lock:
            now = time.time()

            # remove expired requests from queue
            while len(self.requests) and self.requests[0] <= (now - self.window_size):
                self.requests.popleft()
            
            if len(self.requests) < self.capacity:
                self.requests.append(now)
                return True
            return False
