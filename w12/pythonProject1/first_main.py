from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/Dreo-Velocity-Oscillating-Bladeless-DR-HTF007/dp/B09MKPDJRT/")

dollar = driver.find_element(By.XPATH,
                             value='//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]/span[2]/span[2]')
dent = driver.find_element(By.XPATH,
                           value='//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]/span[2]/span[3]')

stars = driver.find_element(By.XPATH,
                           value='//*[@id="acrPopover"]/span[1]/a/span')
print(f"The stars of his product is {stars.text}")
print(f"The dollar is {dollar.text}")
print(f"The dent is {dent.text}")

