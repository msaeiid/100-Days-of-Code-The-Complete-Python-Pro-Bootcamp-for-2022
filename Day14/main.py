from pprint import isreadable
from tabnanny import check
from game_data import data
from art import logo, vs
import random
import os


def get_a_random_person(check_with: dict):
    """Generate a random account from the game data and checks second account A if different of the account B

    Args:
        check_with (dict): to check if two person are not same

    Returns:
        dict: person
    """
    is_correct = random.choice(data)
    if check_with == is_correct:
        while check_with == is_correct:
            is_correct = random.choice(data)
    return is_correct


def format_data(person: dict):
    """Format the account data into printable format.

    Args:
        person (dict): person who want to display
    Returns:
        str: data which should be displayed
    """
    return f"{person['name']}, a {person['description']} from {person['country']}."


def check_answer(A_person: dict, B_person: dict, guess: str):
    """Take the user guess follower counts and returns if they got it right.

    Args:
        A_person (dict): first person data
        B_person (dict): second person data 
        guess (str): user guess

    Returns:
        Bool,Int: If the answer is correct returns True else False
    """
    if (A_person['follower_count'] > B_person['follower_count']):
        return guess == 'a'
    else:
        return guess == 'b'


def play():
    """Play the game
    """
    #print logo
    print(logo)
    SCORE = 0
    game_should_countinue = True
    # choose first person
    account_a = get_a_random_person(None)
    # choose second randomly
    account_b = get_a_random_person(account_a)
    while game_should_countinue:
        #introduce first person
        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        #introduce second person
        print(f"Compare B: {format_data(account_b)}.")
        guess = input("Who has more follower? Type 'A' or  'B': ").lower()

        is_correct = check_answer(account_a, account_b, guess)
        #Clear the screen between rounds
        os.system('cls')
        print(logo)
        if is_correct:

            account_a = account_b
            account_b = get_a_random_person(account_a)
            SCORE += 1
            print(f"You're right! Current SCORE: {SCORE}")
        else:
            print(f"Sorry, that's wrong. Final score: {SCORE}")
            game_should_countinue = False


play()
