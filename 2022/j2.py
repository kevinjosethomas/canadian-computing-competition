# Fergusonball Ratings - 15/15

num = int(input())
players = [(int(input()) * 5) - (int(input()) * 3) for _ in range(num)]
count = len([player for player in players if player > 40])
print(str(count) + ("+" if count == num else ""))
