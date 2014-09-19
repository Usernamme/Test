def quit_trigger(numlimit,  a, b):
    if b >= numlimit > 0:
        return True
    else: return False

def fibs(numlimit, limit): #numlimit - highest number generated - use 0 for no numlimit | limit - number of numbers generated
    a = 1
    b = 1
    for x in range(1, limit):
        a += b
        b += a
        if quit_trigger(numlimit, a, b):
            return (a, b)
    return (a, b)
