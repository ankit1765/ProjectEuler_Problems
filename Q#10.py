#Question No. 10
#Ankit Mittal
#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.


def prime_sum(n):
    
    if n < 2: return 0
    if n == 2: return 2
    if n % 2 == 0: n += 1
    
    primes = [True] * n
    primes[0:2] = [None] * 2
    sum = 0
    
    for ind,val in enumerate(primes):
        if val is True and ind > n ** 0.5 + 1:
            sum += ind
        elif val is True:
            primes[ind*2::ind] = [False] * (((n - 1)//ind) - 1)
            sum += ind
    return sum


sum = prime_sum(2*10**6)

print sum
