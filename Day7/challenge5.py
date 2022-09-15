import random
from hangman_art import stages, logo
from hangman_words import words

random_word = random.choice(words)

guess_word = ['_' for i in random_word]
finish_the_game = False
lives = 6
print(*logo)
while not finish_the_game and lives > 0:
    user_guess = input("Guess a letter: ").lower()
    word_found = False
    if user_guess in guess_word:
      print(f"You have already gussed {user_guess} !")
      print(*guess_word)
    else:
      for position in range(0, len(random_word)):
          if user_guess == random_word[position]:
              guess_word[position] = user_guess
              word_found = True
      print(*guess_word)
      if not word_found:
          lives -= 1
          print(
              f"You guessed {user_guess}, that's not in the word. you lose a life.")
          print(stages[6-lives])
      if lives == 0:
          finish_the_game = True
          print("You Lose!")
      if not '_' in guess_word:
          finish_the_game = True
          print("You win!")
