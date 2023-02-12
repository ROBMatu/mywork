# floor.py
# Author: Robert O'Brien-Monk
# input of float return integer thats rounded down

import math

float_to_floor = float(input("Enter a number that has a decimal place: "))

# using the floor() function from math to return an integer rounded down
num_floor = math.floor(float_to_floor)

print(f"{float_to_floor} floored is {num_floor}")
