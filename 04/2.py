import re

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

    def validate(p):
        return all([
            len(p['byr']) == 4 and p['byr'].isdigit() and 1920 <= int(p['byr']) <= 2002,
            len(p['iyr']) == 4 and p['iyr'].isdigit() and 2010 <= int(p['iyr']) <= 2020,
            len(p['eyr']) == 4 and p['eyr'].isdigit() and 2020 <= int(p['eyr']) <= 2030,
            re.match('^\d+(cm|in)$', p['hgt']) and (
                (p['hgt'].endswith('cm') and 150 <= int(p['hgt'][:-len('cm')]) <= 193) or
                (p['hgt'].endswith('in') and 59 <= int(p['hgt'][:-len('in')]) <= 76)
            ),
            p['hcl'].startswith('#') and len(p['hcl']) == 7 and all(ch in '0123456789abcdef' for ch in p['hcl'][1:]),
            p['ecl'] in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
            len(p['pid']) == 9 and p['pid'].isdigit(),
        ])

    valid = 0
    for passport in passports:
        if all(f in passport for f in required) and validate(passport):
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
