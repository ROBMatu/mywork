# countiesPlot.py
# Author: Robert O'Brien-Monk
# list of counties, making some appear more than others
# data in a pie chart or a bar chart

import numpy as np
import matplotlib.pyplot as plt

# make the array of occurences
possibleCounties = ['Mayo', 'Galway', 'Rosommon', 'Dublin','Donegal']

# pick 100 of possible counties with the frequence set in p 
counties = np.random.choice(possibleCounties , p=[0.1, 0.3, 0.2, 0.12, 0.28 ], size=(100))

# the number of occurences of each county
# this returns a tuple of the unique values and how many times they appear 
unique, counts = np.unique(counties, return_counts=True)

# pie chart of counties generated
#plt.pie(counts, labels = unique)
#plt.show()

# bar chart of counties generated
plt.bar(unique, counts)
plt.show()