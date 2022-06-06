import datetime as dt
import smtplib
import random


smtp_server = "smtp.gmail.com"
port = 587

my_email = "dgko31@gmail.com"
password = "vkomkcdthltoqtpr"


def get_message():
    with open("quotes.txt") as q_data:
        quotes = q_data.readlines()
        return f"Subject: Monday Motivation\n\n{random.choice(quotes)}"


# Try to log in to server and send email
def send_mail():
    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  # check connection
            server.starttls()  # Secure the connection
            server.ehlo()  # check connection
            server.login(my_email, password)

            # Send email here
            server.sendmail(from_addr=my_email,
                            to_addrs=["berkeebrus@gmail.com", "iborahim4033@gmail.com", "ozdamarrirem@gmail.com",
                                      "deryauluturk9@gmail.com", "basakgoksu@gmail.com", "engindenizcabukk@gmail.com"],
                            msg=get_message())

    except Exception as e:
        # Print any error messages
        print(e)


if dt.datetime.now().weekday() == 0:
    send_mail()
