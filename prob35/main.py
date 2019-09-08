# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

# How many circular primes are there below one million?

def generate_rotations(num):
    num_str = str(num)

    rotations = []

    for _ in range(len(num_str)):
        rotations.append(num_str)

        first_digit = num_str[0]
        remainder = num_str[1:]

        num_str = remainder + first_digit

    return rotations

def generate_sieve():
    is_prime = [False, False, True] + [True, False] * ((1000000 - 2) // 2)

    for i in range(3, len(is_prime), 2):
        if is_prime[i]:
            for j in range(i*2, len(is_prime), i):
                is_prime[j] = False

    return set(idx for idx in range(2, len(is_prime)) if is_prime[idx])

def main():
    primes = generate_sieve()

    values = set()

    for i in range(2, 1000000):
        rotations = generate_rotations(i)

        if i not in values and all(int(rotation) in primes for rotation in rotations):
            values = values | set(int(rotation) for rotation in rotations)

    print(len(values))

if __name__ == "__main__":
    main()
