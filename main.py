from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import os
from src.url_checker import is_url_a_youtube_domain
from src.webdriver import create_driver

# TODO: get the platform (linux, window, mac) and use appropriate driver
# TODO: Check for the consent and click Rejectall button
# TODO: start the driver as headless
# TODO: add argparse functionality

url = "https://www.youtube.com/watch?v=BFsU_vOgN5c"
url = "https://www.youtube.com/@JetBrainsTV"
url = "https://www.youtube.com/watch?v=BFsc"
url = "https://www.youtube.com/"
url = "https://www.youtube.com/lksjwesldkfj-lkdsfj"

is_url_a_youtube_domain(url = url)

driver = create_driver()
driver.get(url = url)

buttons = driver.find_elements(by = By.TAG_NAME, value = 'button')

reject_button = None
pause_button = None
for button in buttons:
    if 'REJECT' in button.text.upper():
        reject_button = button

    if button.get_attribute('title') == 'Play (k)':
        pause_button = button
        
if reject_button:
    reject_button.click()
if pause_button:
    pause_button.click()

content = BeautifulSoup(driver.page_source, 'html.parser')
driver.close()

meta_elements = content.find_all('meta')
for meta_element in meta_elements:
    if meta_element.get('itemprop') == 'channelId':
        print(meta_element['content'])

link_elements = content.find_all('link')
for link_element in link_elements:
    if (link_element.get('itemprop') == 'url') & \
            ('@' in link_element.get('href', '')):
        print(link_element['href'])
    if ('alternate' in link_element.get('rel', [])) & \
            ('@' in link_element.get('href', '')):
        print(link_element['href'])

