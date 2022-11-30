#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
strNum = str(number)
last = strNum[-1]
lastNum = int(last)
if number < 0:
    lastNum *= -1
msg1 = f"Last digit of {number} is {lastNum} "
if lastNum > 5:
    msg1 += "and is greater than 5"
elif lastNum == 0:
    msg1 += "and is 0"
elif lastNum < 6 and last != 0:
    msg1 += "and is less than 6 and not 0"
print(msg1);
