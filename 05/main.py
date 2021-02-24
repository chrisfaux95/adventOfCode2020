INPUT_FILE = 'input'

def bin_enc(s):
    return s.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')

def p1(i):
    seats = map(lambda n: int(bin_enc(n), 2), i)
    return max(seats)

def p2(i):
    seats = map(lambda n: int(bin_enc(n), 2), i)
    sorted_seats = sorted(seats)
    # print(sorted_seats)
    for i in sorted_seats:
        if i+1 not in sorted_seats:
            print(i+1)

# b = bin_enc("FBFBBFFRLR")
# b = bin_enc("BFFFBBFRRR")
# b = bin_enc("FFFBBBFRRR")
# b = bin_enc("BBFFBBFRLL")

# print(b, int(b, 2))

r = open(INPUT_FILE).read().strip('\n')
input = r.splitlines()

# print(p1(input))
p2(input)
