# Telemarketer or not? - 15/15

number = "".join([input() for _ in range(4)])
print(
    "ignore"
    if (number[0] == "8" or number[0] == "9") and (number[1] == number[2]) and (number[-1] == "8" or number[-1] == "9")
    else "answer"
)
