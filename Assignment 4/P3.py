'''Author- Akshit Monga'''

from selenium import webdriver

driver = webdriver.Chrome(executable_path="/Users/akshitmonga/WebDrivers/chromedriver")

driver.get("https://codeforces.com")

print("Title is: ",driver.title)

driver.quit()