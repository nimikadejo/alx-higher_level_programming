#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number > 0:
    last = number % 10
else:
    last = ((number * -1) % 10) * -1
if (last > 5):
    print("Last digit of {} is {} and is greater than 5".format(number, last))
elif (last == 0):
    print("Last digit of {} is {} and is zero".format(number, last))
elif (last < 6) and (last != 0):
    print(f"Last digit of {number:d} is {last:d} and is less than 6 and not zero")
