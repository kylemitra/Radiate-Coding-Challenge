# Radiate-Coding-Challenge

## Instructions
Random.org generates high-quality random numbers using several radios. 
These radios capture atmospheric noise, which is primarily created by 
lightning discharges in thunderstorms. (Who knew 3.5 million lightning 
flashes occur daily?!) While we’re not quite in gambling or crypto yet, 
we hope you find this challenge interesting!

Your task is to write a function that uses the Random.org HTTP API to 
create an RGB image that measures 120 by 120 pixels, where each pixel 
is a random RGB color. BMP, PNG, or JPG images are fine. Use whichever 
language you’d prefer.

NOTE: Random.org limits IP addresses to a specific daily bit allowance. 
Make sure you read the guidelines, or you risk being temporarily banned!

Push your code and generated image to a newly created GitHub repo that 
is publicly accessible. Include any tests you may have written, and be 
sure to specify any dependencies. You have up to three hours to complete 
this challenge. Send me an email when you have finished.

## Accessing solution
Begin by cloning this repository to your local machine.  
  
Next, install the required packages by running `pip install -r requirements.txt`  
NOTE: If this command does not work, try `pip3 install -r requirements.txt` (It is 
dependent on your version of Python)  
  
Next, run the solution script via the following command:  
`python solution.py`  

This will produce a new RGB image on your local machine. It should resemble the image
below which is the image I've generated for this challenge.  
![Image of my RGB square](https://github.com/kylemitra/Radiate-Coding-Challenge/blob/main/my_RBG_image.png?raw=true)  

## Testing the solution
I choose to utilize the Pytest package to run automated tests that verify the functions in my code.
To run my Pytest file run `pytest -v` . It show that all the test cases I've included have passed.
For this project, I choose to test that my API call would correctly generate a list of digits and 
that the produced image is of the correct size 120x120.