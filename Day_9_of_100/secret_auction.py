from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
private_bid= {}
new_bids = False

def high_bid(self_bid):
  individual_bid = 0
  highest_bid = ""
  for each_bid in self_bid:
    client_bid= self_bid[each_bid]
    if client_bid > individual_bid:
      individual_bid = client_bid
      highest_bid = client_bid
  print(f"Winner of this auction is {highest_bid} with amount of ${individual_bid} ")

while not new_bids:
  name = input("Please enter your name ")
  amount = int(input("Please enter your bid "))
  private_bid[name] = amount
  make_bids = input("Are there more bidders 'Yes' or No ")
  if make_bids == 'No':
    new_bids = True
    high_bid(private_bid)
  elif make_bids == 'Yes':
    clear()
