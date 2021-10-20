import os
from art import logo
#HINT: You can call clear() to clear the output in the console.

def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

clear = lambda: os.system('cls')

bidders = {}
should_continue = True
max = 0
while should_continue:
  print (logo)
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))
  bidders[name] = bid

  ans = input("Are there another person that wants to bid? yes or no: ").lower()
  if ans == "no":
    should_continue = False
    find_highest_bidder(bidders)

  elif ans == "yes":
    clear()
  else:
    print("Wrong input")
