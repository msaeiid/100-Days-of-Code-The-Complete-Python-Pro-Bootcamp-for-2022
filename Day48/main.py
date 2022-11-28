from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\Development\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
# driver.get(
#     "https://www.amazon.com/dp/B09MCV6W7W/ref=sspa_dk_detail_4?pd_rd_i=B09MCV6W7W&pd_rd_w=RO6Uo&content-id=amzn1.sym.46bad5f6-1f0a-4167-9a8b-c8a82fa48a54&pf_rd_p=46bad5f6-1f0a-4167-9a8b-c8a82fa48a54&pf_rd_r=N95YQY4RDBM0449TZZ86&pd_rd_wg=yBum1&pd_rd_r=97ed3395-43a2-44ca-b807-1d551fc6dccf&s=kitchen&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWw&th=1")

# price = driver.find_element(by=By.CLASS_NAME, value="a-price-whole")
# fraction = driver.find_element(By.CLASS_NAME, "a-price-fraction")
# print(price.text)
# print(fraction.text)


driver.get("https://www.python.org/")
# search_bar = driver.find_element(by=By.NAME, value="q")
# print(search_bar.tag_name)
# print(search_bar.get_attribute("placeholder"))
# logo = driver.find_element(by=By.CLASS_NAME, value="python-logo")
# print(logo.size)
# documentation_link = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-widget a")
# print(documentation_link.text)
select_by_xpath = driver.find_element(by=By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(select_by_xpath.text)
driver.quit()
