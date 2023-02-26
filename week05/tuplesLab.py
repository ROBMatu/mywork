# tuplesLab.py
# Author: Robert O'Brien-Monk
# tuple storing months of the year
# and a tuple extracted from the first storing summer months

months_of_year = ("January", "February", "March", "April", "May", "June", "July",
     "August", "September", "October", "November", "December")

summer= months_of_year[4:7]

for month in summer:
    print(month)