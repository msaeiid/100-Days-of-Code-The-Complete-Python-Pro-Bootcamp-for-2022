fruits = ["Apple", "Pear", "Orange"]


def make_pie(index: int):
    try:
        fruit = fruits[index]
    except IndexError as message:
        print(f"Fruit pie")
    else:
        print(f"fruit {fruit}")


make_pie(4)
