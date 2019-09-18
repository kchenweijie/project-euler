# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right,
# and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

def generate_sieve():
    is_prime = [False, False, True] + [True, False] * ((1000000 - 2) // 2)

    for i in range(3, len(is_prime), 2):
        if is_prime[i]:
            for j in range(i*2, len(is_prime), i):
                is_prime[j] = False

    return set(idx for idx in range(2, len(is_prime)) if is_prime[idx])

def main():
    num = 11
    sieve = generate_sieve()

    primes = set()

    while len(primes) < 11:
        num_str = str(num)
        ltr_trunc = [int(num_str[idx:]) for idx in range(len(num_str))]
        rtl_trunc = [int(num_str[0:idx+1]) for idx in range(len(num_str))]

        all_nums = set(ltr_trunc + rtl_trunc)

        if len(all_nums) == len(all_nums & sieve):
            primes.add(num)

        num += 2

    print(sum(primes))

if __name__ == "__main__":
    main()
