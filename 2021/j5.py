# Modern Art - 15/15

height, width = int(input()), int(input())
num_of_instructions = int(input())
instructions = {}

for _ in range(num_of_instructions):
    instruction = input()

    if instruction in instructions:
        instructions[instruction] += 1
    else:
        instructions[instruction] = 1

gold = 0

for y in range(1, height + 1):
    for x in range(1, width + 1):
        gold += 0 if (instructions.get(f"R {y}", 0) + instructions.get(f"C {x}", 0)) % 2 == 0 else 1

print(gold)
