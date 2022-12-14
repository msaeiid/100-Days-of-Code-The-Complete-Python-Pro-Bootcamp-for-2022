#some extra information
# use global if you want to change variable in method like below example
# enemies = 1


# def change_number_of_enemies():
#     global enemies
#     enemies += 1
#     print(enemies)


# change_number_of_enemies()
# print(enemies)

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def get_a_random_numer(start_number: int, end_number: int):
    import random
    return random.randint(start_number, end_number)


def game_difficulty():
    level = input("Choose a dificulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    elif level == 'hard':
        return HARD_LEVEL_TURNS


def check_answer(guess: str, random_number: int, turn: int):
    """checks answer against quess. Return True if the game is over or False if not"""
    if guess == random_number:
        print(f"You got it! The number was {random_number}")
        # below code is also but it makes lots of bugs
        # global turn
        # turn-=1
        return True, turn-1
    elif guess > random_number:
        # below code is also but it makes lots of bugs
        # global turn
        # turn-=1
        print("Too high\nGuess again!")
        return False, turn-1
    elif guess < random_number:
        # below code is also but it makes lots of bugs
        # global turn
        # turn-=1
        print("Too low\nGuess again!")
        return False, turn-1


turn = 0


def play_game():
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    # naming convension: capital letter for constant
    turn = game_difficulty()
    random_number = get_a_random_numer(1, 100)
    is_game_over = False
    while turn > 0 and not is_game_over:
        print(f"You have {turn} turns remaining to guess the number.")
        guess = int(input("Make a guess: "))
        is_game_over, turn = check_answer(guess, random_number, turn)


play_game()
