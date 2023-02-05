# Secret Instructions - 15/15

previous_dir = None

while True:
    instruction = input()
    if instruction == "99999":
        break

    added = int(instruction[0]) + int(instruction[1])
    if added == 0:
        print(previous_dir, instruction[2:])
    elif added % 2 == 0:
        previous_dir = "right"
        print("right", instruction[2:])
    else:
        previous_dir = "left"
        print("left", instruction[2:])
