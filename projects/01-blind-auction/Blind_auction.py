import art

print(art.gravel)
print("Blind Auction")
bids = {}
while True:
    name = input("What is your name:\n")
    price = int(input("What ir your bid:\n"))
    bids[name] = price
    end = input('Are there any other bidders? Type "yes" or "no"\n')
    print("\n" * 100)
    if end.lower() == "no":
        break

highest_bid = 0
for name in bids:
    if bids[name] > highest_bid:
        winner = name
        highest_bid = bids[name]

print(f"The winner is {winner} with {highest_bid}€")

# Other method
# winner_max = max(bids) asi me da el key mayor alfabéticamente
winner_max = max(bids, key=bids.get)  # asi compara el value no el key
print(f"The winner is {winner_max} with {bids[winner_max]}€")
