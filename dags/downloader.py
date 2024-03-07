import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json

# WINDOWS
# service = webdriver.ChromeService('./chromedriver.exe')

def option_select(driver, xpath, option=None):
    options = driver.find_element(By.XPATH, xpath)
    entries = options.get_property('_options')

    if option == None:
        return {
            'element': options,
            'entries': json.dumps(entries)
        }

    for i in entries:
        if i['label'] == option:
            i['selected'] = True
        else:
            i['selected'] = False

    return {
        'element': options,
        'entries': json.dumps(entries)
    }

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
    driver.implicitly_wait(5)

    # time.sleep(3)
    # TODO: loop through each required type to download
    new_dates = option_select(driver, '//*[@id="page-container"]/template-base/div/div/section[1]/div/sgx-widgets-wrapper/widget-research-and-reports-download[1]/widget-reports-derivatives-tick-and-trade-cancellation/div/sgx-input-select[2]/sgx-select-model')
    driver.execute_script(f"arguments[0]._options = {new_dates['entries']}", new_dates['element'])

    for i in ['Tick', 'Tick Data Structure', 'Trade Cancellation', 'Trade Cancellation Data Structure']:
        new_types = option_select(driver, '//*[@id="page-container"]/template-base/div/div/section[1]/div/sgx-widgets-wrapper/widget-research-and-reports-download[1]/widget-reports-derivatives-tick-and-trade-cancellation/div/sgx-input-select[1]/sgx-select-model', i)
        driver.execute_script(f"arguments[0]._options = {new_types['entries']}", new_types['element'])

        button = driver.find_element(By.XPATH, '//*[@id="page-container"]/template-base/div/div/section[1]/div/sgx-widgets-wrapper/widget-research-and-reports-download[1]/widget-reports-derivatives-tick-and-trade-cancellation/div/button')
        driver.execute_script('arguments[0].click()', button)

    time.sleep(10)
