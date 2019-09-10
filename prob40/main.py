# An irrational decimal fraction is created by concatenating the positive integers:

# 0.123456789101112131415161718192021...

# It can be seen that the 12th digit of the fractional part is 1.

# If dn represents the nth digit of the fractional part, find the value of the following expression.

# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

def main():
    str_buf = ""
    n = 1

    while len(str_buf) < 1000000:
        str_buf += str(n)
        n += 1

    total = 1
    for i in range(7):
        total *= int(str_buf[int(10**i)-1])

    print(total)

if __name__ == "__main__":
    main()
