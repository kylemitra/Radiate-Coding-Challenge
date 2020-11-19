import requests
from PIL import Image
import numpy as np

GET_URL = "https://www.random.org/integers/"  # Address to integer generator


def generate_integers(amount: int):
    # Create parameters for API request input
    my_params = {
        'num': str(amount),  # The number of integers requested
        'min': '0',  # For RGB image, we want between 0-255
        'max': '255',  # For RGB image, we want between 0-255
        'col': '3',  # Columns for Red, Green, Blue Values
        'base': '10',  # Want Base 10 Numbers
        'format': 'plain',  # Want plain text output
        'rnd': 'new'  # Standard randomized format
        }

    # Make GET Request using parameters above
    response = requests.get(GET_URL, params=my_params)

    # Check status code for potential errors
    if response.status_code != 200:
        print(str(response.status_code) + " Error")
    else:  # Return numbers if no error found
        return [int(num) for num in response.text.split()]


def create_pixel_list():
    pixel_list = []  # Create new list to hold pixels
    num_pixels = 120 * 120  # 120 x 120 image size
    total_values = num_pixels * 3  # 3 RGB values per pixel
    # total_values = 43,200

    # NOTE: Since the maximum input of the Integer Generator is
    # 10,000, we need to account for the fact that we require more than
    # the allowed amount of values.
    while total_values > 10000:
        # Add 10,000 random generated integers to end of pixel list
        pixel_list.extend(generate_integers(10000))
        # Decrement total values by 10,000 to get remaining values needed
        total_values -= 10000

    # Once total_values < 10,000 add remaining values needed to pixel list
    pixel_list.extend(generate_integers(total_values))
    return pixel_list


def generate_image():
    pixel_list = create_pixel_list()  # Generate random list of pixels
    np_pixel_array = np.array(pixel_list)  # Create numpy array of pixels
    np_pixel_array = np_pixel_array.reshape((120*120, 3))  # Resize numpy array
    new_image = Image.new('RGB', (120, 120))  # Creates new image
    new_image.putdata([tuple(pixel) for pixel in np_pixel_array])  # Input pixels
    new_image.save("my_RBG_image.png")  # Save image
    print('Image successfully generated')  # Message to indicate success


if __name__ == '__main__':
    generate_image()
