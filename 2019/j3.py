# Cold Compress - 15/15

lines = [input() for _ in range(int(input()))]

for line in lines:
    encrypted = ""
    current = line[0]
    count = 0
    for char in line:
        if char == current:
            count += 1
        else:
            encrypted += f"{count} {current} "
            current = char
            count = 1

    encrypted += f"{count} {current}"

    print(encrypted)


