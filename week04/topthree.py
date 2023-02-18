# topthree.py
# Author: Robert O'Brien-Monk
# generate 3 random numbers between 0-100
# print the top 3 

import random

how_many = 10
top_how_many = 3
range_from = 0
range_to = 100

nums = []

for i in range(0,how_many):
    nums.append(random.randint(range_from,range_to))
print(f"{how_many} random numbers {nums}")

# altering list
nums.sort(reverse = True)
print (f"The top {top_how_many} are: {nums[0:top_how_many]}")