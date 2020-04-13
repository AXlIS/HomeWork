from itertools import count
from math import factorial


def fibo_gen():
    for el in count(1):
        yield factorial(el)


index = 0
for i in fibo_gen():
    if index > 1000:
        break
    else:
        print(i)
        index += 1
