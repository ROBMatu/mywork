# isEven.py
# Author: Robert O'Brien-Monk
# Tell user if number is even or odd

num = int(input("Enter a whole number: "))
while num != -1:
    if num % 2 == 0:
        print(f"{num} is an Even number!")
        num = int(input("Enter a  whole number (-1 to quit): "))
    else:
        print(f"{num} is a Odd number!")
        num = int(input("Enter a whole number (-1 to quit): "))