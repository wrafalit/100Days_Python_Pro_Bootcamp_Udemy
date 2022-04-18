from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

chrome_driver_path = Service('C:\Program Files\Google\Chrome\Application\Development\chromedriver.exe')
driver = webdriver.Chrome(service=chrome_driver_path)

URL = "https://en.wikipedia.org/wiki/Main_Page"
driver.get(URL)
article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# article_count.click()

anyone_can_edit = driver.find_element(By.LINK_TEXT, "Contents")
# anyone_can_edit.click()

search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)



