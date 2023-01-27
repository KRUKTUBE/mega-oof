import random
a = random.randint(1,9)
b = random.randint(0,9)
c = random.randint(0,9)

def rand(a, b, c):
    if a == b:
        b = b + 1
        
    if b >= 10:
        b = b - 2
    
    if b == c:
        c = c + 1
    
    if c >= 10:
        c = c - 2
    plus =str(a) + str(b) + str(c)
    