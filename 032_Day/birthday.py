import pandas as pd
import datetime as dt
import smtplib
import random

def send_email():
    my_email = "wraxxxxxxmail.com"
    password = "Pyxxxxx12#"
    to_addres_email = "pyxxxxp.pl"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_email,
            msg=f"Subject:Happy Birthday\n\n{birth_letter_name}")


with open("birthdays.csv", mode="r") as file_birth:
    data_birthday = pd.read_csv(file_birth)

birht_dic = data_birthday.to_dict(orient="records")
# print(data_birthday)
# print(birht_dic)

now = dt.datetime.now()
now_month = now.month
now_day = now.day

for birth in birht_dic:
    print(birth["day"])
    if birth["day"] == now_day and birth["month"] == now_month:
        # print("birthday found")
        # print(birth["name"])
        birthday_name = birth["name"]
        # print(birth["email"])
        birthday_email = birth["email"]
        birthday_found = True


letter_templates = ["./letter_templates/letter_1.txt", "./letter_templates/letter_2.txt", "./letter_templates/letter_3.txt"]
random_letter = random.choice(letter_templates)
print("\n\n\n")
with open(random_letter, mode="r") as file:
    birth_letter = file.read()


birth_letter_name = birth_letter.replace("[NAME]", birthday_name)
birth_letter_name = birth_letter_name.replace("Lenar", "Rafal")
print(birth_letter_name)

if (birthday_found):
    send_email()