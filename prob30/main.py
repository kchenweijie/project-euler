# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

# 1634 = 14 + 64 + 34 + 44
# 8208 = 84 + 24 + 04 + 84
# 9474 = 94 + 44 + 74 + 44
# As 1 = 14 is not a sum it is not included.

# The sum of these numbers is 1634 + 8208 + 9474 = 19316.

# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

def find_upper_limit():
    num_digits = 1

    while num_digits*(9**5) > int("9"*num_digits):
        num_digits += 1

    return int("9"*num_digits)

def main():
    upper_limit = find_upper_limit()

    valid = []

    for i in range(2, upper_limit+1):
        digit_power_sum = sum(int(digit)**5 for digit in str(i))

        if digit_power_sum == i:
            valid.append(i)

    print(sum(valid))

if __name__ == "__main__":
    main()
