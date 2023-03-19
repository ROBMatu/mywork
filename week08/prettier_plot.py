# prettier_plot.py
# Author: Robert O'Brien-Monk
# add legend, title and axis labels

import numpy as np
import matplotlib.pyplot as plt

min_salary = 20000
max_salary = 80000
num_of_entries = 100

# make sure random numbers are the same each time
np.random.seed(1)
salaries = np.random.randint(min_salary, max_salary, num_of_entries)
ages = np.random.randint(low = 21, high = 65, size = num_of_entries)
plt.scatter(ages, salaries, color= 'green')


# x squared line plot
xpoints = np.array(range(1, 101))
# multiply each entry by itself to get square values
ypoints = xpoints * xpoints 
plt.plot(xpoints, ypoints, color= 'blue', label = "x squared")

plt.title("Random plot")
plt.xlabel("Age")
plt.ylabel("Salaries")
plt.legend()

#plt.show() 
plt.savefig('prettierPlot.png')