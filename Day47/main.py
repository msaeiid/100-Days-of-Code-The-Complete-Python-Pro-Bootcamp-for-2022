def get_url():
    user_url = input("Url: ")
    user_set_price = input("Price: ")
    with open("./url.txt", mode="a") as url_file:
        url_file.write(f"{user_url} - {user_set_price}\n")


def check():
    url_dict = {}
    try:
        with open("./url.txt", mode="r") as url_file:
            for line in url_file.readlines():
                temp_url = line.split(" - ")[0]
                temp_price = line.split(" - ")[0]
                url_dict[temp_url] = temp_price
        print(url_dict)
    except FileNotFoundError:
        with open("./url.txt", mode="w") as url_file:
            pass


def run():
    while True:
        user_input = input("To check enter c and To add url enter a: ").lower()
        if user_input == "c":
            check()
        elif user_input == "a":
            get_url()


check()
run()
