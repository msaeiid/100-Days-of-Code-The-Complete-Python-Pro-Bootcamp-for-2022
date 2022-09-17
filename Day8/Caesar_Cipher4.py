from cmath import log
import string
from art import logo
print(*logo)


def caesar(start_text: str, shift_amount: int, cipher_direction: str):
    if not cipher_direction in ['encode', 'decode']:
        raise ValueError('wrong cipher_direction')

    end_text = ''
    if cipher_direction == 'decode':
        shift_amount *= -1
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position+shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += letter
    print(f'The {cipher_direction}d text is {end_text}')


alphabet = [letter for letter in string.ascii_lowercase]
alphabet += alphabet
go_on = 'yes'
while go_on == 'yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 26:
        shift = shift % 26
    caesar(text, shift, direction)
    go_on = input("Type 'yes' if want to go again. Otherwise type 'no'")
print("Good bye!")
