import pandas

data = pandas.read_csv('./nato_phonetic_alphabet.csv')
# TODO 1. Create a dictionary in this
nato_phonetic_alphabet_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(nato_phonetic_alphabet_dict)
# TODO 2. Create a list of the phonetic code words from a word that user inputs

user_input = input("Enter a word: ").upper()
result = [nato_phonetic_alphabet_dict[letter] for letter in user_input]
print(result)
