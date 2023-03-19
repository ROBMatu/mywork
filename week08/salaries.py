# salaries.py
# Author: Robert O'Brien-Monk
# using module numpy and its functions
# to modify an array

import numpy as np

min_salary = 20000
max_salary = 80000
number_of_entries = 10

# keep random numbers generated the same everytime the program runs
np.random.seed(1)
salaries = np.random.randint(min_salary, max_salary, number_of_entries)
print(salaries)

# add 5000 to each salarie in the array
salaries_plus = salaries + 5000
print(salaries_plus)

# add 5% to each salarie in the array
# then convert that array from floats to integers
salaries_mult = salaries * 1.05
print(salaries_mult)

new_salaries = salaries_mult.astype(int)
print(new_salaries)