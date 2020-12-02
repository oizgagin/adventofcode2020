def solution(lines):
    valid = 0

    for line in lines:
        rule = line.split(":")[0].strip()
        password = line.split(":")[1].strip()

        interval, letter = rule.split(" ")
        lo, hi = map(int, interval.split("-"))

        if lo <= password.count(letter) <= hi:
            valid += 1

    return valid


def main():
    lines = map(str.strip, open("input", "r").readlines())
    print solution(lines)


main()
