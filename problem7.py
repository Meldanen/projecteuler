# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10001st prime number?

max = 10001

def getPrimes(upperBound):
    primes = [2]
    i = 3
    while len(primes) < upperBound:
        prime = True
        for j in range(2, i):
            if i % j == 0:
                prime = False
                break
        if prime:
            primes.append(i)
        i = i + 1
    return primes

primesFinal = getPrimes(max)
print(primesFinal)
print(len(primesFinal))

# Answer : 104743