
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# WINDOWS
# service = webdriver.ChromeService('./chromedriver.exe')

# LINUX
service = webdriver.ChromeService('./chromedriver-linux64/chromedriver')

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_experimental_option('prefs', {
    # 'download.default_directory': 'C:\\Users\\araza\\Documents\\1\\gits\\SGX-Derivative-Scraper\\diels\\',
    'download.default_directory': os.path.join(os.getcwd(), 'diels')
})

# LINUX
options.binary_location = './chrome-linux64/chrome'

driver = webdriver.Chrome(service=service, options=options)

driver.get('https://www.sgx.com/research-education/derivatives')

button = driver.find_element(By.XPATH, '//*[@id="page-container"]/template-base/div/div/section[1]/div/sgx-widgets-wrapper/widget-research-and-reports-download[1]/widget-reports-derivatives-tick-and-trade-cancellation/div/button')

driver.execute_script('arguments[0].click()', button)

print('sleeping')
time.sleep(5)

driver.quit()
