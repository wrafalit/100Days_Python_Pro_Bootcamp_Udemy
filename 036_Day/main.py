import math
import datetime
import requests

API = "2422xxx98d69e8"
COMPANY = "ibm"
DATE = datetime.datetime.now().date()
URL = f"https://newsapi.org/v2/everything?q={COMPANY}&from={DATE}&language=en&sortBy=publishedAt&apiKey={API}"



## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

response = requests.get(url="https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo")
response.raise_for_status()
print(response)
data_IBM = response.json()
print(data_IBM)

#Get yesterday's closing stock price
yester_IBM_close = float(data_IBM["Time Series (Daily)"]["2022-03-22"]["4. close"])
print(yester_IBM_close)

#Get the day before yesterday's closing stock price
before_yester_IBM_close = float(data_IBM["Time Series (Daily)"]["2022-03-21"]["4. close"])
print(before_yester_IBM_close)

#Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = abs(yester_IBM_close - before_yester_IBM_close)
print(difference)

#Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentage_diff = abs((before_yester_IBM_close / yester_IBM_close) * 100 - 100)
print(round(percentage_diff, 2))

#If difference percentage is greater than 5 then print("Get News").
if percentage_diff > 5:
    print("Get News")

## STEP 2: Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
#Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

respons_news = requests.get(url=URL)
respons_news.raise_for_status()
news_data = respons_news.json()

news_list = []
for n in range(3):
    news_list.append(news_data["articles"][n]["title"][:100])
# print(news_data["articles"][0]["title"][:100])
print(news_list)



    #Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use Twilio to send a seperate message with each article's title and description to your phone number.

    #Create a new list of the first 3 article's headline and description using list comprehension.

    #Send each article as a separate message via Twilio.


    #TOD 8. - Send each article as a separate message via Twilio.
