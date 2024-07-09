from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://janggoons.github.io/AdvancedPython/login-test/")

input_id = driver.find_element(By.NAME, value="id")
input_id.send_keys("123")

input_pw = driver.find_element(By.NAME, value="password")
input_pw.send_keys("123")

input_email = driver.find_element(By.NAME, value="email")
input_email.send_keys("123@123.com")

btn = driver.find_element(By.TAG_NAME, "button")
btn.click()