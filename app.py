from datetime import datetime
current_datetime = str(datetime.now())
b=current_datetime.split("-")
c=b[0]
c=c[2:]
d=b[1]
e=b[2].split(" ")
f=e[0]
g=e[1]
kl=g.split(".")
io=kl[0]
start2=f+'/'+d+'/'+c+' '+io
start2= datetime.strptime(start2, '%d/%m/%y %H:%M:%S')
print(start2)





import os


from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=chrome_options)


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.common.exceptions import NoSuchElementException






data = [["Jun", 38.42, 1.74, -1.74],
       ["Jul", 33.26, 0.0, -9.47],
       ["Aug", 34.51, 0.0, -3.05],
       ["Sep", 36.49, 0.17, -2.49],
       ["Oct", 35.66, 0.17, -5.3],
       ["Nov", 37.96, 0.0, -2.0]]

df = pd.DataFrame(data = data, columns = ["Month", "Total", "2", "3"])


print(df)


current_datetime = str(datetime.now())
b=current_datetime.split("-")
c=b[0]
c=c[2:]
d=b[1]
e=b[2].split(" ")
f=e[0]
g=e[1]
kl=g.split(".")
io=kl[0]
start2=f+'/'+d+'/'+c+' '+io
start2= datetime.strptime(start2, '%d/%m/%y %H:%M:%S')
print(start2)

TOKEN2 = os.getenv('TOKEN2')
TOKEN1="440d864051de61f4b6463f10f8006898192b7420"
TOKEN3="ash789@avid-stone-461407-q5.iam.gserviceaccount.com"
TOKEN4 ="116197129399001621585"
TOKEN5="https://www.googleapis.com/robot/v1/metadata/x509/ash789%40avid-stone-461407-q5.iam.gserviceaccount.com"

credentials={
  "type": "service_account",
  "project_id": "avid-stone-461407-q5",
  "private_key_id": TOKEN1,
  "private_key": TOKEN2,
  "client_email": TOKEN3,
  "client_id": TOKEN4,
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": TOKEN5,
  "universe_domain": "googleapis.com"
}
import gspread
gc = gspread.service_account_from_dict(credentials)







