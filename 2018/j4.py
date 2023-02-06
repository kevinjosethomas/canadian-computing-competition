# Sunflowers - 15/15

num_of_flowers = int(input())
flowers = [list(map(int, input().split())) for _ in range(num_of_flowers)]


def check_ascending(array):
    previous = None
    for x in array:
        if not previous:
            previous = x
            continue
        if x <= previous:
            return False
        previous = x
    return True


def rotate(flowers):
    rotated = []
    for i in range(num_of_flowers):
        rotated.append([x[i] for x in reversed(flowers)])

    for i, row in enumerate(rotated):
        if not check_ascending(row):
            return rotate(rotated)
        if not check_ascending([x[i] for x in rotated]):
            return rotate(rotated)

    return rotated


rotated = rotate(flowers)
for row in rotated:
    print(" ".join(map(str, row)))
