# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation
# of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically,
# we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

# 012   021   102   120   201   210

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

from functools import reduce

def factorial(num):
    return reduce(lambda x, y: x*y, range(1, num+1))

def main():
    num = 1000000
    selections = []
    for i in reversed(range(1, 10)):
        fact = factorial(i)
        selections.append(num // fact)
        num %= fact

    digits = list(range(10))

    output = ""
    for sel in selections:
        output += str(digits[sel])
        digits = digits[:sel] + digits[(sel+1):]

    output += str(digits[0])

    print(output) # Go one permutation before this one because obo error

if __name__ == "__main__":
    main()
