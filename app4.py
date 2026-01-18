import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import requests
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

import os


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


date_new53 = str(datetime.now())
print(date_new53)
a123=time.time()


def weath():



weath()
