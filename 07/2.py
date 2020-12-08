def solution(graph):
    def recurse(color, d):
        if len(graph[color]) == 0:
            return 1

        sum = 0
        for nested, mul in graph[color].iteritems():
            r = recurse(nested, d+1)
            if r == 1:
                sum += mul
            else:
                sum += mul + mul * r

        return sum

    return recurse("shiny gold", 0)


def parse(input):
    graph = {}
    for line in input.splitlines():
        color = line.split(" bags ", 1)[0]
        graph[color] = {}

        if "no other bags" in line:
            continue

        for nested in line.split(" contain ")[1].split(","):
            sp = nested.split()
            spno, spcolor = int(sp[0]), sp[1] + " " + sp[2]

            graph[color][spcolor] = spno

    return graph


def main():
    input = open("input", "r").read()
    print solution(parse(input))


main()
