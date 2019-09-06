# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

def main():
    prime_str = [True]*2000000

    for idx in range(2, 2000000):
        if prime_str[idx]:
            for jdx in range(idx*2, 2000000, idx):
                prime_str[jdx] = False

    primes = [idx for idx in range(2, 2000000) if prime_str[idx]]

    print(sum(primes))

if __name__ == "__main__":
    main()
