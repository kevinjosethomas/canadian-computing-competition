# Special Event

num = int(input())
availability = [0, 0, 0, 0, 0]

for _ in range(num):
    person = input()
    for i, a in enumerate(person):
        if a == "Y":
            availability[i] += 1

most = max(availability)
days = []
for i, day in enumerate(availability):
    if day == most:
        days.append(i + 1)

print(",".join(map(str, sorted(days))))
