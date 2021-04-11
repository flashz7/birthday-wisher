import smtplib
import pandas
import datetime as dt
from random import randint

now = dt.datetime.now()
my_email = "jb.does.python@gmail.com"
password = "Eh73D*qN4#Gu"

birthday_list = pandas.read_csv("birthdays.csv")
for index, row in birthday_list.iterrows():
    if row['month'] == now.month and row['day'] == now.day:
        send_to = row['email']
        name = row['name']
        letter = f'letter_{randint(1, 3)}.txt'
        with open(f'./letter_templates/{letter}', "r") as f:
            letter_text = f.read()
            letter_text = letter_text.replace('[NAME]', name)

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=send_to,
                msg=f"Subject: Happy Birthday!\n\n{letter_text}"
            )