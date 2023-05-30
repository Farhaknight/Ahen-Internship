from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome()
time.sleep(2)

driver.get("https://www.instagram.com/")
time.sleep(3)

username = driver.find_element(by="name", value="username")
password = driver.find_element(by="name", value="password")

username.clear()
password.clear()

username.send_keys("farhaknight")
password.send_keys("Farhanattar@1234")
password.send_keys(Keys.RETURN)
time.sleep(5)

try:
    notnow = driver.find_elements(By.TAG_NAME, "button")[1]
    if notnow.text == "Not Now":
        notnow.click()
        time.sleep(2)
except:
    print('Error')
    
driver.find_element(By.CLASS_NAME, value="_a9-z").click()
time.sleep(2)

posts = driver.find_elements(By.TAG_NAME, value="article")
print(len(posts))
for post in posts:
    post.find_elements(By.CLASS_NAME, "_abl-")[1].click()
    time.sleep(2)

driver.execute_script("window.scrollTo(0,10000)")
time.sleep(4)

posts = driver.find_elements(By.TAG_NAME, value="article")
print(len(posts))
for post in posts:
    try:
        post.find_elements(By.CLASS_NAME, "_abl-")[1].click()
        time.sleep(2)
    except:
        print('Done')
        break