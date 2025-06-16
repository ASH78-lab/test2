from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
#from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.core.os_manager import ChromeType

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu')
options.add_argument('--disable-extensions')
options.add_argument('--start-maximized')
# Memory optimization
options.add_argument('--disk-cache-size=1')
options.add_argument('--media-cache-size=1')
options.add_argument('--incognito')
options.add_argument('--remote-debugging-port=9222')
options.add_argument('--aggressive-cache-discard')

service = Service('/usr/local/bin/chromedriver')
    
driver = webdriver.Chrome(service=service, options=options)




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

c2=driver.find_element(By.CSS_SELECTOR, '#topContainer > div > div.RowInline-sc-415fwo-0.Row-sc-415fwo-2.Wrapper-sc-11ugq6k-1.jlqfFP.hktPYH.lblvAq > div > main > div > div > div:nth-child(3) > div > a')








