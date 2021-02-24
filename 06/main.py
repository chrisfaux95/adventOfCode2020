INPUT_FILE = 'input'
TEST_INPUT = 'test_input'

def readfile(f):
    with open(f) as file:
        inp = file.read().strip().split("\n\n")
    return inp

def p1(inp):
    l = [set(x.replace('\n', '')) for x in inp]
    k = [len(x) for x in l]
    print("PART 1:", sum(k))

def p2(inp):
    l = [x.split("\n") for x in inp]
    k = [[set(n) for n in x] for x in l]
    j = [len(set.intersection(*x)) for x in k]
    # print(j)
    print("PART 2:", sum(j))

    

PUZZLE_INPUT = readfile(INPUT_FILE)
# PUZZLE_INPUT = readfile(TEST_INPUT)

p1(PUZZLE_INPUT)
p2(PUZZLE_INPUT)
