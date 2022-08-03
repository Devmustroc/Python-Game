# /usr/bin/env python3

# Linux User & Developer presents: rock, paper.
import random
import time

# The initial rules of the game are created
# here. The three variables we’re using and
# their relationship is defi ned. We also provide a
# variable so we can keep score of the games.

rock = 1
paper = 2
scissors = 3

name = {rock: "Rock", paper: "Paper", scissors: "Scissors"}
rules = {rock: scissors, paper: rock, scissors: paper}

player_score = 0
computer_score = 0

# We begin the game code by defi ning the
# start of each round. The end of each play
# session comes back through here, whether we
# want to play again or not


def start():
    print("Let's play a game of Rock, Paper , Scissors.")
    while game():
        pass
    scores()


def game():
    player = move()
    computer = random.randint(1, 3)
    result(player, computer)
    return play_again()
# Player input is done here. We give the
# player information on how to play this
# particular version of the game and then allow
# their choice to be used in the next step. We also
# have something in place in case they enter an
# invalid option


def move():
    while True:
        print
        player = input("Rock = 1\nPaper = 2\nScissors = 3\nMake a move: ")
        try:
            player = int(player)
            if player in (1, 2, 3):
                return player
        except ValueError:
            pass
        print("Oops! I didn't understand that. Please enter 1, 2, 3")


# There are a few things going on when we
# show the results. First, we’re putting in a
# delay to add some tension, appending a variable
# to some printed text, and then comparing what
# the player and computer did. Through an if
# statement, we choose what outcome to print,
# and how to update the scores

def result(player, computer):
    print("1....")
    time.sleep(1)
    print("2...")
    time.sleep(2)
    print("3!")
    time.sleep(0.5)
    print("Computer threw {0}".format(name[computer]))
    global player_score, computer_score
    if player == computer:
        print("Tie game.")
    else:
        if rules[player] == computer:
            print("Your victory has been assured")
            player_score += 1
        else:
            print("The computer laughs as you realise you have been defeated")
            computer_score += 1

# We now ask for text input on whether
# or not someone wants to play again.
# Depending on their response, we go back to the
# start, or end the game and display the results


def play_again():
    answer = input("Would you like to play again? y/n: ")
    if answer in ("y", "y", "yes", "yes", "of course"):
        return answer
    else:
        print("thank you very mush for playing ours game. see you next time!")


def scores():
    global player_score, computer_score
    print("HIGH SCORES")
    print("Player: ", player_score)
    print("Computer: ", computer_score)


if __name__ == '__main__':
    start()
