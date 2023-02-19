# CCC Word Hunt

word = input()
# word2 = word[::-1]
rows = int(input())
columns = int(input())
grid = tuple(tuple(input().split()) for _ in range(rows))

count = 0

# for row in grid:
#     count += row.count(word)  # count horizontal
#     count += row.count(word2)  # count horizontal

# for x in range(columns):
#     vertical = "".join([row[x] for row in grid])
#     count += vertical.count(word)
#     count += vertical.count(word2)


def dir_values(x, y, direction):
    try:
        if direction == "N":
            return grid[y - 1][x], x, y - 1
        elif direction == "NE":
            return grid[y - 1][x + 1], x + 1, y - 1
        elif direction == "E":
            return grid[y][x + 1], x + 1, y
        elif direction == "SE":
            return grid[y + 1][x + 1], x + 1, y + 1
        elif direction == "S":
            return grid[y + 1][x], x, y + 1
        elif direction == "SW":
            return grid[y + 1][x - 1], x - 1, y + 1
        elif direction == "W":
            return grid[y][x - 1], x - 1, y
        elif direction == "NW":
            return grid[y - 1][x - 1], x - 1, y - 1
    except IndexError:
        pass

    return False


def find_path(x, y, index, swapped, previous, yea):

    if index == len(word):
        print(yea)
        print(previous)
        print(x, y)
        print("\n")
        return True

    if grid[y][x] != word[index]:
        return False

    if previous:
        directions = (
            list(set([previous, "N", "E", "W", "S"])) if len(previous) == 1 else list(set([previous, "NW", "NE", "SW", "SE"]))
        )
    else:
        directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]

    if swapped:
        directions = [previous]

    if y == 0:
        directions = [d for d in directions if "N" not in d]

    if y == rows - 1:
        directions = [d for d in directions if "S" not in d]

    if x == 0:
        directions = [d for d in directions if "W" not in d]

    if x == columns - 1:
        directions = [d for d in directions if "E" not in d]

    for direction in directions:
        value = dir_values(x, y, direction)
        if find_path(
            value[1],
            value[2],
            index + 1,
            True if direction != previous and previous is not None else False,
            previous if previous else direction,
            yea + grid[y][x],
        ):
            return True


for y, row in enumerate(grid):
    for x, letter in enumerate(row):
        count += 1 if find_path(x, y, 0, False, None, "") else 0


print(count)

"""
AB
3
3
C B D
A C B
D B A
"""
