# average.py
# Author: Robert O'Brien-Monk
# input numbers from user into a list
# until user enters 0 to quit
# then print the numbers, with the overall average

nums_list = []

num = int(input("Enter a number (0 to quit): "))

while num != 0:
    nums_list.append(num)
    num = int(input("Enter next number (0 to quit): "))

for element in nums_list:
    print(element)

avg_num = float(sum(nums_list)/len(nums_list))
print(f"The average of the numbers you entered is: {avg_num}")

