import random
word_list = ["ardvark", "baboon", "camel"]
user_guess = input("Guess a letter: ")
random_word=random.choice(word_list)
for letter in random_word:
    if user_guess == letter:
        print("right")
    else:
        print("wrong")
