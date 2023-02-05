# Winning Score - 15/15

apples = (int(input()) * 3) + (int(input()) * 2) + int(input())
bananas = (int(input()) * 3) + (int(input()) * 2) + int(input())

if apples > bananas:
    print("A")
elif bananas > apples:
    print("B")
else:
    print("T")
