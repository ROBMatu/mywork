# randomNumListPop.py
# Author: Robert O'Brien-Monk
# 10 random numbers in queue list 
# print out the list repeatedly but removing
# an element each time using pop()

import random

queue = []
number_of_numbers = 10
range_to = 100
current_num = 0

for n in range(0,number_of_numbers):
    queue.append(random.randint(0,range_to))

print(f"Queue is {queue}")

while len(queue) != 0:
    current_num = queue.pop(0)
    print(f"Current number is {current_num} and the queue is {queue}")
