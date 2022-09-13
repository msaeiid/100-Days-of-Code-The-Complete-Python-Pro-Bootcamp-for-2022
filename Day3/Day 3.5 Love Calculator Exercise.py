print("Welcome to the Love Calculator!")
first_name = input("What is your name?\n ")
second_name = input("What is the other name?\n")

first_digit = 0
second_digit = 0

sent_true = 'true'
sent_love = 'love'
combine_sentence = first_name.lower()+second_name.lower()

for item in sent_true:
    first_digit += combine_sentence.count(item)
for item in sent_love:
    second_digit += combine_sentence.count(item)

score = first_digit * 10 + second_digit
if score < 10 or score > 90:
    print(f"your score is {score} ,you go together like coke and mentos.")
if score >= 40 and score <= 50:
    print(f"Your score {score}, you are alright together.")
else:
    print(f"Your score is {score}")
