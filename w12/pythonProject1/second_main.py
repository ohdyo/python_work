from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/s?k=fan")

names = driver.find_elements(By.CSS_SELECTOR, value='h2 a span')
prices = driver.find_elements(By.CSS_SELECTOR, value='.s-search-results .a-price-whole')

product_dict = {}

for n in range(len(prices)):
    product_dict[n] = {
        "name": names[n].text,
        "price": prices[n].text
    }


# for list in product_dict.values():
#     print(list)

print(product_dict[1])
