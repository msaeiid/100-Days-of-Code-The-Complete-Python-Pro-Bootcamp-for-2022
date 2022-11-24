from FileOperation import FileOperation
from Email import Email
from Scrapper import Scrapper


class Main:

    def __init__(self):
        self.file_operation = FileOperation()
        self.email_operation = Email()
        self.scrapper = Scrapper()

    def add_url(self):
        user_url = input("Url: ")
        user_set_price = input("Price:$ ")
        self.file_operation.write_data(user_url, user_set_price)

    def check(self):
        urls_dict = self.file_operation.load_data()
        if not urls_dict is None:
            for url, price in urls_dict.items():
                status, title, price = self.scrapper.check(url, price)
                if status:
                    self.email_operation.send(title, price, url)
                else:
                    print(f"The price of \n{title}\n is more than {price}")

    def operation(self):
        while True:
            user_input = input("To check enter c and To add url enter a: ").lower()
            if user_input == "c":
                self.check()
            elif user_input == "a":
                self.add_url()


main = Main()
main.check()
main.operation()
