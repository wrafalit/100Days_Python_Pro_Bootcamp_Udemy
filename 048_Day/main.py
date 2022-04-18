from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chrome_driver_path = Service('C:\Program Files\Google\Chrome\Application\Development\chromedriver.exe')
driver = webdriver.Chrome(service=chrome_driver_path)

URL = "https://shopee.pl/Twaróg-półtłusty-Włoszczowski-1-kg-i.544475742.17134626622?sp_atk=2ffa62da-35dc-42b2-97a6-bf1fa7974455"
URL2 = "https://www.amazon.com/Instant-Pot-Plus-60-Programmable/dp/B01NBKTPTS/ref=sr_1_3?keywords=instant%2Bpot%2Bduo%2Bevo%2Bplus%2B9-in-1&qid=1650134126&sprefix=instant%2Bpot%2Bduo%2Bevo%2Bplus%2B%2Caps%2C239&sr=8-3&th=1"
driver.get(URL2)

print(driver.find_element(By.CLASS_NAME, "apexPriceToPay").text)
driver.quit()

