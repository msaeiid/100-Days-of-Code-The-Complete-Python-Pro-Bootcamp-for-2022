from cmath import log
import random
import os
from art import logo
cards = {'Two': 2,
         'Three': 3,
         'Four': 4,
         'Five': 5,
         'Six': 6,
         'Seven': 7,
         'Eight': 8,
         'Nine': 9,
         'Ten': 10,
         'Jack': 10,
         'Queen': 10,
         'King': 10,
         'Ace': 11,
         }
cards_list = list(cards.keys())


def get_random_cards(number_of_cards: int):
    """Returns random card or cards from the deck

    Args:
        number_of_cards (int): number of random cards which needed
    """
    random_cards = []
    for _ in range(number_of_cards):
        random_card = random.choice(cards_list)
        random_cards.append(random_card)
    return random_cards


def calculate_score(cards_list: list):
    """
        Take a list of cards and return the score calculated from the cards
    """
    score = 0
    for card in cards_list:
        score += cards[card]
    #check for blackjack
    if score == 21 and len(cards_list) == 2:
        return 0
    #check for ace if score is more than 21
    if 'ace' in cards_list and score > 21:
        score -= 10
    return score


def compare(user_score: int, computer_score: int):

    if user_score == computer_score:
        return " Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over, You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"


def play_game():
    is_game_over = False
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'n':
        is_game_over = True
    os.system('cls')
    print(logo)
    while not is_game_over:
        # start game with 2 card
        user_cards = get_random_cards(2)
        computer_cards = get_random_cards(2)
        #calculate user and computer score
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f'Your cards: {user_cards}, current score: {user_score}')
        print(
            f"Computer's first card: {computer_cards[0]}  {cards[computer_cards[0]]}")
        if user_score == 0 or computer_score == 0 or user_score > 21 or computer_score > 21:
            is_game_over = True
        else:
            another_card = input(
                "Type 'y' to get another card, type 'n' to pass: ")
            if another_card == 'y':
                user_cards += get_random_cards(1)
                user_score = calculate_score(user_cards)
                print(f'Your cards: {user_cards}, current score: {user_score}')
                print(
                    f"Computer's first card: {computer_cards[0]} => {cards[computer_cards[0]]}")
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards += get_random_cards(1)
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))
    play_game()


play_game()
