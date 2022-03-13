import datetime as dt
import random
import smtplib

# ------------------------------ open file ----------------------------------

with open("quotes.txt", mode="r") as file:
    quotes = file.readlines()

# quotes_list = quotes.split("\n")
random_quote = random.choice(quotes)
print(quotes)

current_week_day = dt.datetime.weekday(dt.datetime.now())
# print(current_week_day)

# ------------------------------- send email -------------------------------

my_email = "wrxxxxmail.com"
password = "Pythxxxx12#"
to_addres_email = "pythoxxxxxx.pl"

with smtplib.SMTP("smtxxxxxom") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)

    if current_week_day == 6:
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_addres_email,
            msg=f"Subject:Motivational quote for today\n\n {random_quote}")