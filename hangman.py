import random
from words_for_hangman import words
import string


def select_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = select_word(words)
    word_letters = set(word)
    alpha = set(string.ascii_uppercase)
    letters_picked = set()

    lives = 7


    while len(word_letters) > 0 and lives > 0:
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(letters_picked))

        # what current word is (ie W - R D)
        word_list = [letter if letter in letters_picked else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        guess = input('Guess a letter: ').upper()
        if guess in alpha - letters_picked:
            letters_picked.add(guess)
            if guess in word_letters:
                word_letters.remove(guess)
                print('')

            else:
                lives = lives - 1
                print('The letter,', guess, 'is not in this word.')

        elif guess in letters_picked:
            print('You have already used this letter. Try again.')

        else:
            print('Invalid input.')

    if lives == 0:
        print('OH NO! You died. The word was', word)
    else:
        print('You guessed the word!! It was ', word)

hangman()