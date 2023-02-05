# Flipper - 15/15

instructions = input()
horizontals = instructions.count('H')
verticals = instructions.count('V')
grid = [[1, 2], [3, 4]]

if horizontals % 2 == 1:
    grid = [grid[1], grid[0]]

if verticals % 2 == 1:
    grid = [[grid[0][1], grid[0][0]], [grid[1][1], grid[1][0]]]

print(grid[0][0], grid[0][1])
print(grid[1][0], grid[1][1])

