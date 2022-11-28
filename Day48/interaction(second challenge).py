from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

## Second challenge
chrome_driver_path = "C:\Development\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
#
# article_count = driver.find_element(by=By.CSS_SELECTOR, value="#articlecount a")
# print(article_count.text)

## First way to click with selenium
# article_count.click()
## Second way to click with selenium
# all_portals = driver.find_element(by=By.LINK_TEXT, value="Content portals")
# all_portals.click()
## Fill in form with selenium
##first find search box
# search = driver.find_element(by=By.NAME, value="search")
##Fill in search box
# search.send_keys("python")
##Press enter button to search
# search.send_keys(Keys.ENTER)

##Third challenge
driver.get("http://secure-retreat-92358.herokuapp.com/")
fname = driver.find_element(by=By.NAME, value="fName")
fname.send_keys("Saeid")
lname = driver.find_element(by=By.NAME, value="lName")
lname.send_keys("Karbaschian")
email = driver.find_element(by=By.NAME, value="email")
email.send_keys("mskarbaschian@gmail.com")

submit_button = driver.find_element(by=By.CSS_SELECTOR, value="form button")
submit_button.click()
print()
