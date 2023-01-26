# Art - 15/15

num_of_drops = int(input())
drops = [tuple(map(int, input().split(","))) for _ in range(num_of_drops)]
x_values = [drop[0] for drop in drops]
y_values = [drop[1] for drop in drops]

print(f"{min(x_values) - 1},{min(y_values) - 1}")
print(f"{max(x_values) + 1},{max(y_values) + 1}")
