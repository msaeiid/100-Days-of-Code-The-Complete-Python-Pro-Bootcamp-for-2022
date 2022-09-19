from art import logo
from replit import clear

print(logo)
print("Welcome to the secret auction program.")
end = 'yes'
bidders = []


def add_bidder(name: str, bid: int):
    bidders.append(
        {
            "name": name,
            "bid": bid
        }
    )


def find_highest_bid(bidders: list):
    max_bid = {
        'name': 'unknwon',
        'bid': 0}
    for bidder in bidders:
        if int(bidder['bid']) > int(max_bid['bid']):
            max_bid['bid'] = bidder['bid']
            max_bid['name'] = bidder['name']
    return max_bid


while end == 'yes':
    name = input("What is your name? ")
    bid = input("What's your bid?: $")
    add_bidder(name, bid)
    end = input("Are there any other bidders? Type 'yes' or 'no.")
    clear()

highest_bid = find_highest_bid(bidders)
print(
    f"The winner is {highest_bid['name']} with a bid of ${highest_bid['bid']}")
