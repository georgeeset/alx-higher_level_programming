#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if (i % 3 == 0) and (i % 5 == 0):
            strng = "FizzBuzz"
        elif i % 3 == 0:
            strng = "Fizz"
        elif i % 5 == 0:
            strng = "Buzz"
        else:
            strng = str(i)
        print("{}".format(strng), end=' ')
