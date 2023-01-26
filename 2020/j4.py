# Cyclic Shifts - 15/15

text = input()
string = input()

for _ in range(len(string)):
    string = string[1:] + string[0]
    if string in text:
        print("yes")
        exit()

print("no")
