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

time.sleep(6)

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
print(len(с))
c2=driver.find_element(By.CLASS_NAME, 'MainStyled-sc-p8mupa-1').find_elements(By.CLASS_NAME,'item')

c3=[]
c4=[]
for i in c:
    c3.append(int(i.text))
            
for i in c2:
    a=i.find_element(By.TAG_NAME,'a')

    c4.append(a.get_attribute("href"))
asd = dict(zip(c4, c3))
pot2=[]
for key, value in asd.items():
    if value >1:
        
        pot2.append(key)
    
all_pin=[]
for i in link:
    if i in pot2:
        all_pin.append(i+'#period:0')



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
date_new256=f+'.'+d+'.'+c+'  '+io


data=[]
    
for i in all_pin:
    driver.get(i) 
    time.sleep(8)
    try:
        tournemebt=driver.find_element(By.CLASS_NAME, 'breadcrumb').find_elements(By.TAG_NAME,'span')[2].text
        if "UEFA - Nations League" in tournemebt:
            tournemebt="UEFA - Nations League"
        elif "Regions Path" in tournemebt:
            tournemebt="Russia - Cup"
        elif "Spain - Super Cup" in tournemebt:
            tournemebt="Spain - Copa del Rey"
        elif "Italy - Super Cup" in tournemebt:
            tournemebt="Italy - Cup"
        elif "England - FA Cup" in tournemebt:
            tournemebt="England - EFL Cup"
        rd=driver.find_elements(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div/main/div/div/div')
        er=len(rd)+1
        
        import time
        from datetime import datetime
        from selenium.common.exceptions import NoSuchElementException

        ert11=date_new256
        for i in range(3,er):
            
            try:
                ert=driver.find_element(By.XPATH,f'/html/body/div[1]/div/div/div/div[1]/div/main/div/div/div[{i}]').text
                if ', 2025' in ert or 'TOMORROW' in ert or 'TODAY' in ert:
                    ert2='-'
                    ert3='-'
                    ert4='-'
                    ert5='-'
                    ert6='-'
                    ert7='-'
                    ert8='-'
                    ert9='-'
                    ert10='-'
        
                    current_datetime = str(datetime.now())
                    b=current_datetime.split("-")
                    cee=b[0]
                    d=b[1]
                    e=b[2].split(" ")
                    f=e[0]
                    date_new=f+'.'+d+'.'+cee
                    f2=str(int(f)+1)
                    date_new2=f2+'.'+d+'.'+cee
                    
                    if "TODAY" in ert:
                    
                
                        ert=date_new
                    elif "TOMORROW" in ert:
                    
                
                        ert=date_new2
                    else:
                        ert=driver.find_element(By.XPATH,f'/html/body/div[1]/div/div/div/div[1]/div/main/div/div/div[{i}]').text
                        ert=ert.split(", ")
                        b255=ert[1].split(" ")
                        c255=b255[1]
                        date1=c255+'.'+'09'+'.'+ert[2]
                        r255=b255[0]
                        if r255=="SEP":
                            u5o255="09"
                        elif r255=="OCT":
                            u5o255="10"
                        elif r255=="NOV":
                            u5o255="11"
                        elif r255=="DEC":
                            u5o255="12"
                        elif r255=="JAN":
                            u5o255="01"
                        elif r255=="FEB":
                            u5o255="02"
                        elif r255=="MAR":
                            u5o255="03"
                        elif r255=="APR":
                            u5o255="04"   
                        elif r255=="MAY":
                            u5o255="05" 
                        elif r255=="JUN":
                            u5o255="06" 
                        elif r255=="JUL":
                            u5o255="07" 
                        elif r255=="AUG":
                            u5o255="08" 

                            
                        ert=c255+'.'+u5o255+'.'+ert[2]
        
                    ert01=ert
                    data.append([ert,ert2,tournemebt,ert3,ert4,ert5,ert6,ert7,ert8,ert9,ert10,ert11])
                            
        
        
                    
                
                else:
                    rd5=driver.find_elements(By.XPATH,f'/html/body/div[1]/div/div/div/div[1]/div/main/div/div/div[{i}]/div/div/div')
                                                        
        
                    er5=len(rd5)-1
        
                    for z in range(0,er5):
                        b=z+2
                        ert2=driver.find_element(By.XPATH,f'/html/body/div[1]/div/div/div/div[1]/div/main/div/div/div[{i}]/div/div/div[{b}]/div[1]/div/a/div/div').text
                        a=ert2.split(' (Match)\n')
                        ert2=a[2]
                        ert3=a[0]
                        ert4=a[1]
                        
                        ert5=driver.find_element(By.XPATH,f'/html/body/div[1]/div/div/div/div[1]/div/main/div/div/div[{i}]/div/div/div[{b}]/div[2]/div[1]/button').text
                        ert6=driver.find_element(By.XPATH,f'/html/body/div[1]/div/div/div/div[1]/div/main/div/div/div[{i}]/div/div/div[{b}]/div[2]/div[2]/button').text
                        ert7=driver.find_element(By.XPATH,f'/html/body/div[1]/div/div/div/div[1]/div/main/div/div/div[{i}]/div/div/div[{b}]/div[2]/div[3]/button').text
                        
                        ert8=driver.find_element(By.XPATH,f'/html/body/div[1]/div/div/div/div[1]/div/main/div/div/div[{i}]/div/div/div[{b}]/div[3]/div[1]/button/span[1]').text
                        ert9=driver.find_element(By.XPATH,f'/html/body/div[1]/div/div/div/div[1]/div/main/div/div/div[{i}]/div/div/div[{b}]/div[3]/div[1]/button/span[2]').text
                        ert10=driver.find_element(By.XPATH,f'/html/body/div[1]/div/div/div/div[1]/div/main/div/div/div[{i}]/div/div/div[{b}]/div[3]/div[2]/button/span[2]').text
                        try:
                            ert5=float(ert5)
                        except ValueError:
                            ert5='-'
                            
                        try:
                            ert6=float(ert6)
                        except ValueError:
                            ert6='-'
                            
                        try:
                            ert7=float(ert7)
                        except ValueError:
                            ert7='-'
                        
                        
                        ert8=float(ert8)
                        ert9=float(ert9)
                        ert10=float(ert10)
        
                        
        
                        
            
                        data.append([ert01,ert2,tournemebt,ert3,ert4,ert5,ert6,ert7,ert8,ert9,ert10,ert11])
                    
                    
                
            except NoSuchElementException:
                pass
    except NoSuchElementException:
        pass
    
        


header = ['date','time','league','Столбец3',
'Столбец4',
'1',
'X',
'2',
'handicap',
'H',
'A',
'Столбец11'
            ]
df = pd.DataFrame(data, columns=header)
df = df.loc[df['1'] != '-']

date_new533 = str(datetime.now())
print(date_new533)

b123=time.time()
delta1=b123-a123
name_fun='Pinnacle'
data=[]
data.append([date_new53,date_new533,delta1,name_fun])


header = ['run',
    'end',
    'delta',
    'name']
df2 = pd.DataFrame(data, columns=header)
print(df,df2)

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

wer = gc.open("Test789").sheet1
wer.update([df.columns.values.tolist()]+df.values.tolist())
wer2 = gc.open("Test789").sheet2
wer2.update([df.columns.values.tolist()]+df.values.tolist())






