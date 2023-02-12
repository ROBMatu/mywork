# randomGenerator.py
# Author: Robert O'Brien-Monk
# prints random number between 1 and 10

import random

start_num = int(input("Enter a start number for your range: "))
end_num = int(input("Enter another number for the end of your range: "))

num = random.randint(start_num,end_num)
print(f"Here is a random number {num}")

