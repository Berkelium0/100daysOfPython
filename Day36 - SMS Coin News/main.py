import requests
import datetime as dt
import smtplib

smtp_server = "smtp.gmail.com"
port = 587

NEWS_API_KEY = "0189345d017f405eabfbeae909d6d20f"
news_params = {"q": "bitcoin", "apiKey": NEWS_API_KEY}

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
                        msg=f"{message}")


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
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
news_response = requests.get("https://newsapi.org/v2/everything", params=news_params)
articles = news_response.json()["articles"][:3]

articles_text = f"Headline: {articles[0]['title'].encode('ascii',errors='backslashreplace')}\nBrief: {articles[0]['description'].encode('ascii',errors='backslashreplace')}\n\n" + f"Headline: {articles[1]['title'].encode('ascii',errors='backslashreplace')}\nBrief: {articles[1]['description'].encode('ascii',errors='backslashreplace')}\n\n" + f"Headline: {articles[2]['title'].encode('ascii',errors='backslashreplace')}\nBrief: {articles[2]['description'].encode('ascii',errors='backslashreplace')}\n\n"
articles_text = articles_text
print(articles_text)
# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.

if abs(change) > 5:
    send_mail(f"Subject:Bitcoin Alert! Bitcoin has increased {format(change, '.3f')}%!\n\n{articles_text}")
elif abs(change) < -5:
    send_mail(f"Subject:Bitcoin Alert! Bitcoin has decreased {format(abs(change), '.3f')}%!\n\n{articles_text}")
else:
    send_mail(f"Subject:Bitcoin Alert! lol chill, Bitcoin only changed {format(change, '.3f')}%\n\n{articles_text}")

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
