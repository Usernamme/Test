import time
s = time.time()

def isprime(x):
    for n in primes: 
        if x % n == 0:
            return False
    else:
        return True

possibilities = []
poss = open("Possibilities.txt", "r")
for line in poss:
    possibilities.append(line.strip())
primes = [2, 3, 5, 7]
pri = open("Primes.txt","r+")

for x in possibilities:
    if isprime(int(x)):
       primes.append(int(x))
       pri.write("%s\n" % x)

print(time.time()-s)
pri.close()
