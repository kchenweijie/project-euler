# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

TARGET = 600851475143

def main():
    target = TARGET
    factor = 2

    while factor != target:
        if target % factor == 0:
            target /= factor
        else:
            factor += 1

    print(factor)

if __name__ == "__main__":
    main()
