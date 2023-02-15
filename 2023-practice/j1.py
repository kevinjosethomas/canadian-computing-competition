# What is n, Daddy? - 15/15

num = int(input())
combinations = set()
for i in range(min(num, 6)):
    if num - i > 5:
        continue
    combinations.add(tuple(sorted((num - i, i))))

print(len(combinations))
