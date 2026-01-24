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
     
    
    driver.get("https://www.meteopt.com/modelos/gfs?lat=55.752&lon=37.616&lang=en")
    time.sleep(8)
    data=[]
    button = driver.find_element(By.XPATH,"/html/body/div[1]/main/section/div/div/div/div/div/div/div/div/div/div/div/span/div/div[1]/div[3]/button")
    driver.execute_script("arguments[0].click();", button)
    time.sleep(5)
    for i in range(1,129):
        e0 = driver.find_element(By.XPATH, f"/html/body/div[1]/main/section/div/div/div/div/div/div/div/div/div/div/div/span/div/div[4]/div[2]/table/tbody/tr{[i]}/td[1]")
        e=int(e0.text)
        
        e2 = driver.find_element(By.XPATH, f"/html/body/div[1]/main/section/div/div/div/div/div/div/div/div/div/div/div/span/div/div[4]/div[2]/table/tbody/tr{[i]}/td[2]")
        e20=e2.text
        e21=e20.split(', ')
        e22=e21[1]
        e23=e22.split(' ')
        e24=e23[0]
        
        e25=e23[1]
        if e25=="Jan":
            e25='01'
        if e25=="Feb":
            e25='02'
        if e25=="May":
            e25='05'
        if e25=="Jun":
            e25='06'
        if e25=="Jul":
            e25='07'
        if e25=="Aug":
            e25='08'
        if e25=="Sep":
            e25='09'
        if e25=="Oct":
            e25='10'
        if e25=="Nov":
            e25='11'
        if e25=="Dec":
            e25='12'
    
        
        e28=e23[2]
        e29=e28[:2]
        e27=e24+'-'+e25+'-'+'2025'+" "+e29+":00:00"
    
        
        e3 = driver.find_element(By.XPATH, f"/html/body/div[1]/main/section/div/div/div/div/div/div/div/div/div/div/div/span/div/div[4]/div[2]/table/tbody/tr[{i}]/td[3]")
        e30=e3.text
        e31=e30.split()
        e32=e31[0]
    
        
        e4 = driver.find_element(By.XPATH, f"/html/body/div[1]/main/section/div/div/div/div/div/div/div/div/div/div/div/span/div/div[4]/div[2]/table/tbody/tr[{i}]/td[3]/span").get_attribute('style')
        e40=e4.split('rotate(')
        e41=e40[1]
        e42=e41.split('deg);')
        e43=e42[0]
    
        
        e5 = driver.find_element(By.XPATH, f"/html/body/div[1]/main/section/div/div/div/div/div/div/div/div/div/div/div/span/div/div[4]/div[2]/table/tbody/tr[{i}]/td[4]")
        e50=e5.text
        e51=e50.split()
        e52=e51[0]
        
        e6 = driver.find_element(By.XPATH, f"/html/body/div[1]/main/section/div/div/div/div/div/div/div/div/div/div/div/span/div/div[4]/div[2]/table/tbody/tr[{i}]/td[4]/span").get_attribute('style')
        e60=e6.split('rotate(')
        e61=e60[1]
        e62=e61.split('deg);')
        e63=e62[0]
        
        e7 = driver.find_element(By.XPATH, f"/html/body/div[1]/main/section/div/div/div/div/div/div/div/div/div/div/div/span/div/div[4]/div[2]/table/tbody/tr{[i]}/td[5]")
        e8 = driver.find_element(By.XPATH, f"/html/body/div[1]/main/section/div/div/div/div/div/div/div/div/div/div/div/span/div/div[4]/div[2]/table/tbody/tr{[i]}/td[6]")
        e9 = driver.find_element(By.XPATH, f"/html/body/div[1]/main/section/div/div/div/div/div/div/div/div/div/div/div/span/div/div[4]/div[2]/table/tbody/tr{[i]}/td[7]")
        e10 = driver.find_element(By.XPATH, f"/html/body/div[1]/main/section/div/div/div/div/div/div/div/div/div/div/div/span/div/div[4]/div[2]/table/tbody/tr{[i]}/td[8]")
        e11 = driver.find_element(By.XPATH, f"/html/body/div[1]/main/section/div/div/div/div/div/div/div/div/div/div/div/span/div/div[4]/div[2]/table/tbody/tr{[i]}/td[9]")
        e12 = driver.find_element(By.XPATH, f"/html/body/div[1]/main/section/div/div/div/div/div/div/div/div/div/div/div/span/div/div[4]/div[2]/table/tbody/tr{[i]}/td[10]")
        e13 = driver.find_element(By.XPATH, f"/html/body/div[1]/main/section/div/div/div/div/div/div/div/div/div/div/div/span/div/div[4]/div[2]/table/tbody/tr{[i]}/td[11]")
        e14 = driver.find_element(By.XPATH, f"/html/body/div[1]/main/section/div/div/div/div/div/div/div/div/div/div/div/span/div/div[4]/div[2]/table/tbody/tr{[i]}/td[12]")
        e15 = driver.find_element(By.XPATH, f"/html/body/div[1]/main/section/div/div/div/div/div/div/div/div/div/div/div/span/div/div[4]/div[2]/table/tbody/tr{[i]}/td[13]")
        e16 = driver.find_element(By.XPATH, f"/html/body/div[1]/main/section/div/div/div/div/div/div/div/div/div/div/div/span/div/div[4]/div[2]/table/tbody/tr{[i]}/td[14]")
        e17 = driver.find_element(By.XPATH, f"/html/body/div[1]/main/section/div/div/div/div/div/div/div/div/div/div/div/span/div/div[4]/div[2]/table/tbody/tr{[i]}/td[15]")
        e18 = driver.find_element(By.XPATH, f"/html/body/div[1]/main/section/div/div/div/div/div/div/div/div/div/div/div/span/div/div[4]/div[2]/table/tbody/tr{[i]}/td[16]")
        e19 = driver.find_element(By.XPATH, f"/html/body/div[1]/main/section/div/div/div/div/div/div/div/div/div/div/div/span/div/div[4]/div[2]/table/tbody/tr{[i]}/td[17]")
        e200 = driver.find_element(By.XPATH, f"/html/body/div[1]/main/section/div/div/div/div/div/div/div/div/div/div/div/span/div/div[4]/div[2]/table/tbody/tr{[i]}/td[18]")
     
        data.append([e,e27,e32,e43,e52,e63,float(e7.text),float(e8.text),e9.text,float(e10.text),e11.text,e12.text,e13.text,float(e14.text),e15.text,float(e16.text),float(e17.text),float(e18.text),e19.text,e200.text])
   
       #data.append([e,e27,int(e32),int(e43),int(e52),int(e63),float(e7.text),float(e8.text),int(e9.text),float(e10.text),int(e11.text),int(e12.text),int(e13.text),float(e14.text),int(e15.text),float(e16.text),float(e17.text),float(e18.text),int(e19.text),int(e200.text)])

    header = ['Steps',
          'Date/Hour',
          'W.10m',
          'W.10m2',          
          'W.850',
          'W.8502',
          'Prec.',
          'PWAT',
          'CAPE',
          'LI',
          'Z500-1000',
          'Geop.850',
          'Geop.500',
          'T.2m',
          'RH.2m',
          'T.850',
          'T.500',
          'Pressure',
          'Clouds',
          'SnowLn']
        
    import pandas as pd
    df = pd.DataFrame(data, columns=header)
    print(df)
  
    driver.quit()
    date_new533 = str(datetime.now())
    print(date_new533)
    
    b123=time.time()
    delta1=b123-a123
    name_fun='WEATHER'
    many=0
    
    data=[]
    data.append([date_new53,date_new533,delta1,name_fun,many])
    
    
    header = ['run',
        'end',
        'delta',
        'name','many']
    df2 = pd.DataFrame(data, columns=header)
    print(df,df2)
    
    
    import gspread
    gc = gspread.service_account_from_dict(credentials)
    
    wer = gc.open("Test789").get_worksheet(6)
    wer.update([df.columns.values.tolist()]+df.values.tolist())
    
    wks2 = gc.open("Test789").get_worksheet(1)
    list_of_lists = wks2.get_all_values()
    df5 = pd.DataFrame(list_of_lists)
    new_header = df5.iloc[0]
    df5 = df5[1:]
    df5.rename(columns=new_header, inplace=True)
    df7=pd.concat([df5,df2])
    wks2.update([df7.columns.values.tolist()]+df7.values.tolist())



weath()
