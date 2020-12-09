from collections import defaultdict

def solution(nums):
    d = defaultdict(int)

    for i in xrange(0, 25):
        d[nums[i]] += 1

    for i in xrange(25, len(nums)):
        for k, v in d.iteritems():
            if v != 0:
                if nums[i] - k in d:
                    break
        else:
            return nums[i]

        d[nums[i-25]] -= 1
        d[nums[i]] += 1


def parse(input):
    return map(int, input.splitlines())


def main():
    input = open("input", "r").read()
    print solution(parse(input))


main()
