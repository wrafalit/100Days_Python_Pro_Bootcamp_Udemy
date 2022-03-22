

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#Get yesterday's closing stock price



#Get the day before yesterday's closing stock price


#Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp


#Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.


    ## STEP 2: Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

#Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
#If difference percentage is greater than 5 then print("Get News").


    #Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use Twilio to send a seperate message with each article's title and description to your phone number.

    #Create a new list of the first 3 article's headline and description using list comprehension.

    #Send each article as a separate message via Twilio.


    #TOD 8. - Send each article as a separate message via Twilio.
