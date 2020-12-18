import string


def solution(exprs):

    def evaluate(expr):
        nums, ops = [], []

        i = 0
        while i < len(expr):
            if expr[i] == ' ':
                i += 1
                continue

            if expr[i] in string.digits:
                nums.append(expr[i])
                i += 1
                continue

            if expr[i] in ('+', '*'):
                while len(ops) and ops[-1] != '(':
                    nums.append(ops.pop())
                ops.append(expr[i])
                i += 1
                continue

            if expr[i] == '(':
                ops.append(expr[i])
                i += 1
                continue

            if expr[i] == ')':
                while ops[-1] != '(':
                    nums.append(ops.pop())
                ops.pop()
                i += 1
                continue

        while ops:
            nums.append(ops.pop())

        stack = []
        for t in nums:
            if t in string.digits:
                stack.append(int(t))

            if t == '*':
                stack.append(stack.pop() * stack.pop())

            if t == '+':
                stack.append(stack.pop() + stack.pop())

        return stack[0]

    sum = 0
    for expr in exprs:
        sum += evaluate(expr)
    return sum


def parse(input):
    return input.splitlines()


def main():
    input = open("input", "r").read()
    print solution(parse(input))


main()
