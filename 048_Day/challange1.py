from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chrome_driver_path = Service('C:\Program Files\Google\Chrome\Application\Development\chromedriver.exe')
driver = webdriver.Chrome(service=chrome_driver_path)

URL = "https://www.python.org/"
driver.get(URL)
# print(driver.find_element(By.CSS_SELECTOR, ".event-widget time"))
dates = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
# print(dates)

# for date in dates:
#     print(date.text)


# print(driver.find_element(By.CSS_SELECTOR, ".event-widget ").text)
events = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
for event in events:
    print(event.text)

# dic_list = {}
# dic = {}
# n=0
# for event in events[1:]:
#     for d in dates:
#         dic["time"]=d.text
#         dic['name']=event.text
#         dates.remove(d)
#         # print(dic)
#         dic_list[n]=dic
#         n += 1
#         break
#
# print(dic_list)

driver.quit()