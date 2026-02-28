
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


options = Options()

options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')






driver = uc.Chrome(options=options, version_main=145)


import time


driver.get("https://www.whoscored.com/") 
time.sleep(15)
a=driver.find_element(By.TAG_NAME,'body')
print(a.text)
    
    
    

    
