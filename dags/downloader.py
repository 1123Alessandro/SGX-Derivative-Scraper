import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json

# WINDOWS
# service = webdriver.ChromeService('./chromedriver.exe')

def fetch_data():

    service = webdriver.ChromeService('./chromedriver-linux64/chromedriver')
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_experimental_option('prefs', {
        'download.default_directory': os.path.join(os.getcwd(), 'diels')
    })

    options.binary_location = './chrome-linux64/chrome'

    driver = webdriver.Chrome(service=service, options=options)

    driver.get('https://www.sgx.com/research-education/derivatives')

    time.sleep(3)
    dates = driver.find_element(By.XPATH, '//*[@id="page-container"]/template-base/div/div/section[1]/div/sgx-widgets-wrapper/widget-research-and-reports-download[1]/widget-reports-derivatives-tick-and-trade-cancellation/div/sgx-input-select[2]/sgx-select-model')

    entries = dates.get_property('_options')
    for i in entries:
        i['selected'] = False

    raw = json.dumps(entries)
    driver.execute_script(f"arguments[0]._options = {raw}", dates)

    types = driver.find_element(By.XPATH, '//*[@id="page-container"]/template-base/div/div/section[1]/div/sgx-widgets-wrapper/widget-research-and-reports-download[1]/widget-reports-derivatives-tick-and-trade-cancellation/div/sgx-input-select[1]/sgx-select-model')

    entries = types.get_property('_options')
    for i in entries:
        i['selected'] = False

    raw = json.dumps(entries)

    driver.execute_script(f"arguments[0]._options = {raw}", types)

    button = driver.find_element(By.XPATH, '//*[@id="page-container"]/template-base/div/div/section[1]/div/sgx-widgets-wrapper/widget-research-and-reports-download[1]/widget-reports-derivatives-tick-and-trade-cancellation/div/button')
    driver.execute_script('arguments[0].click()', button)

    time.sleep(5)
