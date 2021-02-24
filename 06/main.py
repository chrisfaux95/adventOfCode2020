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
    # WORKS ON EXAMPLE INPUT
    # DOESN'T WORK ON ACTUAL INPUT
    l = [x.split("\n") for x in inp]
    k = [[set(n) for n in x] for x in l]
    j = [len(set.intersection(*x)) for x in k]
    # print(j)
    print("PART 2:", sum(j))

def p2_2(inp):
    # print(inp)
    l = [x.split("\n") for x in inp]
    # print(l)
    t_ans = []
    for g in l:
        # print(g)
        shared_ans = set(g[0])
        for p in g:
            shared_ans &= set(p)
        t_ans.append(len(shared_ans))
    print("PART 2:", sum(t_ans))
    

PUZZLE_INPUT = readfile(INPUT_FILE)
# PUZZLE_INPUT = readfile(TEST_INPUT)

p1(PUZZLE_INPUT)
p2(PUZZLE_INPUT)
