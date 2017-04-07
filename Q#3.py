n, i, prime_factors = 600851475143, 3, []
# know n is not even, so start at 3 to see if it's a factor
while n != 1:
    if n % i == 0:
        prime_factors.append(i)
        # keep track of all prime factors
        n = n/i
    else:
        # increment factors through all odd numbers
        i += 2
        
print prime_factors[-1] 
# only print the largest prime factor
