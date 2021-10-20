from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time

chrome_driver_path = "C:/Users/justa/chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

zillow_url = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.69219435644531%2C%22east%22%3A-122.17446364355469%2C%22south%22%3A37.703343724016136%2C%22north%22%3A37.847169233586946%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D"

zillow_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "lt-LT,lt;q=0.9,en-LT;q=0.8,en;q=0.7,en-US;q=0.6,ru;q=0.5,pl;q=0.4"
}
response = requests.get(url=zillow_url, headers=zillow_headers)

website_html = response.text

soup = BeautifulSoup(website_html, 'html.parser')

all_rental_listings_elements = soup.select('.list-card-top a')
rental_listings_links = []

for listing in all_rental_listings_elements:
    link = listing["href"]
    if 'http' not in link:
        link = f"https://www.zillow.com{link}"
    rental_listings_links.append(link)

all_address_elements = soup.select('.list-card-addr')
all_addresses = [address.getText().split(" | ")[-1] for address in all_address_elements]

all_price_elements = soup.select(".list-card-price")
all_prices = [price.get_text().replace("/", "+").replace(" 1 bd", "").split("+")[0] for price in all_price_elements if "$" in price.text]

driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

for n in range(len(rental_listings_links)):
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeu575IDrOgg6xOADIq-fQfR0PF2TAceqCZjtbCRFS4Mtt4pA/viewform?usp=sf_link")
    
    time.sleep(2)
    address = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')

    address.send_keys(all_addresses[n])
    price.send_keys(all_prices[n])
    link.send_keys(rental_listings_links[n])
    submit_button.click()

