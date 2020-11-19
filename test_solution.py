import pytest
from imageio import imread


@pytest.mark.parametrize('input_amount, expected', [
    (1, True),
    (3, True),
])
# Test to ensure generate integers generates random numbers
def test_generate_integers(input_amount, expected):
    # Import original generate_integers function
    from solution import generate_integers
    # Store output for given input_amount
    answer = generate_integers(input_amount)

    # Check to make sure that answer is an integer
    for value in answer:
        if isinstance(value, int):
            test_result = True
        else:
            test_result = False
    # Output whether answer is correct
    assert test_result == expected


@pytest.mark.parametrize('filepath, expected_width, expected_height', [
    ('./my_RBG_image.png', 120, 120),
])
# Test to ensure that image is correct size
def test_image_size(filepath, expected_width, expected_height):
    # Read in the image from filepath
    my_image = imread(filepath)
    # Store the image attributes
    height, width, c = my_image.shape
    # Check if width is equal to expected
    assert width == expected_width
    # Check if width is equal to expected
    assert height == expected_height
