from itertools import combinations
from functools import reduce
test_input = [
    1721,
    979,
    366,
    299,
    675,
    1456
]

with open('input') as file:
    lines = file.readlines()
in_expenses = list(map(int, lines))


def product(n):
    return reduce(lambda a, b: a*b, n, 1)


# Part 1


def p1(i):
    inp_combo = combinations(i, 2)
    # print(inp_combo)
    for i in inp_combo:
        # print(i, sum(i))
        if sum(i) == 2020:
            return product(i)
# if i[0] + i[1] == 2020:
#     return i[0] * i[1], i

# Part 2


def p2(i):
    inp_combo = combinations(i, 3)
    for i in inp_combo:
        if sum(i) == 2020:
            return product(i), i


# print(p1(test_input))
# print(p1(in_expenses))

print(p2(in_expenses))
