# normalise.py
# Author: Robert O'Brien-Monk
# input string then strip whitespace and convert to lowercase
# and return the length before and after strip()

input_string = input("Enter a string: ")

processed_string = input_string.strip().lower()

len_input = len(input_string)
len_processed = len(processed_string)

print(f"The string you entered has been normalised to: {processed_string}")
print(f"The string was reduced from {len_input} to {len_processed} characters in length.")
