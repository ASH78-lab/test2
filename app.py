import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys




chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=chrome_options)




driver.set_window_size(1800, 1000)
driver.get("https://www.pinnacle.com/")
time.sleep(10)
driver.find_element(By.TAG_NAME,'body').send_keys(Keys.END)
    
time.sleep(5)
#c=driver.find_elements(By.CLASS_NAME, 'total-events')
#print(len(c))

get_title = driver.title

# Printing the title of this URL
print(get_title)
print(driver.find_element(By.TAG_NAME,'body').text)
driver.quit()







