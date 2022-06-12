import smtplib
import datetime as dt
import random
import pandas

message = "Subject: Letter from Python \n\n There is a body of email i guess"


def send_mail(message):
    MY_EMAIL = '@hotmail.com'
    # Important - hotmail is not hotmail. Its outlook.
    with smtplib.SMTP('outlook.office365.com') as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password='')  # < might leak so random.
        connection.sendmail(from_addr=MY_EMAIL, to_addrs='', msg=message)


def check_list():
    data = pandas.read_csv('dates.csv')
    now = dt.datetime.now()

    for row in range(len(data)):
        # print(data.loc[row]['month'] == now.month)
        # print(data.loc[row]['day'] == now.day)
        if now.month == data.loc[row]["month"] and now.day == data.loc[row]["day"]:
            print(f"Whooo its a {data.loc[row]['name']} birthday!")
            # send a random letter with [NAME] being replaced by relevant Name. Lazy to write letters for now


def call_baal():
    global message
    now = dt.datetime.now()
    with open('quotes.txt', 'r') as file:
        quotes = file.readlines()
    if now.day == 18 and now.month == 2:
        message = f"Subject: Quote of the Day\n\n {random.choice(quotes)}"
        send_mail(message)
    else:
        pass


# time.sleep(5)
# call_baal()
#
# call_baal()
check_list()
