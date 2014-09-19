def quit_trigger(numlimit,  a, b):
    if b >= numlimit > 0:
        return True
    else:
        return False

def fibs(numlimit, limit): 
#numlimit - highest number generated - use 0 for no numlimit | limit - number of times it runs: EACH RUN PRODUCES TWO NEW NUMBERS
    a = 1
    b = 1
    fibonacci = []
    fibonacci.extend([a,b])
    for x in range(1, limit):
        a += b
        b += a
        fibonacci.extend([a,b])
        if quit_trigger(numlimit, a, b):
            return fibonacci
    return fibonacci
