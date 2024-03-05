import time
from selenium import webdriver

service = webdriver.ChromeService('./chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')

driver = webdriver.Chrome(service=service, options=options)
time.sleep(5)
driver.quit()
