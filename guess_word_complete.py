# import random library
import random

# import string module
import string

# import words file
from words import words

# validate words
def get_valid_word(words):
  # randomly choose a word from the list
  word = random.choice(words)
  
  # check if a word contains a hypen or space
  while '-' in word or ' ' in word:  
    word = random.choice(words)

  return word.upper()

# hangman function
def hangman():
  # computer chooses a word
  word = get_valid_word(words)

  # store the correct user guesses
  word_letters = set(words)

  # set of all letters the user can guess
  alphabet = set(string.ascii_uppercase)
  
  # store all user guesses
  used_letters = set()

  # number of lives
  lives = 6

  # while the length of the word is greater than 0 and the number of lives is greater than 0
  while len(word_letters) > 0 and lives > 0:
    
    # print letters used
    #" ".join(["a", "b", "cd"]) -> 'a b cd'
    print("You have", lives, "lives left and you have used these letters:"," ".join(used_letters))

    # print the current word
    word_list = [letter if letter in used_letters else '-' for letter in word]
    print("Current word:", " ".join(word_list))

    # get user input
    user_letter = input("Guess a letter: ").upper()

    # if the letter hasn't been used before
    if user_letter in alphabet - used_letters:
      # add the letter to the used-letters category
      used_letters.add(user_letter)
      
      # if the letter is in the word
      if user_letter in word_letters:
        # remove the letter from the word
        word_letters.remove(user_letter)

      # subtract one life if the letter is wrong
      else:
        lives = lives - 1
        print("Letter is not in word.")
    
    # if the user guesses the same letter
    elif user_letter in used_letters:
      print("You have already used that character. Please try again.")

    # if the user inputs a character that is not a letter
    else:
      print("Invalid character. Please try again.")

  # if there are no more lives left
  if lives == 0:
    print("You died, sorry.  The word was", word)
  else:
    print("You guessed the word", word, "!!")
    
# call the hangman function
hangman()
