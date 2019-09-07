# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 21000?

def main():
    value = 2**1000

    value_str = str(value)

    print(sum(int(digit) for digit in value_str))

if __name__ == "__main__":
    main()
