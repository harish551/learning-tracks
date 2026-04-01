import time
from threading import Lock

class FixedWindow:

    def __init__(self, capacity, window_size):
        self.capacity = capacity
        self.window_size = window_size
        self.current_window = int(time.time() // self.window_size)
        self.count = 0
        self.lock = Lock()

    def allow_request(self):
        with self.lock:
            now_window = int(time.time() // self.window_size)

            if self.current_window != now_window:
                self.count = 0
                self.current_window = now_window
        
            if self.count < self.capacity:
                self.count += 1
                return True
            return False

