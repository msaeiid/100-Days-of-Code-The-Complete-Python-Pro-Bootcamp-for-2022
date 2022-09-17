import string


alphabet = [letter for letter in string.ascii_lowercase]
alphabet+=alphabet
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(start_text: str, shift_amount: int,cipher_direction: str):
    if not cipher_direction in ['encode','decode']:
        raise ValueError('wrong cipher_direction')
    
    end_text=''
    if cipher_direction =='decode':
        shift_amount*=-1
    for letter in start_text:
        position=alphabet.index(letter)
        new_position=position+shift_amount
        end_text+=alphabet[new_position]
    print(f'The {cipher_direction}d text is {end_text}')
caesar(text,shift,direction)