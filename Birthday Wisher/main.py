import smtplib
import datetime as dt
import random
# import pandas

MY_EMAIL = "DummyGamilAccount@gmail.com"
PASSWORD = "pASSWORDcREATEbYgOOGLE"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:
    with open('quotes.txt', 'r') as data_file:
        all_quote = data_file.readlines()
        quote = random.choice(all_quote)

    print(quote)
    # It is my personal account
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="k************d@gmail.com",
            msg=f"Subject:Monday Motivation\n\n{quote}" 
        ) 
        connection.close()
