# Variables
global primes
primes = [2]
l = []
notfailed = True


# Functions
def prime(n, l):
    for i in range(len(primes)):
        if n%primes[i] == 0:
            l.append(primes[i])
            return prime(int(n/primes[i]), l)
    return (n, l)


# Generating Prime Numbers
for i in range(3, 10000):
    notfailed = True
    for x in range(len(primes)):
        if notfailed == True:
            if i%primes[x] == 0:
                notfailed = False
        else:
            pass
    if notfailed == True:
        primes.append(i)




# Display
divisors = prime(600851475143, l)
listp = divisors[1]
print(divisors)
