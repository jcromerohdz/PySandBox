from ctypes import WinError


logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

bids = {}

def find_highest_bidder(bids):
  high_bid = 0
  winner = ""
  for name in bids:
    if bids[name] > high_bid:
      high_bid = bids[name]
      winner = name

  print(f"The winner is {winner} with a bid of ${high_bid}")


bidding_finished = False

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    bidding_finished = False