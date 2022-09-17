import math


def paint_calc(height: int, width: int, cover: int):
    area = height*width
    number_of_cans = area/cover
    return math.ceil(number_of_cans)


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
num = paint_calc(height=test_h, width=test_w, cover=coverage)
print(f"You'll need {num} cans paint.")
