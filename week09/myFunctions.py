# myFunctions.py
# Author: Robert O'Brien-Monk
# The fibonacci() takes in a number 
# and returns a list containing a Fibonacci sequence of that many numbers.
# E.g. if we called fibonacci(7)  the sequence
#[0, 1 ,1, 2, 3, 5, 8] would be returned
# If the user enters in a number less than 0 we raise a ValueError.
# If the user enters 0 it returns an empty list.


import logging
logging.basicConfig(level=logging.DEBUG)

# function for fibonacci sequence
def fibonacci(number):
    a = 0 
    b = 1
    if number == 0:
        return []
    if number < 0:
       raise ValueError('number must be > 0')
    fibonacciSequence = [0]
    #number += 1
    for i in range(1,number):
        fibonacciSequence.append(b)
        a,b = b, a+b
    logging.debug("%d: %s",number,fibonacciSequence)
    return fibonacciSequence


# test code
if __name__ == '__main__':
    assert fibonacci(7) == [0,1,1,2,3,5,8]
    assert fibonacci(11) == [0,1,1,2,3,5,8,13,21,34,55]
    assert fibonacci(0) == []
    assert fibonacci(1) == [0]
    try:
        fibonacci(-1)
    except ValueError:
        pass
    else:
        assert False
    print("all good")
