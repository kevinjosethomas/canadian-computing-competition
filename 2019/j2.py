# Time to Decompress - 15/15

lines = int(input())
for _ in range(lines):
    line = input().split()
    print(line[1] * int(line[0]))
