from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "C:\Development\chromedriver.exe"

driver = webdriver.Chrome(chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(by=By.ID, value="cookie")
right_pane_name_list = ["buyCursor", "buyGrandma", "buyFactory", "buyMine", "buyShipment", "buyAlchemy lab",
                        "buyPortal", "buyTime machine"]


def find_last_right_pane():
    for n in range(len(right_pane_name_list) - 1, -1, -1):
        temp_pane = driver.find_element(by=By.ID, value=right_pane_name_list[n])
        number = temp_pane.text.split(' - ')[1].split("\n")[0]
        number = int(number.replace(',', ''))
        money = driver.find_element(by=By.ID, value="money").text
        money = int(money.replace(',', ''))
        if money > number:
            return temp_pane


def check_option():
    current_right_pane = find_last_right_pane()
    current_right_pane.click()


start_time = time.time()
timeout = (5 * 60) + start_time
step_time = start_time + 5
while time.time() < timeout:
    cookie.click()
    if time.time() > step_time:
        check_option()
        step_time = time.time() + 5
print(driver.find_element(by=By.ID, value="cps").text)
