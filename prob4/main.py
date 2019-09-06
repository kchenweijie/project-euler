# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def main():
    numbers = [x * y for x in range(100, 1000)
                     for y in range(100, 1000)]

    palindromes = [number if str(number) == str(number)[::-1] else 0 for number in numbers]

    print(max(palindromes))

if __name__ == "__main__":
    main()
