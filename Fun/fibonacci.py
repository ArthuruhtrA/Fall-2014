"""
    Ported from PHP
"""

iterations = 20
a = 1
b = 1
c = "1"
print(c)
c += str(a)
for i in range(iterations):
    print (c)
    a += b
    b += a
    c += str(a) + str(b)
print(c)
iterations = 20
a = 1
b = 1
c = "1"
c += "|" + str(a)
for i in range(iterations):
    a += b
    b += a
    c += "|" + str(a) + "|" + str(b)
print(c)

import time
time.sleep(15)
