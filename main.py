from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome()
driver.get("https://www.amazon.com/Microsoft-Lightweight-Processor-Multi-Tasking-Platinum/dp/B0B8QDBFVQ/ref=sr_1_3?crid=2NABQ1NSJTDH1&keywords=surface&qid=1698235610&sprefix=surfac%2Caps%2C270&sr=8-3&th=1")

price_whole = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_fraction = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
print(f"{price_whole.text}.{price_fraction.text}$")
#driver.close()
driver.quit() #quits all the pages