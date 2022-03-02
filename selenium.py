import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


s = Service('C:/Users/Legion/Desktop/Python/geckodriver-v0.30.0-win64/geckodriver.exe')
driver = webdriver.Firefox(service=s)

url = 'https://eksisozluk.com/odtu-elektrik-ve-elektronik-muhendisligi--165727?p='

page_num = 1
contents = []

while page_num <= 10:
    driver.get(url+ str(page_num))
    elements = driver.find_elements(By.CSS_SELECTOR, ".content")

    for element in elements:
        contents.append(element.text)

    time.sleep(1)
    page_num += 1

ct = 1
with open("eksi_odtu.txt",'w',encoding='utf-8') as file:
    for entry in contents:
        file.write(str(ct)+".\n" + entry + "\n")
        file.write("**************************\n")
        ct += 1

driver.close()