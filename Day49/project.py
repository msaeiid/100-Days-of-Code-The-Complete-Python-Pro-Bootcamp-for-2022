from selenium import webdriver
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

SLEEP_TIME = 2

USERNAME = "*"
PASSWORD = "*"

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.linkedin.com/")
# click sign in button
sign_in = driver.find_element(by=By.LINK_TEXT, value="Sign in")
sign_in.click()
# enter username and password and sign in
username_input = driver.find_element(by=By.ID, value="username")
username_input.send_keys(USERNAME)
password_input = driver.find_element(by=By.ID, value="password")
password_input.send_keys(PASSWORD)
sign_in_button = driver.find_element(by=By.CSS_SELECTOR, value=".login__form_action_container button")
sign_in_button.click()
# click on Job button in navbar
job_button = driver.find_elements(by=By.CSS_SELECTOR, value=".global-nav__nav .app-aware-link")[2]
job_button.click()


def clear_input(element: WebElement):
    for i in range(10):
        element.send_keys(Keys.BACKSPACE)


# Enter Job title in search box
job_title = input("enter job title")
search_input_title_1 = driver.find_elements(by=By.CSS_SELECTOR,
                                            value=".jobs-search-box__text-input")[0]
clear_input(search_input_title_1)
search_input_title_1.send_keys(job_title)
time.sleep(SLEEP_TIME)
title_option = driver.find_element(by=By.CSS_SELECTOR, value="li button")
time.sleep(SLEEP_TIME)
title_option.click()
# Enter country or town
country_title = input("enter Country/town ... ")
search_input_country_1 = driver.find_elements(by=By.CSS_SELECTOR,
                                              value=".jobs-search-box__text-input")[3]
clear_input(search_input_country_1)
search_input_country_1.send_keys(country_title)
time.sleep(SLEEP_TIME)
country_option = driver.find_element(by=By.CSS_SELECTOR, value="li button")
time.sleep(SLEEP_TIME)
country_option.click()
time.sleep(SLEEP_TIME)
apply_buttons = driver.find_elements(by=By.CSS_SELECTOR, value=".jobs-apply-button--top-card button")
# change browser tab
for button in apply_buttons:
    if button.text == 'Apply':
        button.click()
        break
opened_tabs = driver.window_handles
driver.switch_to.window(opened_tabs[len(opened_tabs) - 1])

input()
