from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


driver.get("http://livejournal.com/")


driver.find_element("xpath","//a[text()='Войти']").click()

time.sleep(3)

username = driver.find_element("id","user")
username.send_keys("syneltest")
password = driver.find_element("id","lj_loginwidget_password")
password.send_keys("123qweASD")
password.send_keys(Keys.RETURN)


time.sleep(3)

wait = WebDriverWait(driver, 10)
post_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span.s-header-item-post--long")))
post_button.click()


title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "textarea.text-0-2-179")))
title.send_keys("Jamshid Askarov")
title.send_keys(Keys.RETURN)

time.sleep(3)

title = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "contentEditableHelper beforeAll")))
title.send_keys("Chainsaw Man gogogogooooooooo")
title.send_keys(Keys.RETURN)