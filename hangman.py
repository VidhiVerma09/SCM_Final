import random

# Different sets of Hangman pictures based on difficulty levels
HANGMAN_PICS_EASY = ['''
    +---+
        |
        |
        |                          
        |
        |
        |
        ===''', '''
    +---+
    |   |
        |
        |
        |
        |
       ===''', '''
    +---+
    |   |
    O   |
        |
        |
        |
       ===''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
       ===''', '''
    +---+
    |   |
    O   |
    |\  |                          
        |
        |
        |
        ===''', '''
    +---+
    |   |
    O   |
   /|\  |                          
        |
        |
        |
        ===''', '''
    +---+
    |   |
    O   |
   /|\  |                          
   / \  |
        |
        |
        ===''', '''
    +---+
    |   |
    O   |
   /|\  |                          
   /_\  |
        |
        |
        ===''', '''
    +---+
    |   |
    O   |
   /|\  |                          
   /_\  |
   | |  |
        |
        ===''',]

HANGMAN_PICS_MEDIUM = ['''
    +---+
        |
        |
        |
        |
        ===''', '''
    +---+
    O   |
        |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===''']

HANGMAN_PICS_HARD = ['''
    +---+
        |
        |
        |
        |
        ===''', '''
    +---+
    O   |
        |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===''',]

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

def getRandomWord(wordList):
    """
    Returns a random string from the passed list of strings.
    """
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    """
    Display the current state of the game.
    """
    print(HANGMAN_PICS_EASY[len(missedLetters)])
    print()

    print("Missed letters:", end=" ")
    for letter in missedLetters:
        print(letter, end=" ")
    print()

    # Display the secret word with blanks and correct guesses filled in
    for letter in secretWord:
        if letter in correctLetters:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()

def getGuess(alreadyGuessed):
    """
    Get the letter guessed by the player.
    """
    while True:
        print("Please guess a letter:", end=" ")
        guess = input().lower()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif guess in alreadyGuessed:
            print("You have already guessed that letter.")
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("Please enter a letter from the alphabet.")
        else:
            return guess

def playAgain():
    """
    Ask the player if they want to play again.
    """
    print("Do you want to play again? (yes or no)")
    return input().lower().startswith('y')

def getDifficulty():
    while True:
        print("Choose the difficulty level:")
        print("1. Easy (8 missed guesses)")
        print("2. Medium (6 missed guesses)")
        print("3. Hard (4 missed guesses)")
        choice = input("Enter the number corresponding to your choice: ")
        if choice in ['1', '2', '3']:
            if choice == '1':
                return HANGMAN_PICS_EASY, 8
            elif choice == '2':
                return HANGMAN_PICS_MEDIUM, 6
            elif choice == '3':
                return HANGMAN_PICS_HARD, 4
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

print('|_H_A_N_G_M_A_N_|')
while True:
    missedLetters = ''
    correctLetters = ''
    secretWord = getRandomWord(words)
    gameIsDone = False
    hangmanPics, maxMissedGuesses = getDifficulty()

    # Now for the game itself:
    while True:
        displayBoard(missedLetters, correctLetters, secretWord)
        # Let the player enter a letter:
        guess = getGuess(missedLetters + correctLetters)

        if guess in secretWord:
            correctLetters = correct
