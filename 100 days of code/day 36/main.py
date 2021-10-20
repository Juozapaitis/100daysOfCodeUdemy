import requests
import datetime
from twilio.rest import Client
import os
from dotenv import load_dotenv

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

load_dotenv('100 days of code//.gitignore')

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = os.getenv('stock_api_key')
NEWS_API_KEY = os.getenv('news_api_key')
ACCOUNT_SID = os.getenv('account_sid')
AUTH_TOKEN = os.getenv('auth_token')
FROM_NUMBER = os.getenv('from_number')
TO_NUMBER = os.getenv('to_number')

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

stock_params = {
    'function': "TIME_SERIES_DAILY",
    'symbol': STOCK_NAME,
    'apikey': STOCK_API_KEY,
}

response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

#TODO 2. - Get the day before yesterday's closing stock price

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

difference = float(day_before_yesterday_closing_price) - float(yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "⬆️"
else:
    up_down = "⬇️"


#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

difference_percent = round(difference / float(yesterday_closing_price)) * 100

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").


if abs(difference_percent) > 1:
    news_params = {
        'apiKey': NEWS_API_KEY,
        'q': COMPANY_NAME,
    }

    news_response = requests.get(url=NEWS_ENDPOINT,params=news_params)
    news_data = news_response.json()["articles"]
    three_articles = news_data[:3]

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.



#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 


#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
nl = '\n'
formatted_articles_list = [f"{STOCK_NAME}: {up_down}{difference_percent}%\nHeadline: {article['title']}. {nl} Brief: {article['description']}." for article in three_articles]
#TODO 9. - Send each article as a separate message via Twilio. 

client = Client(ACCOUNT_SID, AUTH_TOKEN)
for article in formatted_articles_list:
    message = client.messages.create(
        body = article,
        from_ = FROM_NUMBER,
        to = TO_NUMBER,
    )
    print(message)

#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

