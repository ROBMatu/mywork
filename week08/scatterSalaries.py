# scatterSalaries.py
# Author: Robert O'Brien-Monk
# scatter plot of salaries against ages

import numpy as np
import matplotlib.pyplot as plt

min_salary = 20000
max_salary = 80000
num_of_entries = 100

# makes sure random numbers are the same each time
np.random.seed(1)
salaries = np.random.randint(min_salary, max_salary, num_of_entries)
ages = np.random.randint(low=21, high = 65, size = num_of_entries) 

# generate scatter plot
plt.scatter(ages, salaries )
plt.show()
 