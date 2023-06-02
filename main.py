# python -m pip install selenium
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://cubinez.ru/")

time.sleep(2)

# 👇️ using find_element method 👇️
search_field = driver.find_element(By.XPATH, "//*[@ decoding=\"async\"]")



driver.save_screenshot('bd.png')



time.sleep(2)

driver.close()