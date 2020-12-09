from collections import defaultdict

def solution(nums):
    target = 50047984

    for i in xrange(0, len(nums)):
        sum = 0
        for j in xrange(i, len(nums)):
            sum += nums[j]
            if sum == target:
                return min(nums[i:j+1]) + max(nums[i:j+1])


def parse(input):
    return map(int, input.splitlines())


def main():
    input = open("input", "r").read()
    print solution(parse(input))


main()
