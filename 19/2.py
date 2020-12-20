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

        if len(res) == 1:
            return res[0]

        return "(" + '|'.join(res) + ")"

    r42 = traverse('42')
    r31 = traverse('31')

    r = re.compile('^(%s){2,}(%s){1,}$' % (r42, r31))

    valid = 0
    for message in messages:
        if not r.match(message):
            continue

        r42c = 0
        while re.match(r42, message):
            r42c += 1
            message = re.sub(r42, '', message, count=1)

        r31c = 0
        while re.match(r31, message):
            r31c += 1
            message = re.sub(r31, '', message, count=1)

        if r42c > r31c:
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
