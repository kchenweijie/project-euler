# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

def main():
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    curr = 31

    while len(primes) < 10001:
        if not any(curr % prime == 0 for prime in primes):
            primes.append(curr)
        else:
            curr += 2

    print(primes[-1])

if __name__ == "__main__":
    main()
