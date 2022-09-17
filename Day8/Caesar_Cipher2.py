import string


alphabet = [letter for letter in string.ascii_lowercase]
#alphabet += alphabet
print(alphabet)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text: str, shift_amount: int):
    cipher_text = ''
    for letter in plain_text:
        position = alphabet.index(letter)
        if position == 25:
            position = -1
        cipher_text += alphabet[position+shift_amount]
    print(f'The encoded text is {cipher_text}')


def decrypt(cipher_text: str, shift_amount: int):
    plain_text = ''
    for letter in cipher_text:
        position = alphabet.index(letter)
        plain_text += alphabet[position-shift_amount]
    print(f'The decoded text is {plain_text}')


if direction == 'encode':
    encrypt(plain_text=text, shift_amount=shift)
elif direction == 'decode':
    decrypt(cipher_text=text, shift_amount=shift)
