# div.py
# Author: Robert O'Brien-Monk
# divide to numbers and return integer and remainder

one_num = int(input("Enter your first number: "))
two_num = int(input("Enter your next number you want to divide by: "))

ans_div = one_num // two_num
ans_remainder = one_num % two_num

print(f"{one_num} divided by {two_num} is {ans_div} with remainder of {ans_remainder}")