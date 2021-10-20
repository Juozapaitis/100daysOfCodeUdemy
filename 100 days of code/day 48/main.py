from selenium import webdriver

chrome_driver_path = "C:/Users/justa/chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

driver.get("https://www.python.org/")


event_times = driver.find_elements_by_css_selector('.event-widget time')
titles = driver.find_elements_by_css_selector('.event-widget ul a')
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": titles[n].text,
    }

print(events)

driver.quit()