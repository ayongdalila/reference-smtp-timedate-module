# ------------------------------- Sending Email Using SMTP ------------------------------- #

import smtplib

my_email = "nordalilaforcodinguse@gmail.com"
password = "iesthglskbruwgzy"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, 
                        to_addrs="nordalila2704@gmail.com", 
                        msg="Subject: Hello\n\nThis is the body of the email.")

# ------------------------------- DateTime Module ------------------------------- #

import datetime as dt

# to get the current date and time
now = dt.datetime.now()
print(now)
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
print(year)
print(month)
print(day)
print(hour)
print(minute)

# 1 is Tuesday, 2 is Wednesday, 3 is Thursday, 4 is Friday, 5 is Saturday, 6 is Sunday, 0 is Monday
day_of_week = now.weekday()
print(day_of_week)

# to create a new date object
date_of_birth = dt.datetime(year=1997, month=10, day=28)
print(date_of_birth)

if date_of_birth.month != now.month:
    print("Not your birthday month")
else:
    print("Happy Birthday Month!")


# ------------------------------- Using SMTP and DateTime Module ------------------------------- #

import random
import datetime as dt
import smtplib

my_email = "nordalilaforcodinguse@gmail.com"
password = "iesthglskbruwgzy"

now = dt.datetime.now()
if now.weekday() == 1:  # Check if today is Tuesday (1)
    with open("quotes.txt") as file:    
        all_quotes = file.readlines()

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="nordalila2704@gmail.com",
            msg=f"Subject: Tuesday Motivation\n\n{random.choice(all_quotes)}"
        )

