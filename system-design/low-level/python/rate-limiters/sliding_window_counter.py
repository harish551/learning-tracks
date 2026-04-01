import time
from threading import Lock

class SlidingWindowCounter:

    def __init__(self, capacity, window_size):
        self.capacity = capacity
        self.window_size = window_size
        self.current_window_start = time.monotonic()
        self.current_count = 0
        self.previous_count = 0
        self.lock = Lock()

    def allow_request(self):
        with self.lock:
            now = time.monotonic()

            if now >= self.current_window_start + self.window_size:
                elapsed_windows = int((now - self.current_window_start) // self.window_size)

                if elapsed_windows == 1:
                    self.previous_count = self.current_count
                else:
                    self.previous_count = 0

                self.current_count = 0
                self.current_window_start += elapsed_windows * self.window_size
            
            elapsed_time = now - self.current_window_start
            weight = (self.window_size - elapsed_time) / self.window_size
            effective_count = self.current_count + self.previous_count * weight

            if effective_count >= self.capacity:
                return False
            
            self.current_count += 1
            return True

