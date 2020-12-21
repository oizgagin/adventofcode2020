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

    res = 0
    for not_allergen in not_allergens:
        for food in foods:
            if not_allergen in food['ingridients']:
                res += 1

    return res


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
