import pytest

def triple(x):  # Function to test
    return x * 3

# List of values for testing containing input and expected result
test_data = [
    (5, 15), ('a', 'aaa'), (0, 0), ([True], [True, True, True])
]  

# Parametrize the test with the test data; the first argument is a string mapping 
# parameters to the test data
@pytest.mark.parametrize("input,expected", test_data)  
def test_triple(input, expected): 
    assert triple(input) == expected   # Test the function with the parameters
