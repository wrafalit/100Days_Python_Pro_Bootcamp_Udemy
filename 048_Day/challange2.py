from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

chrome_driver_path = Service('C:\Program Files\Google\Chrome\Application\Development\chromedriver.exe')
driver = webdriver.Chrome(service=chrome_driver_path)

URL = "https://secure-retreat-92358.herokuapp.com/"
driver.get(URL)

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Rafal")

lName = driver.find_element(By.NAME, "lName")
lName.send_keys("It")

email = driver.find_element(By.NAME, "email")
email.send_keys("asda@ow.ps")

button = driver.find_element(By.CSS_SELECTOR, ".btn")
button.click()