'''
Context manager implementation
A context manager is a Python object that defines the runtime context
to be established when executing a with statement.

Context managers are used to manage resources such as file streams,
network connections, and locks. They ensure that resources are properly
acquired and released, even in the case of exceptions.
'''


class MyContext:
    def __enter__(self):
        print("Entering context")
        return "resource"

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")
        if exc_type:
            print(f"Exception: {exc_value}")
        return False  # re-raises exception if any

with MyContext() as res:
    print(f"Using {res}")


from contextlib import contextmanager

@contextmanager
def file_context(file_name, mode='r'):
    file = None
    try:
        file = open(file_name, mode)
        yield file
    finally:
        if file:
            print("Closing file")
            file.close()

with file_context('example.txt', 'w') as f:
    f.write("Hello, World!")