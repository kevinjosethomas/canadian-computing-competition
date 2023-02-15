# Good Groups

together = {}
for _ in range(int(input())):
    constraint = input().split()
    if constraint[0] in together:
        together[constraint[0]].append(constraint[1])
    else:
        together[constraint[0]] = [constraint[1]]

separate = {}
for _ in range(int(input())):
    constraint = input().split()
    if constraint[0] in separate:
        separate[constraint[0]].append(constraint[1])
    else:
        separate[constraint[0]] = [constraint[1]]

groups = [input().split() for _ in range(int(input()))]

violations = 0
for group in groups:
    for person in group:
        needs = [*together.get(person, [])]
        if needs:
            for n in needs:
                if n not in group:
                    together[person].remove(n)
                    violations += 1
                    continue

        avoid = [*separate.get(person, [])]
        if avoid:
            for a in avoid:
                if a in group:
                    separate[person].remove(a)
                    violations += 1
                    continue

print(violations)

# 2
# A B
# C D
# 2
# A D
# A E
# 2
# A D E
# C B F
