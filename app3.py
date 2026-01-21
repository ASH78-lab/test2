
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By






driver = uc.Chrome(headless=True,use_subprocess=False, version_main=143)

driver.set_window_size(1800, 1000)
driver.get("https://1xbet.whoscored.com/") 
time.sleep(15)









a=driver.find_element(By.TAG_NAME,'body')
print(a.text)
    
    
    

    
