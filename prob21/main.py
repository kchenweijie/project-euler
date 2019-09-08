# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

import math

def factors_of_num(num):
    factors = []

    for factor in range(1, math.floor(num**0.5)):
        if num % factor == 0:
            factors.append(factor)

    factors += [num // factor for factor in factors if factor != 1]

    if num % int(math.floor(num**0.5)) == 0:
        factors.append(int(math.floor(num**0.5)))

    return sorted(factors)

def amicable(num):
    factors = factors_of_num(num)
    potential_pair = sum(factors)

    potential_pair_factors = factors_of_num(potential_pair)
    potential_pair_sum = sum(potential_pair_factors)

    if potential_pair_sum == num and potential_pair != num:
        return potential_pair
    return None

def main():
    numbers = set()

    for i in range(1, 10000):
        if i not in numbers:
            pair = amicable(i)

            if pair is not None:
                numbers = numbers | {i, pair}

    print(sum(numbers))

if __name__ == "__main__":
    main()
