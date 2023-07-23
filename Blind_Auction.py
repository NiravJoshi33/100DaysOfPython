#Blind Auction

print("Welcome to the secret auction program")

cont = "yes"
data = {}
while cont == "yes":
    name = input("What is your name?")
    bid = int(input("How much is your bid?"))
    data[name] = bid #Associates the bid value with the name 
    cont = input("Do you want to add another bidding?")
    #print(data)

bid_count = 0
for bidder in data:
    #print(bids)
    if data[bidder] > bid_count:
        bid_count = data[bidder]

winner = list(data.keys())[list(data.values()).index(bid_count)]
print(f"{winner} has won the auction with {bid_count} rupees bidding")
#print(data)