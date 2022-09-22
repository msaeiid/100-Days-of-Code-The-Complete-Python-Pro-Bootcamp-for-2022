##############DEBUGGING##############

# for i in range(1, 20):  # change 20 to 21
#     if i == 20:
#         print("You got it")


## produce the bug
# from random import randint
# dice_imgs = ["1", "2", "3", "4", "5", "6"]
# dice_num = randint(1, 6)  # change 1, 6 to 0, len(dice_imgs)-1 or 5
# print(dice_imgs[dice_num])  # OR dice_num -1

## Play Computer
# year = int(input("What's your year of birth? "))
# if year > 1980 and year < 1994:
#     print("You are a millenial.")
# elif year > 1994:  # change > to >=
#     print("You are a Gen Z.")


## Fix the Errors
# you must cast to=> int age=int(input("How old are you? "))
# age = input("How old are you? ")
# if age > 18:
# print(f"You can drive at age {age}.")  # indent this line

# Print is your friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))  # replace == with =
# total_words = pages*word_per_page
# print(total_words)

##Use a Debugger
# def mutate(a_list):
#     b_list=[]
#     for item in a_list:
#         new_item = item*2
#     b_list.append(new_item)# indent this line
#     print(b_list)
    
# mutate([1,2,3,5,8,13])