# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

# Find the sum of all numbers which are equal to the sum of the factorial of their digits.

# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

factorials = {"0": 1}

def generate_factorials():
    prod = 1

    for i in range(1, 10):
        prod *= i

        factorials[str(i)] = prod

def find_upper_limit():
    num_digits = 1

    while num_digits*(factorials["9"]) > int("9"*num_digits):
        num_digits += 1

    return int("9"*num_digits)

def main():
    generate_factorials()

    upper_limit = find_upper_limit()

    valid = []

    for i in range(3, upper_limit+1):
        digit_sum = sum(factorials[digit] for digit in str(i))

        if digit_sum == i:
            valid.append(i)

    print(sum(valid))

if __name__ == "__main__":
    main()
