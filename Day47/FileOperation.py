class FileOperation:

    def __init__(self):
        self.file_path = './url.txt'

    def write_data(self, url: str, price: float):
        with open(self.file_path, mode="a") as file:
            file.write(f"{url} - {price}\n")

    def load_data(self):
        try:
            with open(self.file_path, mode="r") as file:
                url_dict = {}
                for line in file.readlines():
                    temp_url = line.split(" - ")[0]
                    temp_price = float(line.split(" - ")[1].split('\n')[0])
                    url_dict[temp_url] = temp_price
                return url_dict
        except FileNotFoundError:
            with open("./url.txt", mode="w") as url_file:
                print("There isn't any url in file")
