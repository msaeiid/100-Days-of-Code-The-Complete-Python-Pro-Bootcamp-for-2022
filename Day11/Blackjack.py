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
    for i in range(number_of_cards):
        random_card = random.choice(cards_list)
        random_cards.append(random_card)
    return random_cards


def calculate_score(cards_list: list):
    score = 0
    for card in cards_list:
        score += cards[card]
    return score


def check_winner(user_cards: list, computer_cards: list):

    user_score = 0
    number_of_ace_in_userhand = 0
    for card in user_cards:
        user_score += cards[card]
        if card == 'Ace':
            number_of_ace_in_userhand += 1

    computer_score = 0
    number_of_ace_in_computerhand = 0
    for card in computer_cards:
        computer_score += cards[card]
        if card == 'Ace':
            number_of_ace_in_computerhand += 1

    while user_score > 21 and number_of_ace_in_userhand > 0:
        user_score -= 10
        number_of_ace_in_userhand -= 1
    while computer_score > 21 and number_of_ace_in_userhand > 0:
        computer_score -= 10
        number_of_ace_in_computerhand -= 1

    print(f'Your final hand: {user_cards}, final score: {user_score}')
    print(
        f"Computer's final hand: {computer_cards} final score: {computer_score}")

    lose_message = 'lose'
    win_message = 'win'
    draw_message = 'Draw'

    if (user_score > 21 and computer_score > 21) or user_score == computer_score:
        return draw_message
    elif user_score > 21:
        return lose_message
    elif computer_score > 21:
        return win_message
    elif user_score > computer_score:
        return win_message
    else:
        return lose_message


def play_game():
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
        game_is_over = False
    else:
        game_is_over = True
    while not game_is_over:
        os.system('cls')
        print(logo)
        user_cards = get_random_cards(2)
        user_score = calculate_score(user_cards)
        computer_cards = get_random_cards(2)
        computer_score = calculate_score(computer_cards)
        print(f'Your cards: {user_cards}, current score: {user_score}')
        print(
            f"Computer's first card: {computer_cards[0]} => {cards[computer_cards[0]]}")

        if computer_score >= 21 or user_score >= 21:
            result = check_winner(user_cards, computer_cards)
            print(result)

        another_card = input(
            "Type 'y' to get another card, type 'n' to pass: ")
        if another_card == 'y':
            user_cards += get_random_cards(1)
            user_score = calculate_score(user_cards)
            print(f'Your cards: {user_cards}, current score: {user_score}')
            print(
                f"Computer's first card: {computer_cards[0]} => {cards[computer_cards[0]]}")

        result = check_winner(user_cards, computer_cards)
        print(result)

        if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
            game_is_over = False
        else:
            game_is_over = True


play_game()
