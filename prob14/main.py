# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

chain_lengths = {}

def get_chain(n):
    if n == 1:
        return [("1", 1)]
    if str(n) in chain_lengths:
        return [(str(n), chain_lengths[str(n)])]
    if n % 2 == 0:
        remaining_chain = get_chain(n // 2)
    else:
        remaining_chain = get_chain(3*n + 1)
    return [(str(n), remaining_chain[0][1] + 1)] + remaining_chain

def main():
    chain_lens = [0]

    for i in range(1, 1000000):
        chain = get_chain(i)

        chain_lengths.update(chain)

        chain_len = chain[0][1]

        chain_lens.append(chain_len)

    max_len = max(chain_lens)
    print(chain_lens.index(max_len), max_len)

if __name__ == "__main__":
    main()
