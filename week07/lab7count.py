#lab7count.py
# Author: Robert O'Brien-Monk
# function readnumber() reads in a number from a file
# function writenumber() overwrites a number in a file
# https://stackoverflow.com/questions/63692472/to-show-how-many-times-user-has-run-the-script

FILENAME = "count.txt"

def readNumber():
    with open(FILENAME) as f:
        number = int(f.read())
        return number
    
#num=readNumber()
#print(num)

# write takes a string so we need to convert
def writeNumber(number):
   with open(FILENAME, "wt") as f:
        f.write(str(number))

#writeNumber(3)
count = 0

def code_to_run():
  num = readNumber()
  num += 1
  writeNumber(num)
  global count
  count = count + 1

runprogram = True
run = 0
while runprogram == True:
   print("You have run the code {} times".format(count))
   run = str(input("Shall I run the code? (y/n): "))
   if run == "y":
      code_to_run()
   else:
      runprogram = False




