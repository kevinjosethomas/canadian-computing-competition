# Escape Room - 13/15
# optimized from 11/15 to 13/15 via https://github.com/qiz-li/ccc-solutions/blob/main/2020/j5.py

import sys

maze = []
products = {}
height, width = int(sys.stdin.readline()), int(sys.stdin.readline())

for y in range(height):
    row = []
    x = 0
    for col in map(int, sys.stdin.readline().split()):
        row.append(col)
        product = (x+1) * (y+1)
        if product in products:
            products[product].append((x, y))
        else:
            products[product] = [(x, y)]
        x += 1

    maze.append(row)

visited = set()
queue = [(0, 0)]

while queue:
    cell = queue.pop(0)
    value = maze[cell[1]][cell[0]]

    for product in products.get(value, []):
        if product == (width-1, height-1):
            print("yes")
            break
        if product not in visited:
            visited.add(product)
            queue.append(product)
    else:
        continue
    break
else:
    print("no")