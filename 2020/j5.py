# Escape Room - 11/15

num_of_rows = int(input())
num_of_cols = int(input())
maze = tuple(tuple(map(int, input().split())) for _ in range(num_of_rows))
visited = []


def find_next_step(x, y):

    if x == num_of_cols - 1 and y == num_of_rows - 1:
        return True

    visited.append((x + 1, y + 1))

    value = maze[y][x]

    factors = []
    for i in range(1, value + 1):
        if i > num_of_cols or (value // i) > num_of_rows:
            continue
        if value % i == 0:
            factors.append((i, value // i))

    for factor in [factor for factor in factors if factor not in visited]:
        if find_next_step(factor[0] - 1, factor[1] - 1):
            return True

    return False


print("yes") if find_next_step(0, 0) else print("no")
