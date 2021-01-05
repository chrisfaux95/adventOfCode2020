INPUT_FILE = 'input'
TEST_INPUT = 'test_input'

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


p1(INPUT_FILE)
# p1(TEST_INPUT)