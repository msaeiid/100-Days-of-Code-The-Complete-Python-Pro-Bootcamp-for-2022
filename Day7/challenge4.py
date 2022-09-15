import random
from turtle import pos
word_list = ["ardvark", "baboon", "camel"]

stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
random_word = random.choice(word_list)

guess_word = ['_' for i in random_word]
finish_the_game = False
lives = 6
while not finish_the_game and lives > 0:
    user_guess = input("Guess a letter: ").lower()
    word_found = False
    for position in range(0, len(random_word)):
        if user_guess == random_word[position]:
            guess_word[position] = user_guess
            word_found = True
    print(*guess_word)
    if not word_found:
        lives -= 1
        print(stages[6-lives])
    if lives == 0:
        finish_the_game = True
        print("You Lose!")
    if not '_' in guess_word:
        finish_the_game = True
        print("You win!")
