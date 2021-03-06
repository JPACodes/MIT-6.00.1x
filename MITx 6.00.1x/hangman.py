# Problem Set 2, hangman.py
# Name: Jeanpeter Polraanco
# Collaborators: Stackoverflow
# Time spent: 15hrs..4/24

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")

    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    secret_word = random.choice(wordlist)
    return secret_word

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()

secret_word_letters = []


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    guess = ""
    for char in secret_word:
        for c in letters_guessed:
            if char == c:
                guess += c
            else:
                continue

    return guess == secret_word


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed_word = [' _ ' for c in secret_word]

    for letter in letters_guessed:
        for count, char in enumerate(secret_word):
            if char == ' ':
                guessed_word[count] = ' '
            if letter == char:
                guessed_word[count] = letter
            else:
                continue
    guessed_word_str = ''.join(guessed_word)
    print(guessed_word_str)
    return guessed_word_str


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''

    english_letters = string.ascii_lowercase

    available_letters = []
    available_letters_copy = []

    for char in english_letters:
        available_letters.append(char)

    available_letters_copy.extend(available_letters)

    for c in available_letters_copy:
        for i in letters_guessed:
            if i == c:
                available_letters.remove(i)

    available_letters_str = ''.join(available_letters)

    print('Available letters:', available_letters_str)


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    good_guess = 0
    guesses_left = 6
    warnings_left = 3
    letters_guessed = ''
    vowels = 'aeio'
    guess = ''
    prohibited_letters = '!@#$%^&*()_+~{}|:"<>?'
    accepted_letters = string.ascii_lowercase

    while not is_word_guessed(secret_word, letters_guessed) and guesses_left > 0:
        textOK = False
        guess.lower()
        while not textOK and guesses_left != 0:
            rounds(guesses_left, warnings_left)
            get_available_letters(guess)
            guess = (input("Please guess a letter: ")).lower()
            if guess not in accepted_letters or guess in prohibited_letters:
                print('Try a valid character')
                if warnings_left == 0 and guesses_left != 0:
                    guesses_left -= 1
                elif guesses_left == 0 and warnings_left == 0:
                    print("Game Over!")
                else:
                    warnings_left -= 1
            elif guess in letters_guessed:
                if warnings_left != 0:
                    warnings_left -= 1
                    print("You already guessed this letter")
                else:
                    print("You already guessed this letter. You have no warnings left so you lose one guess.")
                    guesses_left -= 1
            else:
                if guess not in secret_word:
                    print("that letter is not in the word")
                    if guess in vowels and guess not in letters_guessed:
                        guesses_left -= 2
                    else:
                        guesses_left -= 1
                else:
                    print("Good guess!")
                    good_guess += 1
                textOK = True

        letters_guessed += guess
        get_guessed_word(secret_word, letters_guessed)

        if is_word_guessed(secret_word, letters_guessed):
            print("Congratulations, you won!")
            print("Your total score for this game is", (guesses_left * len(secret_word)))
        if guesses_left < 1:
            print("Sorry, you ran out of guesses. The word was:", secret_word)

def rounds(guesses_left, warnings_left):
    print('You have', guesses_left, 'guesses left', 'and', warnings_left, 'warnings left')


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass





def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


#if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
secret_word = choose_word(wordlist)
hangman(secret_word)

###############

# To test part 3 re-comment out the above lines and
# uncomment the following two lines.

# secret_word = choose_word(wordlist)
# hangman_with_hints(secret_word)


