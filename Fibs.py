#checks if the latest fib num is under the limit
def quit_trigger(numlimit,  a, b):
    if b >= numlimit > 0:
        return True
    else:
        return False

"""returns a list of fib numbers - [1, 1, 2, 3, 5, 8, ...]
   numlimit - highest number generated - use 0 for no numlimit 
   limit    - number of times it runs: each run produces 2 numbers - use half of the number of numbers you want to generate"""
def fibs(numlimit, limit): 
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
