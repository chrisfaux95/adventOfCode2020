INPUT_FILE = 'input'
TEST_INPUT = 'test_input'

from functools import reduce
# Inital solution of part 1


def p1(i):
    with open(i) as file:
        lines = file.readlines()
    l = [x[:-1] for x in lines]
    # print(l)
    # for i in l: print(len(i))
    [x, y] = [0, 0]
    [w, h] = [len(l[0]), len(l)]
    # print(x,y,w,h)
    trees = 0
    for row in l:
        if x >= w:
            x %= w
            # print(x)
        # print(row[x])
        if row[x] == '#':
            trees += 1
            # print(x,y)
        x += 3
        y += 1
    print("Trees hit:", trees)

# revised solution of part 1 with checking functionized


def p1_revised(i):
    with open(i) as file:
        lines = file.readlines()
    l = [x[:-1] for x in lines]
    print(slope_check([3, 1], l))

# part 2 solution


def p2(i):
    with open(i) as file:
        lines = file.readlines()
    l = [x[:-1] for x in lines]
    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    sc = lambda a: slope_check(a,l)
    tree_list = list(map(sc, slopes))
    print(reduce(lambda a,b: a*b, tree_list))
    

    


# slope checker function
def slope_check(sxy, l):
    [sx, sy] = sxy
    [x, y] = [0, 0]
    [w, h] = [len(l[0]), len(l)]
    trees = 0
    while y <= h:
        if x >= w:
            x %= w
        # print(x,y)
        if y >= h:
            break
        if l[y][x] == "#":
            trees += 1
        x += sx
        y += sy
    return trees


# p1(INPUT_FILE)
# p1(TEST_INPUT)

# p1_revised(INPUT_FILE)
# p1_revised(TEST_INPUT)

p2(INPUT_FILE)
# p2(TEST_INPUT)
