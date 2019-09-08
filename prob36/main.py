# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

# (Please note that the palindromic number, in either base, may not include leading zeros.)

def to_binary(num):
    return "{0:b}".format(num)

def is_palindrome(string):
    return string == string[::-1]

def main():
    valid = []

    for i in range(1, 1000000):
        if is_palindrome(str(i)) and is_palindrome(to_binary(i)):
            valid.append(i)

    print(sum(valid))

if __name__ == "__main__":
    main()
