primes = [2]
sums = 0
i = 1
while i < 2000000:
    i += 2
#    print(i)
    notfailed = True
    for x in range (int(len(primes)/2)):
        if notfailed == True:
            if i%primes[x] == 0:
                notfailed = False
        else:
            pass
    if notfailed == True:
        primes.append(i)
        print(i)
        sums += i
    
print(len(primes))
print(primes[-1])
print(sum)