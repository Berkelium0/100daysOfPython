##################### Extra Hard Starting Project ######################
import pandas
import random
import smtplib
import datetime as dt
import gspread

# sa = gspread.service_account(filename="buoyant-country-352515-8e59ad0bbf01.json")
# birthdays = sa.open("birthdays").worksheet("Form Responses 1").get_all_records()

birthdays = pandas.read_csv("birthdays.csv").to_dict(orient="records")

smtp_server = "smtp.gmail.com"
port = 587

my_email = "dgko31@gmail.com"
password = "vkomkcdthltoqtpr"


# 1. Update the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.

def send_birthday_wish(bday):
    letters = [
        "letter_templates/letter_1.txt",
        "letter_templates/letter_2.txt",
        "letter_templates/letter_3.txt",
        "letter_templates/letter_4.txt"
    ]

    with open(random.choice(letters)) as letter:
        message = letter.read().replace("[NAME]", bday["name"])
        try:
            with smtplib.SMTP(smtp_server, port) as server:
                server.ehlo()  # check connection
                server.starttls()  # Secure the connection
                server.ehlo()  # check connection
                server.login(my_email, password)

                # Send email here
                server.sendmail(from_addr=my_email,
                                to_addrs=bday["email"],
                                msg=f"Subject:DGKO!!!!\n\n{message}")

        except Exception as e:
            # Print any error messages
            print(e)


# 2. Check if today matches a birthday in the birthdays.csv
for birthday in birthdays:
    if birthday["day"] == dt.datetime.now().day and birthday["month"] == dt.datetime.now().month:
        send_birthday_wish(birthday)
