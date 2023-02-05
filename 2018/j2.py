# Occupy parking - 15/15

input()
old = input()
new = input()
count = 0
for i, p in enumerate(old):
    if p == "C" and new[i] == "C":
        count += 1

print(count)
