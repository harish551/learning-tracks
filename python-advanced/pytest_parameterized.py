'''
Parameterized Tests with pytest
In pytest, you can use the `@pytest.mark.parametrize` decorator 
to run a test function with different sets of parameters. 

This allows you to easily test multiple scenarios without 
having to write separate test functions for each case.
'''

import pytest

@pytest.mark.parametrize("input, expected", [
    (1, 2),  # Test case 1: input 1 should return 2
    (2, 3),  # Test case 2: input 2 should return 3
    (3, 4),  # Test case 3: input 3 should return 4
])

def test_increment(input, expected):
    assert input + 1 == expected 
