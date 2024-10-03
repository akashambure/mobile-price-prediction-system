import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service('chromedriver.exe')

driver = webdriver.Chrome(service = service)

driver.get('https://www.smartprix.com/mobiles')
time.sleep(10)

button_01 = driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/input')
button_01.click()

time.sleep(10)

button_02 = driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[2]/input')
button_02.click()

time.sleep(20)

old_height = driver.execute_script('return document.body.scrollHeight')

while True:

    load_more = driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/div[1]/div[2]/div[3]')
    load_more.click()

    time.sleep(10)

    new_height = driver.execute_script('return document.body.scrollHeight')

    if new_height == old_height:
        break

    old_height = new_height

html = driver.page_source

with open('smartprix.html','w',encoding='utf-8') as file:
    file.write(html)