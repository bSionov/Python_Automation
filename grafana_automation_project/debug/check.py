import time
from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 8)
driver.get("http://localhost:3000/")

time.sleep(1)
username_txt = driver.find_element(By.ID, ":r0:")
password_txt = driver.find_element(By.ID, ":r1:")
login_btn = driver.find_element(By.CSS_SELECTOR, ".css-1b7vft8-button")

username_txt.send_keys("admin")
password_txt.send_keys("admin")
login_btn.click()

time.sleep(1)
skip_btn = driver.find_element(By.CSS_SELECTOR, ".css-bhnz0e-button")
skip_btn.click()

side_menu_buttons = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".css-762eyb")))
for button in side_menu_buttons:
    if button.text == "Administration":
        print(button.text)
        button.click()
        break

admin_section = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".css-i0m3xi")))
for button in admin_section:
    ''' General
        Plugins and data
        Users and access
        Authentication '''
    print(button.text)
    if button.text == "Users and access":
        button.click()
        break
input("end")
