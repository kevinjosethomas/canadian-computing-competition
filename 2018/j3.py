# Are we there yet? - 15/15

cities = [*map(int, input().split()), 0]

for i, city in enumerate(cities):
    distances = ""

    for j, city2 in enumerate(cities):
        if i == j:
            distances += "0 "
        elif i > j:
            distances += f"{sum(cities[j:i])} "
        else:
            distances += f"{sum(cities[i:j])} "

    print(distances)
