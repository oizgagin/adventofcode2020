def solution(graph):
    parents = set()

    visited = set()

    def recurse(color, path):
        if color == 'shiny gold':
            for p in path:
                parents.add(p)
            return

        visited.add(color)
        for nested in graph[color]:
            recurse(nested, path.union([color]))

    for color in graph:
        if color not in visited:
            recurse(color, set())

    return len(parents)


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
