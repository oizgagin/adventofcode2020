def loop_size(pub, subject):
    c = 0
    val = 1
    while True:
        c += 1
        val = (val * subject) % 20201227
        if val == pub:
            return c


def loop(subject, size):
    val = 1
    for _ in xrange(0, size):
        val = (val * subject) % 20201227
    return val


def solution(pub1, pub2):
    size1, size2 = loop_size(pub1, 7), loop_size(pub2, 7)
    return loop(pub1, size2)


def parse(input):
    return map(int, input.splitlines())


def main():
    input = open("input", "r").read()
    print(solution(*parse(input)))


main()
