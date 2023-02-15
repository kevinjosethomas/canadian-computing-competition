# Deliv-e-droid

delivered = int(input())
collisions = int(input())
score = (delivered * 50) - (collisions * 10) + (500 if delivered > collisions else 0)
print(score)
