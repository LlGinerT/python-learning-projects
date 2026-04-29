import random
import smtplib
import datetime as dt

from constants import *

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 4:
    with open("quotes.txt") as quotes_file:
        all_quotes = quotes_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)

    with smtplib.SMTP(HOST) as connection:  # mail provider path
        connection.starttls()
        connection.login(user=MY_EMAIL, password=KEY)
        connection.sendmail(
            from_addr=MY_EMAIL, to_addrs="", msg=f"Subject:Hello World!\n\n{quote}"
        )  # Syntax "Subject:Hello\n\nBody"
        connection.close()
        # create apiKey
        # if explode check the previous lesson or url on the error
