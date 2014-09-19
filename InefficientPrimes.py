def isprime(x):
    for n in primes: 
        if not x % n == 0:
            return False
    else:
        return True
primes = []


def primecalc(upperlimit):
    for x in range(2,upperlimit):
        if isprime(x):
            primes.append(int(x))
            print(x)
