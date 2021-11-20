# import libraries
import urllib.request
from decimal import Decimal

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

import time


def parse_etf_details(etf_details_url: str):
    # run firefox webdriver from executable path of your choice
    driver = webdriver.Firefox()

    # get web page
    driver.get(etf_details_url)

    # execute script to scroll down the page
    driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    res = driver.find_elements(By.CSS_SELECTOR, 'tr[class^="Table-module__row"]')

    items_fractions = dict()
    for item in res:
        name = item.find_element(By.CSS_SELECTOR, 'div[class^="StructureTableItem__name_"]').text
        item_type = item.find_element(By.CSS_SELECTOR, 'div[class^="StructureTableItem__type"]').text
        value = item.find_element(By.CSS_SELECTOR, 'div[class^="StructureTableItem__value"]').text
        items_fractions[name] = [item_type, Decimal(value.split('%')[0].replace(',', '.'))]

    time.sleep(12)
    for k, v in items_fractions.items():
        print(k, ':', v)
    driver.quit()
