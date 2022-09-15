import random
from turtle import pos
word_list = ["ardvark", "baboon", "camel"]
random_word = random.choice(word_list)

guess_word = ['_' for i in random_word]
user_win = False
while not user_win:
    user_guess = input("Guess a letter: ").lower()
    for position in range(0, len(random_word)):
        if user_guess == random_word[position]:
            guess_word[position] = user_guess
    print(*guess_word)
    if not '_' in guess_word:
        user_win = True
        print("You win!")
