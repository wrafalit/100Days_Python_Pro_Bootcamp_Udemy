# import smtplib
#
# my_email = "wrafxxxxxxil.com"
# password = "Pythxxxxxxxt12#"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="pyxxxxxxx.pl",
#         msg="Subject:Hello\n\n This is the body of my email"
#     )

import datetime as dt

now = dt.datetime.now()
year = now.year
mont = now.month
day_of_week = now.weekday()
print(year)
print(mont)
print(day_of_week)

data_of_birth = dt.datetime(year= 1986,month= 11, day=13)
print(data_of_birth)
