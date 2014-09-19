import math

def fibs(numlimit, limit): #numlimit - highest number generated, limit - number of numbers generated
    a = 1
    b = 1
    
    while True:
        a += b
        b += a
        
