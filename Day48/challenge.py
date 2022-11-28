from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\Development\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.python.org/")

times = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget time")
texts = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget li a")
events = {}
for i in range(len(times)):
    events[i] = {'time': times[i].text, 'name': texts[i].text}
print('')
