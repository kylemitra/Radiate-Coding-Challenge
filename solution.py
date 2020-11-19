import requests
from PIL import Image

GET_URL = "https://www.random.org/integers/"  # Address to integer generator


def generate_integers(amount: int):
    # Create parameters for API request input
    my_params = {
        'num': str(amount),  # The number of integers requested
        'min': '0',  # For RGB image, we want between 0-255
        'max': '255',  # For RGB image, we want between 0-255
        'col': '3',  # Want Standard 3 column output
        'base': '10',  # Want Base 10 Numbers
        'format': 'plain',  # Want plain text output
        'rnd': 'new'  # Standard randomized format
        }

    # Make GET Request using parameters above
    response = requests.get(GET_URL, params=my_params)

    # Check status code for potential errors
    if response.status_code != 200:
        print(response.status_code + "Error")
    else:  # Return numbers if no error found
        return [int(num) for num in response.text.split()]


def generate_image():
    new_image = Image.new('RGB', (120, 120))  # Creates new image
    return


def create_pixel_list():
    pixel_list = []  # Create new list to hold pixels
    num_pixels = 120 * 120  # 120 x 120 image size
    total_values = num_pixels * 3  # 3 RGB values per pixel

    # NOTE: Since the maximum input of the Integer Generator is
    # 10,000, we need to consider the possibility for when there
    # are more than 10,000 values we need to generate
    while total_values > 10000:
        # Add 10,000 random generated integers to end of pixel list
        pixel_list.extend(generate_integers(10000))
        # Decrement total values by 10,000 to get remaining values needed
        total_values -= 10000

    # Once total_values < 10,000 add remaining values needed to pixel list
    pixel_list.extend(generate_integers(total_values))
    return pixel_list


def main():
    return


if __name__ == '__main__':
    main()
