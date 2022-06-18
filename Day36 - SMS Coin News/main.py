import requests
import datetime as dt
import smtplib

smtp_server = "smtp.gmail.com"
port = 587

my_email = "dgko31@gmail.com"
password = "vkomkcdthltoqtpr"


def send_mail(message):
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # check connection
        server.starttls()  # Secure the connection
        server.ehlo()  # check connection
        server.login(my_email, password)

        # Send email here
        server.sendmail(from_addr=my_email,
                        to_addrs="berkeebrus@gmail.com",
                        msg=f"Subject:Bitcoin Alert!!!!\n\n{message}")


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
headers = {'X-CoinAPI-Key': '53B1D41A-90C3-4C32-8B10-59BAA2C90A48'}

yesterday = dt.datetime.today().date() - dt.timedelta(days=1)
day_before_yesterday = yesterday - dt.timedelta(days=1)

yesterday_url = f'https://rest.coinapi.io/v1/trades/BITSTAMP_SPOT_BTC_USD/history?time_start={yesterday}T08:00:00'
yesterday_price = requests.get(yesterday_url, headers=headers).json()[0]["price"]

day_before_yesterday_url = f'https://rest.coinapi.io/v1/trades/BITSTAMP_SPOT_BTC_USD/history?time_start={day_before_yesterday}T08:00:00'
day_before_yesterday_price = requests.get(day_before_yesterday_url, headers=headers).json()[0]["price"]

change = ((day_before_yesterday_price - yesterday_price) / yesterday_price) * 100

if abs(change) > 5:
    send_mail(f"Bitcoin has increased {format(change, '.3f')}%!")
elif abs(change) < -5:
    send_mail(f"Bitcoin has decreased {format(change, '.3f')}%!")
else:
    send_mail(f"lol chill, Bitcoin onl changed {format(change, '.3f')}%")
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
