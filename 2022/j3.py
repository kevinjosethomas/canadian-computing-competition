# Harp Tuning - 15/15

instruction = input()
instructions = []

ins = ""
reached_turns = False
for char in instruction:

    if reached_turns:
        if 65 <= ord(char) <= 90:
            instructions.append(ins)
            ins = char
            reached_turns = False
            continue

    if char == "+" or char == "-":
        reached_turns = True

    ins += char

instructions.append(ins)
ins = char
reached_turns = False

for i in instructions:
    direction = True if "+" in i else False
    turns = i.split("+" if direction else "-")
    print(turns[0] + (" tighten " if direction else " loosen ") + turns[1])
