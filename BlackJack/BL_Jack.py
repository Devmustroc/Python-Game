"""The classic card game also known as 21. (This version doesn't have
splitting or insurance.)
More info at: https://en.wikipedia.org/wiki/Blackjack
Tags: large, game, card game"""

import sys

#Setup the constants:

HEARTS = chr(9829)  # Character 9829 is '♥'.
DIAMONDS = chr(9830)  # Character 9830 is '♦'.
SPADES = chr(9824) # Character 9824 is '♠'.
CLUB = chr(9827) # Character 9827 is '♣'.

# (A list of chr codes is at https://inventwithpython.com/charactermap)
BACKSIDE = 'backside'


def main():
    print('''Rules:
Try to get as close to 21 without going over.
Kings, Queens, and Jacks are worth 10 points.
Aces are worth 1 or 11 points.
Cards 2 through 10 are worth their face value.
(H)it to take another card.
(S)tand to stop taking cards.
On your first play, you can (D)ouble down to increase your bet
but must hit exactly one more time before standing.
In case of a tie, the bet is returned to the player.
The dealer stops hitting at 17.
''')
    money = 5000
    while True : # Main game loop.
        #Check if the player has run out of money:
        if money <= 0:
            print("You're  Broke!")
            print("Good thing you aren't playing with real money")
            print('Thank for playing!')
            sys.exit()
    # Let the player enter their bet for this round:
    print("money: ", money)
    bet = getBet(money)

    # Give the dealer and player two cards from the deck each:
    deck = getDeck()
    dealerHand = [deck.pop(), deck.pop()]
    playerHand = [deck.pop(), deck.pop()]

    # Handle player actions:
    print('Bet: ', bet)
    while True: # Keep looping until player stands or busts.
        displayHands(playerhand, dealerHand, False)
        print()

        # Check if the player has bust:
        if getHandValue(playerHand) > 21:
            break

        # Get the player's move, either H, S, or D:
        if move == 'D':
            # Player is doubling down, they can increase their bet:
            additionnalBet = getBet(min(bet, (money - bet)))
            bet += additionnalBet
            print(f'Bet increased to {bet}')
            print('Bet:', bet)

        if move in ('H', 'D'):
            # Hit/doubling down takes another card.
            newCard = deck.pop()
            rank, suit = newCard
            print(f'You drew a {rank} of {suit}')
            playerHand.append(newCard)

    # Handle the dealer's actions:
    if getHandValue(playerHand) <= 21:
        while getHandValue(dealerHand) < 17:
            #The dealer hits:
            print('Dealer hits...')
            dealerHand.append(deck.pop())
            displayHands(playerHand, dealerHand, False)

            if getHandValue(dealerHand) > 21:
                break  # the dealer has busted.
            input('press Enter to continue...')
            print("\n\n")

    # Show the final hands:
    displayhands(playHand, dealerHand, True)

    playerValue = getHandValue(playerHand)
    dealerValue = getHandValue(dealerHand)

    # Handlde whether the player won, lost, or tied:

    if dealerHand > 21:
        print(f"Dealer busts! You win ${bet}")
        money += bet
    elif (playerValue > 21) or (playerValue < dealerValue):
        print('You lost!')
        money -= bet
    elif playerValue > dealerValue:
        print(f'You won ${bet}')
        money += bet
    elif playerValue == dealerValue:
        print("it's a tie, the bet is returned to you")

    input("Press Enter to continue...")
    print("\n\n")

def getBet():
    """Ask the player how much they want to bet for this round."""



