from pyprimesieve import primes

#Start the prime search with 3
primesList = primes(3, 100000000)

#2 is the first prime
prevPrime = 2

#Create our set
numberOfGaps = set()

#Loop through the primes
for prime in primesList:
    #Add the gap between current prime and previous prime
    numberOfGaps.add(prime - prevPrime)
    #Update previous prime
    prevPrime = prime

#Display how many gaps there are
print(len(numberOfGaps))