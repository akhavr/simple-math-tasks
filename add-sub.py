from random import *

for i in range(10):
    print "%s + %s =" % (choice(range(100)), choice(range(100)))

print

for i in range(10):
    a = choice(range(100))
    b = choice(range(100))
    print "%s - %s = " % (max(a,b), min(a,b))
