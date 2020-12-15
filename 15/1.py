def solution(nums):
    d = {}
    for i, num in enumerate(nums):
        d[num] = (i, i)

    curr, i = nums[-1], len(nums)
    while True:
        if curr not in d:
            val = 0
        else:
            val = d[curr][1] - d[curr][0]

        if val not in d:
            d[val] = (i, i)
        else:
            d[val] = (d[val][1], i)

        curr = val

        if i == 2019:
            return val

        i += 1


def parse(input):
    return map(int, input.split(','))


def main():
    input = open("input", "r").read()
    print solution(parse(input))


main()
