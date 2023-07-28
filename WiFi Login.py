from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as ec
import time

link = 'http://192.168.2.190/userlogin/index.html'
username = input('Enter username: ')
password = input('Enter password: ')

while True:
    brw = webdriver.Chrome()
    brw.get(link)
    time.sleep(1)

    field = '//*[@id="user"]'
    wdw(brw, timeout=10*1000).until(ec.visibility_of_element_located((By.XPATH, field)))
    brw.find_element(By.XPATH, field).send_keys(username)

    field = '//*[@id="passwd"]'
    wdw(brw, timeout=10*1000).until(ec.visibility_of_element_located((By.XPATH, field)))
    brw.find_element(By.XPATH, field).send_keys(password)

    button = '//*[@id="submitbtn"]'
    wdw(brw, timeout=10*1000).until(ec.visibility_of_element_located((By.XPATH, button)))
    brw.find_element(By.XPATH, button).click()

    brw.quit()
    time.sleep(300)
    
