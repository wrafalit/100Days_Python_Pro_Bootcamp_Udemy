from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = Service('C:\Program Files\Google\Chrome\Application\Development\chromedriver.exe')
driver = webdriver.Chrome(service=chrome_driver_path)

# URL = "https://orteil.dashnet.org/experiments/cookie/"
URL = "https://orteil.dashnet.org/cookieclicker/"
driver.get(URL)

cookie = driver.find_element(By.ID, "bigCookie")

n=0
while n<1000:
    cookie.click()
    time.sleep(0.5)

    n +=1