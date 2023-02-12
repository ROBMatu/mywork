# convert.py
# Author: Robert O'Brien-Monk
# take in a float and convert it to integer

dollars_in = float(input("Enter your lodgement as a decimal number: "))

dollars_to_cent = abs(int(dollars_in * 100))

print(f"That amount in cents is: {dollars_to_cent}")