# Boiling Water - 15/15

temperature = int(input())
pressure = (5 * temperature) - 400

print(pressure)
if pressure == 100:
    print(0)
elif pressure > 100:
    print(-1)
else:
    print(1)
