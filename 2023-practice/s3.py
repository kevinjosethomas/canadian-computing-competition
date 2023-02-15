# Absolutely Acidic - 15/15

num = int(input())
readings = tuple(int(input()) for _ in range(num))
reading_frequency = {}
frequency_reading = {}

for reading in readings:
    if reading in reading_frequency:
        reading_frequency[reading] += 1
    else:
        reading_frequency[reading] = 1

for reading, frequency in reading_frequency.items():
    if frequency in frequency_reading:
        frequency_reading[frequency].append(reading)
    else:
        frequency_reading[frequency] = [reading]

frequencies = sorted(frequency_reading.keys(), reverse=True)

top_readings = frequency_reading[frequencies[0]]

if len(top_readings) > 1:
    difference = max(top_readings) - min(top_readings)
    print(difference)
else:
    second_readings = frequency_reading[frequencies[1]]
    differences = sorted([abs(top_readings[0] - reading) for reading in second_readings], reverse=True)
    print(differences[0])
