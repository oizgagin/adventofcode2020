def solution(ints):
    ints.sort()

    for i in xrange(0, len(ints)):
        for j in xrange(i+1, len(ints)):
            l, r = j+1, len(ints)
            while l < r:
                m = l + (r - l) / 2
                s = ints[i] + ints[j] + ints[m]

                if s == 2020:
                    return ints[i] * ints[j] * ints[m]

                if s < 2020:
                    l = m + 1
                else:
                    r = m


def main():
    ints = map(int, open("input", "r").readlines())
    print solution(ints)


main()
