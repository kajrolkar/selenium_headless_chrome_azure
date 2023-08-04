import logging
import azure.functions as func
from selenium.webdriver.common.by import By
import os, sys, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info({os.popen('./install.sh').read()})

    logging.info(f"{os.popen('dpkg -l libnss3').read()} \n {os.popen('ldconfig -p | grep libnss3').read()}")

    logging.info({os.popen('sudo cp /home/site/wwwroot/opt/chromedriver /usr/local/bin').read()})
    logging.info({os.popen('ls -l /usr/local/bin').read()})

    chrome_options = ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.binary_location = '/home/site/wwwroot/opt/chrome-linux/chrome'

    driver = webdriver.Chrome(options=chrome_options)
    href_list = []
    site = 'https://bcz-cbl.be/nl/zuivel-in-cijfers/belgische-noteringen/'
    driver.get(site)
    lnks=driver.find_elements(By.TAG_NAME, 'a')
    for lnk in lnks:
        a = lnk.get_attribute('href')
        val = href_list.append(a)
    driver.quit()
    return func.HttpResponse(f"Hello, {href_list}")
