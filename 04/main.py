import re

INPUT_FILE = 'input'
TEST_INPUT = 'test_input'

BYR_RANGE = [1920, 2002]
IYR_RANGE = [2010, 2020]
EYR_RANGE = [2020, 2030]
HGT_CM = [150, 193]
HGT_IN = [59, 76]
HGT_MEASURE = ['cm', 'in']
EYE_COLOR = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

HCL_PATTERN = re.compile(r'#[0-9A-Fa-f]{6}\b')
PID_PATTERN = re.compile(r'[0-9]{9}\b')


def convert_dict(l):
    e1 = l.split()
    e2 = [x.split(":") for x in e1]
    # print(e2)
    d = {x[0]: x[1] for x in e2}
    # print(d)
    return(d)


def initial_check(d):
    if len(d) == 8:
        return True
    if len(d) == 7 and 'cid' not in d:
        return True
    return False


def validate_pass(d):
    # CHECK IF ENOUGH PARAMETERS EXIST
    if initial_check(d):
        # return True
        # GRAB PARAMETERS IN EASIER TO WRITE FORMAT
        byr = d['byr']
        iyr = d['iyr']
        eyr = d['eyr']
        hgt = d['hgt']
        hcl = d['hcl']
        ecl = d['ecl']
        pid = d['pid']
        # CHECK YEAR LENGTHS
        if len(byr) != 4 or len(iyr) != 4 or len(eyr) != 4:
            # print("WRONG YEAR LENGTH: ", byr, iyr, eyr)
            return False
        # CHECK YEAR RANGES
        # BIRTH YEAR
        if int(byr) < BYR_RANGE[0] or int(byr) > BYR_RANGE[1]:
            # print("Out of Range BYR: ", byr)
            return False
        # ISSUE YEAR
        if int(iyr) < IYR_RANGE[0] or int(iyr) > IYR_RANGE[1]:
            # print("Out of Range IYR: ", iyr)
            return False
        # EXPIRATION YEAR
        if int(eyr) < EYR_RANGE[0] or int(eyr) > EYR_RANGE[1]:
            # print("Out of Range EYR: ", eyr)
            return False
        # HEIGHT CHECK
        h = hgt[:-2]
        if h != '':
            h = int(h)
        m = hgt[-2:]
        # print(f"{h} in {m}")
        if m not in HGT_MEASURE:
            # print("Invalid Measurements:", hgt)
            return False
        if m == 'cm':
            if h < HGT_CM[0] or h > HGT_CM[1]:
                # print("Out of Range: ", hgt)
                return False
        elif m == 'in':
            if h < HGT_IN[0] or h > HGT_IN[1]:
                # print("Out of Range: ", hgt)
                return False
        # EYE COLOR CHECK
        if ecl not in EYE_COLOR:
            # print(ecl)
            return False
        # HAIR COLOR CHECK
        if HCL_PATTERN.match(hcl) == None:
            # print("HCL", hcl)
            return False
        # print("HCL", hcl)
        # ID CHECK
        if PID_PATTERN.match(pid) == None and len(str(pid)) != 9:
            # print("PID", pid)
            return False
        print("PID", pid)
        return True
    return False


def p1(f):
    with open(f) as file:
        s = file.read()
    l = s.split("\n\n")
    entries = [convert_dict(x) for x in l]
    # initial_entries = filter(initial_check, entries)
    valid_passes = filter(validate_pass, entries)
    # print([x['hgt'] for x in valid_entries])
    print(len(list(valid_passes)))


# p1(TEST_INPUT)
p1(INPUT_FILE)
