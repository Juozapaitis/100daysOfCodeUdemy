from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "C:/Users/justa/chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

driver.get("https://orteil.dashnet.org/cookieclicker/")

cookie = driver.find_element_by_id("bigCookie")

items = driver.find_elements_by_css_selector('#store div')
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
five_min = time.time() + 60 * 5

while True:
    cookie.click()

    # Every 5 seconds:
    if time.time() > timeout:

        all_prices = driver.find_elements_by_class_name("enabled")
        item_prices = []

        for price in all_prices:
            element_text = price.text
            if element_text != "":
                if "," in element_text:
                    cost = int(element_text.replace(",", ""))
                    print(cost)
                else:
                    print("+")
                    print(int(float(element_text.replace("Cursor\n", "")))) # Error "Cursor" has to be {name_of_product}
                    print("+")
                    cost = int(float(element_text.replace("Cursor\n", "")))
                    print(cost)
                item_prices.append(cost)
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        #Get current cookie count
        money_element = driver.find_element_by_id("cookies").text
        money_element = money_element.split(" ")[0]
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        #Find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            # print(f" {cost} and  {id}")
            if cookie_count > cost:
                 affordable_upgrades[cost] = id

        #Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element_by_id(to_purchase_id).click()
        
        #Add another 5 seconds until the next check
        timeout = time.time() + 5

    #After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > five_min:
        cookie_per_s = driver.find_element_by_id("cps").text
        print(cookie_per_s)
        break