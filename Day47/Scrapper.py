import requests
import bs4


class Scrapper:
    def __init__(self):
        self.headers = {
            "Request Line": "GET / HTTP/1.1",
            "Accept": f"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-GB,en;q=0.9,fa-IR;q=0.8,fa;q=0.7,en-US;q=0.6",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
        }

    def check(self, url: str, user_price: float):

        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            soup = bs4.BeautifulSoup(response.text, "html.parser")
            is_available = soup.find(name="div", id="availability")
            if not (is_available is None) and is_available.text.strip() == "Currently unavailable.":
                print("Currently unavailable.")
            else:
                whole_price = soup.find(name="span", class_="a-price-whole").text
                fraction_price = soup.find(name="span", class_="a-price-fraction").text
                title = soup.find(name="span", id="productTitle").text.strip()
                if len(fraction_price):
                    total = float(whole_price + fraction_price)
                else:
                    total = int(whole_price)
                return total < user_price, title, total
        else:
            print("Service is unavailable")
