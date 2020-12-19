import re


def solution(rules, messages):

    def traverse(id):
        res = []
        for rule in rules[id]:
            s = []
            for rule_id in rule:
                if rule_id in ('a', 'b'):
                    s.append(rule_id)
                else:
                    s.append(traverse(rule_id))
            res.append(''.join(s))

        return "(" + '|'.join(res) + ")"

    r = re.compile('^' + traverse('0') + '$')

    valid = 0
    for message in messages:
        if r.match(message):
            valid += 1
    return valid


def parse(input):
    raw_rules, raw_messages = input.split("\n\n")[0], input.split("\n\n")[1]

    rules = {}
    for raw_rule in raw_rules.splitlines():
        id, exprs = raw_rule.split(":")[0].strip(), raw_rule.split(":")[1]

        rule = []
        for expr in exprs.split("|"):
            rule.append(list(map(lambda s: s.strip(' "'), expr.split())))
        rules[id] = rule

    return rules, raw_messages.splitlines()


def main():
    input = open("input", "r").read()
    print(solution(*parse(input)))


main()
