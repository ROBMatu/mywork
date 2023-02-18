# guess2.py
# Author: Robert O'Brien-Monk
# guess a number until the randomly selected correct number is guessed
# hints if too high or too low

import random
# computer chooses random number from 0 to 100 inclusive
target_num = random.randint(0,100)

guess = int(input("Guess the secret nummber: "))

while guess != target_num:
    if guess < target_num:
        print("Too low")
    else:
        print("Too high")
    guess = int(input("Guess again: "))

print(f"Well done you guessed the secret number: {target_num}, shhh Don't tell.")

