import random

def choose_word():
    words = ['python', 'developer', 'hangman', 'programming', 'computer', 'software', 'keyboard']
    return random.choice(words)

def display_hangman(tries):
    stages = [
        '''
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        --------
        ''',
        '''
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        --------
        ''',
        '''
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        --------
        ''',
        '''
           -----
           |   |
           O   |
          /|   |
               |
               |
        --------
        ''',
        '''
           -----
           |   |
           O   |
           |   |
               |
               |
        --------
        ''',
        '''
           -----
           |   |
           O   |
               |
               |
               |
        --------
        ''',
        '''
           -----
           |   |
               |
               |
               |
               |
        --------
        '''
    ]
    return stages[tries]

def play_hangman():
    word = choose_word()
    word_letters = set(word)
    guessed_letters = set()
    incorrect_guesses = 0
    max_tries = 6

    print("Welcome to Hangman!")
    
    while len(word_letters) > 0 and incorrect_guesses < max_tries:
        print(display_hangman(incorrect_guesses))
        print(f"You have {max_tries - incorrect_guesses} tries left.")
        
        word_display = [letter if letter in guessed_letters else '_' for letter in word]
        print("Current word: ", ' '.join(word_display))

        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word_letters:
            guessed_letters.add(guess)
            word_letters.remove(guess)
        else:
            guessed_letters.add(guess)
            incorrect_guesses += 1
            print(f"Incorrect guess. You have {max_tries - incorrect_guesses} tries left.")

    print(display_hangman(incorrect_guesses))
    
    if incorrect_guesses == max_tries:
        print(f"Sorry, you lost! The word was '{word}'.")
    else:
        print(f"Congratulations! You guessed the word '{word}' correctly.")

play_hangman()
