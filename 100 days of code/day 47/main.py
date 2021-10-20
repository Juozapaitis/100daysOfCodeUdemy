from bs4 import BeautifulSoup
import requests
import lxml
import smtplib
from email.message import EmailMessage
from unidecode import unidecode

BUY_PRICE = 200

url = "https://www.amazon.com/dp/B091TTDRVP/"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language":"lt-LT,lt;q=0.9,en-LT;q=0.8,en;q=0.7,en-US;q=0.6,ru;q=0.5,pl;q=0.4",
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, 'lxml')

title = soup.find(id="productTitle").getText().strip()
price = soup.find(id="priceblock_ourprice").getText()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login('forTestingUcCiu@gmail.com', "fr(KGH$7b2tOm")
        connection.sendmail(
            from_addr='forTestingUcCiu@gmail.com',
            to_addrs='forTestingUcCiu@gmail.com',
            msg=f"Subject:{title} price is under your buy price!\n\n{message}\n{url}".encode("utf-8")
        )