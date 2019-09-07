# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

# 3
# 7 4
# 2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

# NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)

with open("p067_triangle.txt") as fd:
    TRIANGLE_STR = fd.readlines()

def main():
    triangle_nums = [[int(num) for num in row.split(" ")] for row in TRIANGLE_STR]

    result = [triangle_nums[len(triangle_nums) - 1]]

    for i in reversed(range(len(triangle_nums) - 1)):
        row = triangle_nums[i]
        next_row = result[0]

        to_add = [row[j] + max(next_row[j:j+2]) for j in range(len(row))]

        result = [to_add] + result

    print(result[0][0])

if __name__ == "__main__":
    main()
