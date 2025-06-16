import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
from selenium.webdriver.common.keys import Keys

from datetime import datetime
import os
date_new53 = str(datetime.now())
print(date_new53)
a123=time.time()




chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=chrome_options)




driver.set_window_size(1800, 1300)


driver.get("https://www.pin880.com/en/standard/soccer/leagues")



time.sleep(10)


driver.find_element(By.TAG_NAME,'body').send_keys(Keys.END)

time.sleep(10)

link=[
'https://www.pin880.com/en/standard/soccer/england-efl-cup',
'https://www.pin880.com/en/standard/soccer/england-fa-cup',
'https://www.pin880.com/en/standard/soccer/england-premier-league',
'https://www.pin880.com/en/standard/soccer/england-community-shield',
'https://www.pin880.com/en/standard/soccer/england-championship',
'https://www.pin880.com/en/standard/soccer/france-cup',
'https://www.pin880.com/en/standard/soccer/france-ligue-1',
'https://www.pin880.com/en/standard/soccer/2a',
'https://www.pin880.com/en/standard/soccer/germany-bundesliga',
'https://www.pin880.com/en/standard/soccer/germany-cup',
'https://www.pin880.com/en/standard/soccer/germany-super-cup',
'https://www.pin880.com/en/standard/soccer/germany-bundesliga-2',
'https://www.pin880.com/en/standard/soccer/italy-cup',
'https://www.pin880.com/en/standard/soccer/italy-serie-a',
'https://www.pin880.com/en/standard/soccer/italy-super-cup',
'https://www.pin880.com/en/standard/soccer/spain-copa-del-rey',
'https://www.pin880.com/en/standard/soccer/spain-la-liga',
'https://www.pin880.com/en/standard/soccer/spain-super-cup',
'https://www.pin880.com/en/standard/soccer/russia-cup',
'https://www.pin880.com/en/standard/soccer/russia-premier-league',
'https://www.pin880.com/en/standard/soccer/russia-super-cup',
'https://www.pin880.com/en/standard/soccer/russia-first-league',
'https://www.pin880.com/en/standard/soccer/uefa-champions-league',
'https://www.pin880.com/en/standard/soccer/uefa-europa-league',
'https://www.pin880.com/en/standard/soccer/uefa-conference-league',
'https://www.pin880.com/en/standard/soccer/uefa-euro-qualifiers',
'https://www.pin880.com/en/standard/soccer/uefa-euro',
'https://www.pin880.com/en/standard/soccer/uefa-super-cup',
'https://www.pin880.com/en/standard/soccer/uefa-nations-league-a',
'https://www.pin880.com/en/standard/soccer/uefa-nations-league-b',
'https://www.pin880.com/en/standard/soccer/uefa-nations-league-c',
'https://www.pin880.com/en/standard/soccer/uefa-nations-league-d',
'https://www.pin880.com/en/standard/soccer/uefa-nations-league-playoffs',
'https://www.pin880.com/en/standard/soccer/fifa-world-cup-qualifiers-europe',
'https://www.pin880.com/en/standard/soccer/international-friendlies'
    
]

c=driver.find_elements(By.CLASS_NAME, 'total-events')

c2=driver.find_element(By.CLASS_NAME, 'MainStyled-sc-p8mupa-1').find_elements(By.CLASS_NAME,'item')








