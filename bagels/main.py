"""Bagels, by Mustapha Abourar Elmustapha.abourar@gmail.com
A deductive logic game where you must guess a number based on clues.
"""
import random

NUM_DIGITS = 3  # (!) Try setting this to 1 or 10.
MAX_GUESSES = 10  # (!) Try setting this to 1 or 100.


def main():
    print(f'''
    Bagels, a deductive logic game.
16. By Mustapha Abourar elmustapha.abourar@gmail.com
17.
18. I am thinking of a {NUM_DIGITS}-digit number with no repeated digits.
19. Try to guess what it is. Here are some clues:
20. When I say: That means:
21. Pico One digit is correct but in the wrong position.
22. Fermi One digit is correct and in the right position.
23. Bagels No digit is correct.
24.
25. For example, if the secret number was 248 and your guess was 843, the
26. clues would be Fermi Pico.
''')

    while True:  # main game loop.
        # This stores the secret number the player needs to guess:
        secretNum = getSecretNum()
        print('I have though up a number.')
        print(f'You have {MAX_GUESSES} guesses to get it')

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # Keep looping until thery enter the valid guess:
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f'Guess #{numGuesses}:')
                guess = input('>>> ')
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break  # They're correct, so break out of the loop.
            if numGuesses > MAX_GUESSES:
                print('you ran out of the guesses')
                print(f'The answer was {secretNum}')

        # Ask the player if he wants to playa again
        print('Do you want to play again ? (yes or no')
        if not input('>>>').islower().startswith('y'):
            break
    print('Thanks for playing')


"""
Returns a string made up of NUM_DIGITS unique random digits.
"""


def getSecretNum():
    numbers = list('0123456789')  # Creating list of digits from 0 to 9.
    random.shuffle(numbers)  # Shuffle them into random order.

    # Get the first NUM_DIGITS digits in the list for the secret number:
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


"""Returns a string with the pico, fermi, bagels clues for a guess
and secret number pair.
"""


def getClues(guess, secretNum):
    if guess == secretNum:
        return 'You got it!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # A correct digit is in the correct place.
            clues.append('Femi')
        elif guess[i] in secretNum:
            # A correct digit is in the incorrect place.
            clues.append('Pico')

    if len(clues) == 0:
        return 'Bagels'  # There are no correct digits at all.
    else:
        # Sort The clues into alphabetical order  so their original order
        # doesn't give information away.
        clues.sort()
        # Make a single string from the list of string clues
        return ' '.join(clues)


# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()
