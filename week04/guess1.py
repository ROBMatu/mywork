# guess1.py
# Author: Robert O'Brien-Monk
# guess a number until the correct number is guessed

target_num = 42

guess = int(input("Guess the secret nummber: "))

while guess != target_num:
    print("Wrong")
    guess = int(input("Guess again: "))

print(f"Well done you guessed the secret number: {target_num}, shhh Don't tell.")
