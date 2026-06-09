
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


options = Options()

options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')






driver = uc.Chrome(options=options, version_main=145)


import time


driver.get("https://www.crimsonhaven46.xyz/en/standard/soccer/fifa-world-cup#period:0") 
time.sleep(15)
a=driver.find_element(By.TAG_NAME,'body')
print(a.text)
    
    
    

    
