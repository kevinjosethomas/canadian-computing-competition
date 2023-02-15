# Sum Game - 15/15

num = int(input())
swifts = list(map(int, input().split()))
semaphores = list(map(int, input().split()))

k = 0
scores = [0, 0]
for i in range(1, num + 1):
    scores[0] += swifts[i - 1]
    scores[1] += semaphores[i - 1]

    if scores[0] == scores[1]:
        k = i

print(k)
