from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# search_tool = driver.find_element(By.CSS_SELECTOR, value="#p-search a")
# search_tool.click()

text = input('원하는 검색어를 입력해주세요 : ')

search = driver.find_element(By.NAME, value="search")
search.send_keys(text)
search.send_keys(Keys.ENTER)

text = input('글자 크기를 설정해주세요 : ')


