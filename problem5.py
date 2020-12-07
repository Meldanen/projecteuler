# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
import math

max = 10
smallestNumber = math.inf

numbersToDivideWith = list(range(1, max + 1))

i = 1
while True:
    moduloNumberinos = list(map((lambda item: i % item == 0), numbersToDivideWith))
    if all(moduloNumberinos):
        smallestNumber = i
        break
    i = i + 1
print(smallestNumber)
# Answer : 232792560