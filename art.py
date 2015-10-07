from turtle import *
import math

mode("logo")
ht()

a = 0
b = 1
c = 1
fib = [1]
for n in range(10):
    fib.append(a + b)
    c = b
    b += a
    a = c

pd()
for i in fib:
    goto(math.exp(i) * math.cos(i), math.exp(i) * math.sin(i))


input("Press enter to exit.")
