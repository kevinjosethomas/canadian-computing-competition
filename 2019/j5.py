# Rule of Three - 14/15

rules = [[*(input().split()), i] for i in range(1, 4)]
steps, initial, final = input().split()


def substitute(current, remaining, path):

    if remaining == 0:
        if current == final:
            return True, path
        return False, path

    for i in range(len(current)):
        for rule in rules:
            try:
                index = current.index(rule[0], i, i + len(rule[0]))
            except:
                continue

            new = current[:index] + rule[1] + current[index + len(rule[0]) :]
            output = substitute(new, remaining - 1, [*path, f"{rule[2]} {index+1} {new}"])

            if output[0]:
                return True, output[1]

    return False, path


success, path = substitute(initial, int(steps), [])
print("\n".join(path))
