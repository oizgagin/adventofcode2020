def solution(passports):
    required = set([
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid',
        #'cid',
    ])

    valid = 0
    for passport in passports:
        if all(f in passport for f in required):
            valid += 1
    return valid


def parse(input):
    raws = map(lambda s: filter(None, s.split('\n')), filter(None, input.split('\n\n')))
    passports = []
    for raw in raws:
        passport = {}
        for part in raw:
            kvs = part.split()
            for kv in kvs:
                k, v = kv.split(':')
                passport[k] = v
        passports.append(passport)
    return passports


def main():
    input = open("input", "r").read()
    print solution(parse(input))


main()
