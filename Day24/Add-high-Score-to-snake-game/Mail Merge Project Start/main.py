# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
PLACEHOLDER = '[name]'

with open('./Input/Letters/starting_letter.txt', mode='r') as template:
    template = template.read()
with open('./Input/Names/invited_names.txt', mode='r') as names:
    names = names.readlines()
for name in names:
    letter = template.replace(PLACEHOLDER, name.strip())
    with open(f'./Output/ReadyToSend/letter_for_{name.strip()}.txt', mode='w') as completed_letter:
        completed_letter.write(letter)
        completed_letter.close()
