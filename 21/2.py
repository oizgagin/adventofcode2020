def solution(foods):
    m = {}
    for food in foods:
        for allergen in food['allergens']:
            if allergen in m:
                m[allergen] = m[allergen].intersection(food['ingridients'])
            else:
                m[allergen] = food['ingridients']

    not_allergens = set()
    for food in foods:
        for ingridient in food['ingridients']:
            if all(ingridient not in m[allergen] for allergen in m.keys()):
                not_allergens.add(ingridient)

    for allergen in m.keys():
        for not_allergen in not_allergens:
            if not_allergen in m[allergen]:
                m[allergen].remove(not_allergen)

    determined = {}

    while True:
        candidate = None
        for allergen, candidates in m.iteritems():
            if len(candidates) == 1 and list(candidates)[0] not in determined:
                candidate = list(candidates)[0]
                determined[allergen] = candidate

        if candidate is None:
            break

        for allergen in m.keys():
            if candidate in m[allergen]:
                m[allergen].remove(candidate)

    return ','.join(map(lambda t: t[1], sorted(determined.items(), key=lambda t: t[0])))


def parse(input):
    foods = []
    for line in input.splitlines():
        ingridients, allergens = line.split("(contains")[0].split(), map(str.strip, line.split("(contains")[1].strip(")").split(","))
        foods.append({'ingridients': set(ingridients), 'allergens': allergens})
    return foods


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
