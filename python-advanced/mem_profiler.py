'''
Memory profiler implementation
A memory profiler is a tool that measures the memory usage of a Python program.
It helps identify memory leaks and optimize memory consumption.
'''

import sys
from memory_profiler import profile

@profile
def my_function():
    a = [i for i in range(100000)]
    b = [i*i for i in a]
    del a
    return b


if __name__ == "__main__":
    b = my_function()
    print(sys.getsizeof(b))  # Output: Memory usage of the list b