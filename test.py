import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# WINDOWS
# service = webdriver.ChromeService('./chromedriver.exe')

# LINUX
service = webdriver.ChromeService('./chromedriver-linux64/chromedriver')

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')

# LINUX
# options.add_argument('--headless')
options.binary_location = './chrome-linux64/chrome'

driver = webdriver.Chrome(service=service, options=options)

driver.get('https://google.com')

tb = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
tb.send_keys('testing')
print(tb.get_property('value'))
driver.execute_script('arguments[0].value = "hatdog"', tb)
print(tb.get_property('value'))
tb.send_keys(Keys.ENTER)

searched = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')

print(searched.get_property('value'))

time.sleep(5)
print('time for bed')
# driver.quit()
