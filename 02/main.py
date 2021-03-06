INPUT_FILE = 'input'
TEST_INPUT = 'test_input'


# with open('input') as file:
#     lines = file.readlines()

# Part 1

def p1(i):
    with open(i) as file:
        lines = file.readlines()
    # print(lines)
    l = [x.split() for x in lines]
    # print(l)
    valid_pass = 0
    for item in l:
        # print(item)
        [low,high] = item[0].split('-')
        [low,high] = [int(low), int(high)]
        c = item[2].count(item[1][:-1])
        # print(c, low, high)
        if c >= low and c <= high:
            valid_pass += 1
        # print(item[2].count(item[1][:-1]))
    print("Valid Passwords:", valid_pass)


# Part 2:

def p2(i):
    with open(i) as file:
        lines = file.readlines()
    l = [x.split() for x in lines]
    valid_pass = 0
    for item in l:
        [start, end] = item[0].split('-')
        [start, end] = [int(start), int(end)]
        # print(start,end)
        char_check = 0
        if item[2][start - 1] == item[1][0]:
            char_check += 1
        if item[2][end - 1] == item[1][0]:
            char_check += 1
        if char_check == 1:
            valid_pass += 1
    print("Valid Passwords", valid_pass)





# p1(TEST_INPUT)
# p1(INPUT_FILE)
# p2(TEST_INPUT)
p2(INPUT_FILE)