# Choose your own path -

from itertools import chain

num_of_pages = int(input())

pages = []
endings = {}
for i in range(1, num_of_pages + 1):
    page = list(map(int, input().split()))
    if page[0] == 0:
        endings[i] = 0
    pages.append(page[1:])


def check_redundant_pages(pages):
    all_pages = set(chain(*pages))
    for i in range(2, num_of_pages + 1):
        new_pages = [*all_pages]
        for x in pages[i - 1]:
            new_pages.remove(x)
        if i not in new_pages:
            return "N"
    return "Y"


def find_path(page, count, visited):
    if page == 1:
        return count

    for i, p in enumerate(pages):
        if i + 1 in visited:
            continue
        if page in p:
            path = find_path(i + 1, count + 1, [*visited, i + 1])
            if path:
                return path


lowest_count = None
for ending in endings:
    count = find_path(ending, 1, [])
    if not lowest_count:
        lowest_count = [ending, count]
        continue
    if count < lowest_count[1]:
        lowest_count = [ending, count]

print(check_redundant_pages(pages))
print(lowest_count[1])
