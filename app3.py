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



def whos():
    import undetected_chromedriver as uc
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.service import Service

    service = Service()
    options = webdriver.ChromeOptions()
    

    
    driver = uc.Chrome(headless=True,use_subprocess=False,vservice=service, options=options)
    #driver = uc.Chrome()
    driver.set_window_size(1800, 1000)
    driver.get("https://1xbet.whoscored.com/") 
    time.sleep(15)
    

    


  

  

    a=driver.find_element(By.TAG_NAME,'body')
    print(a.text)
    
    
    
    
    '''
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    #driver = webdriver.Chrome(options=chrome_options)
    driver = uc.Chrome(options=chrome_options)
  
    driver.set_window_size(1800, 1000)
    driver.get("https://1xbet.whoscored.com/") 
    time.sleep(15)
    a=driver.find_element(By.TAG_NAME,'body')
    print(a.text)
  
    try:
        button = driver.find_element(By.XPATH,"/html/body/div[5]/div/div[1]/div/button5")
        driver.execute_script("arguments[0].click();", button)
    except:
        pass





    

    data2=[]
    
    
    link_preview=driver.find_elements(By.CLASS_NAME,'Match-module_previewBtn__mYHIm')
    asd=[]
    from datetime import datetime
    current_datetime = str(datetime.now())
    b=current_datetime.split("-")
    c=b[0]
    d=b[1]
    e=b[2].split(" ")
    f=e[0]
    g=e[1]
    kl=g.split(".")
    io=kl[0]
    date_new256=f+'.'+d+'.'+c
    
    data=[]
    asd5=[]
    asd2=[
    "europe-champions-league",
    "europe-europa-league",
    "europe-conference-league",
    "england-premier-league" ,
    'international-world-cup-qualification-uefa',
    "spain-laliga",
    "germany-bundesliga-",
    "france-ligue-1",
    'italy-serie-a',
    "england-league-cup",
    'england-fa-cup'
        
    ]
    
    data=[]
    
    
    for i in link_preview:
        a=i.get_attribute('href')
        for b in asd2:
            if b in a:
                asd5.append(a)
            else:
                pass
    time.sleep(2)
    for i in asd5:
        driver.get(i) 
        time.sleep(8)
    
        a1=driver.find_elements(By.CLASS_NAME,'team-link')
        
        name1=a1[0].text
        name2=a1[1].text
        try:
            a2=driver.find_element(By.CLASS_NAME,'small-display-on').find_element(By.CLASS_NAME,'gray')
            b=a2.text
            count1=int(b.count("Out"))+int(b.count("Doubtful"))*0.5
        except NoSuchElementException :
            count1=0
        try:
            a3=driver.find_element(By.CLASS_NAME,'small-display-off').find_element(By.CLASS_NAME,'gray')
            b2=a3.text
            count2=int(b2.count("Out"))+int(b2.count("Doubtful"))*0.5
        except NoSuchElementException :
            count2=0
        print(name1,count1,name2,count2)
        data.append([date_new256,name1,count1])
        data.append([date_new256,name2,count2])
        data2.append([name1,count1,name2,count2])
    driver.quit()
        
    header = ['1','2','3'] 
    df = pd.DataFrame(data, columns=header)
    header2 = ['1','2','3','4'] 
    df4 = pd.DataFrame(data2, columns=header2)
    df3 = pd.concat([df,df4])

    print(df3)
  
    date_new533 = str(datetime.now())
    print(date_new533)
    
    b123=time.time()
    delta1=b123-a123
    name_fun='Whos'
    many=0
    
    data=[]
    data.append([date_new53,date_new533,delta1,name_fun,many])
    
    
    header = ['run',
        'end',
        'delta',
        'name','many']
    df9 = pd.DataFrame(data, columns=header)
    print(df3,df9)
  
    import gspread
    gc = gspread.service_account_from_dict(credentials)
    
    wer = gc.open("Test789").get_worksheet(7)
    wer.update([df.columns.values.tolist()]+df.values.tolist())
    
    wks2 = gc.open("Test789").get_worksheet(1)
    list_of_lists = wks2.get_all_values()
    df5 = pd.DataFrame(list_of_lists)
    new_header = df5.iloc[0]
    df5 = df5[1:]
    df5.rename(columns=new_header, inplace=True)
    df7=pd.concat([df5,df9])
    wks2.update([df7.columns.values.tolist()]+df7.values.tolist())
    '''





import gspread
gc = gspread.service_account_from_dict(credentials)


wks2 = gc.open("Test789").get_worksheet(3)
list_of_lists = wks2.get_all_values()
df5 = pd.DataFrame(list_of_lists)

new_header = df5.iloc[0]  # берем первую строку как заголовок
df5 = df5[1:]
# переименовываем столбцы
df5.rename(columns=new_header, inplace=True) 
df5=df5[['col1','col2']]

df5=df5[df5['col2']=='pin']
znach=int(df5['col1'])

wks3 = gc.open("Test789").get_worksheet(4)
znach2 = int(wks3.acell('A1').value)

if znach==1:
    whos()
elif znach2==1:
    whos()
else:
    pass
    
