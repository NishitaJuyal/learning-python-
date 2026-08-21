#You need to enter the bidders who are bidding with the biding amount and the program will tell you who is the winner with the highest bid.
logo ='''
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

def bid_function(biding_data):
    highest_bid = 0
    winner = ""
    for biders in biding_data:

        biding_amount=biding_data[biders]
        if highest_bid < biding_amount:
            highest_bid = biding_amount
            winner = biders
    print("\n"*30)
    print(f"\nThe winner is {winner} with an amount of ${highest_bid}")

bids_dictionary={}
restart = True
while restart:
    name = input("What is your name?")
    bid = int(input("What is your bid? $"))
    bids_dictionary[name] = bid
    choice = input("Are there any other bidder? (y/n)").lower()

    if choice == "n":
        restart = False
        print("Thank you for your time!!!")
        bid_function(bids_dictionary)
    elif choice == "y":
        print("\n"*30)
        




