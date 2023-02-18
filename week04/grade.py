# grade.py
# Author: Robert O'Brien-Monk
# input of student percentage mark and return corresponding grade

percent_mark = float(input("Enter percentage mark: "))

if percent_mark < 0 or percent_mark > 100:
    print("Only from 0 to 100 allowed")
elif percent_mark < 40:
    print("Fail")
elif percent_mark < 50:
    print("Pass")
elif percent_mark < 60:
    print("Merit 2")
elif percent_mark < 70:
    print("Merit 1")
else:
    print("distinction")


