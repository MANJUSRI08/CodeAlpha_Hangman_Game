import random
HANGMAN_PICS = [
    """
       ------
       |    |
            |
            |
            |
            |
    =========""",
    """
       ------
       |    |
       O    |
            |
            |
            |
    =========""",
    """
       ------
       |    |
       O    |
       |    |
            |
            |
    =========""",
    """
       ------
       |    |
       O    |
      /|    |
            |
            |
    =========""",
    """
       ------
       |    |
       O    |
      /|\\   |
            |
            |
    =========""",
    """
       ------
       |    |
       O    |
      /|\\   |
      /     |
            |
    =========""",
    """
       ------
       |    |
       O    |
      /|\\   |
      / \\   |
            |
    ========="""
]

def choose_word():
    words = ['python', 'hangman', 'challenge', 'programming', 'developer']
    return random.choice(words)

def display_word(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

def play_hangman():
    word = choose_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = len(HANGMAN_PICS) - 1
    
    print("Welcome to Hangman! Try to guess the word.")
    
    while incorrect_guesses < max_incorrect_guesses:
        print(HANGMAN_PICS[incorrect_guesses])
        print(f"Word: {display_word(word, guessed_letters)}")
        print(f"Guessed Letters: {sorted(guessed_letters)}")
        print(f"Incorrect Guesses Left: {max_incorrect_guesses - incorrect_guesses}")
        
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
        elif guess in word:
            guessed_letters.add(guess)
            print("Good guess!")
        else:
            guessed_letters.add(guess)
            incorrect_guesses += 1
            print("Incorrect guess.")
        
        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You've guessed the word: {word}")
            break
    else:
        print(HANGMAN_PICS[incorrect_guesses])
        print(f"Sorry, you've run out of guesses. The word was: {word}")

if __name__ == "__main__":
    play_hangman()
