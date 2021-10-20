from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:/Users/justa/chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

driver.get("http://secure-retreat-92358.herokuapp.com/")


first_name = driver.find_element_by_name('fName')
first_name.send_keys("Justas")

last_name = driver.find_element_by_name('lName')
last_name.send_keys("Ju")

email = driver.find_element_by_name('email')
email.send_keys("g@gmail.com")

button = driver.find_element_by_css_selector('form button')
button.click()

# all_article_number = driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]')
# # all_article_number.click()

# all_portals = driver.find_element_by_link_text("All portals")
# # all_portals.click()

# search_window = driver.find_element_by_name("search")
# search_window.click()
# search_window.send_keys("Python")
# search_window.send_keys(Keys.ENTER)

# submit_button = driver.find_element_by_name("go")
# submit_button.click()

# driver.quit()