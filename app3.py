
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


options = Options()

options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')


custom_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299"
options.add_argument(f'--user-agent={custom_user_agent}')



driver = uc.Chrome(options=options, version_main=143)


import time
'''
driver = uc.Chrome(headless=True,use_subprocess=False, version_main=143)
driver.set_window_size(1800, 1000)
'''
driver.get("https://1xbet.whoscored.com/") 
time.sleep(15)
a=driver.find_element(By.TAG_NAME,'body')
print(a.text)
    
    
    

    
