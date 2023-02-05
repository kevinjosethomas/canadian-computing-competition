# Silent Auction - 15/15

count = int(input())
bids = [[input(), int(input())] for _ in range(count)]

highest_bid = None

for bid in bids:
    if highest_bid is None:
        highest_bid = bid
    elif bid[1] > highest_bid[1]:
        highest_bid = bid

print(highest_bid[0])
