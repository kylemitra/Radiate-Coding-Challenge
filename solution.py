import requests

GET_URL = "https://www.random.org/integers/"  # Address to integer generator


def generate_integers(amount: int):
    # Check that amount if valid
    if amount < 1 or amount > 10000:
        print('Amount must be in range 1-10000')

    # Create parameters for API request input
    my_params = {
        'num': str(amount),  # The number of integers requested
        'min': '0',  # For RGB image, we want between 0-255
        'max': '255',  # For RGB image, we want between 0-255
        'col': '3',  # Columns for Red, Green, Blue
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


def main():
    return


if __name__ == '__main__':
    main()
