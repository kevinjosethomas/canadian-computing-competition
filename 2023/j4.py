# Trianglane

num = int(input())
first = tuple(map(int, input().split()))
second = tuple(map(int, input().split()))
perimeter = 0

for i, x in enumerate(first):

    if x:  # triangle is painted

        # top & bottom
        if i % 2 != 0:  # downright
            perimeter += 1  # add top boundary
        else:  # upright
            if not second[i]:  # if bottom is not painted
                perimeter += 1  # add bottom boundary

        if i == 0:  # first one
            perimeter += 1
        else:
            if not first[i - 1]:  # left one is not painted
                perimeter += 1

        if i + 1 == num:
            perimeter += 1  # last one
            continue

        if not first[i + 1]:
            perimeter += 1

for i, x in enumerate(second):

    if x:
        if i % 2 != 0:  # upright
            perimeter += 1
        else:  # downright
            if not first[i]:
                perimeter += 1

        if i == 0:
            perimeter += 1  # add left of first
        else:
            if not second[i - 1]:  # left one is not painted
                perimeter += 1

        if i + 1 == num:
            perimeter += 1  # last one
            continue

        if not second[i + 1]:
            perimeter += 1  # add right

print(perimeter)
