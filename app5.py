import pandas as pd
import time
from datetime import datetime
import requests
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












def asi78():

    from bs4 import BeautifulSoup
    headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            "Referer": "https://www.google.com/",
            "Connection": "keep-alive",
        }

    
   
    URL = 'https://tipsters.asianbookie.com/?classic=1'
    req = requests.get(URL, headers=headers, timeout=10)
    print(req.status_code)
    
    src = req.text
    soup = BeautifulSoup(src, 'lxml')
    all_products_hrefs = soup.find(class_='showAll').find_all('a')
    len(all_products_hrefs)
    #for i in all_products_hrefs:
    #    print(i.get('href'))
    #------------------------------------------------------------------------------------------  
    all_products_hrefs = soup.find(class_='showAll').find_all('font',color="white",size="3")
    len(all_products_hrefs)
    #for i in all_products_hrefs:
        #print(i.text)
    #-------------------------------------------------------------------------------------------  
    tyu = soup.find(class_='showAll').find_all('td',colspan="9")
    c=len(tyu)
    
    ert=[]
    
    for i in range(1,c):
        b="Settlement for above matches will"
        if b in tyu[i].text:
            ert.append(i)
    
    #---------------------------------------------------------------------------------------------
    ll_products_hrefs = soup.find(class_='showAll').find_all('font',color="white",size="3")
    
    
    
    h=ert[0]
    
    sdf=[]
    for i in range(1,h+1):
        a=i*8-6
        sdf.append(a)
    sdf[0:h]
    
    all_products_hrefs = soup.find(class_='showAll').find_all('a')
    ght=[]
    for i in all_products_hrefs:
        ght.append(i.get('href'))
    
    yut=[]
    for i in sdf:
        yut.append('https://tipsters.asianbookie.com'+ ght[i])
    
    dfg=[]
        
    for i in yut:
        URL = i
        req = requests.get(URL, headers=headers)
        src = req.text
        soup = BeautifulSoup(src, 'lxml')
        all_products_hrefs1 = soup.find_all('b')[1]
        all_products_hrefs2 = soup.find_all('b')[2]
        all_products_hrefs3 = soup.find_all('b')[4]
        all_products_hrefs4 = soup.find_all('b')[5]
        
        wer=int(all_products_hrefs3.text)/(int(all_products_hrefs3.text)+int(all_products_hrefs4.text))
        wed=1-wer
        
        dfg.append(f'{all_products_hrefs1.text} {all_products_hrefs2.text}/{wer}/{wed}')
    
    
    l_products_hrefs=[]
    for i in ll_products_hrefs:
        l_products_hrefs.append(i.text)
        
    l_products_hrefs2=l_products_hrefs[:h]
    slovar2= dict(zip(dfg,l_products_hrefs2))
    slovar2
    
    asd=[
        'English FA Cup',
        'Spanish Cup',
        'Spanish La Liga',
        'French Ligue 1',
        'German Bundesliga',
        'Italian Serie A ',
        'English Premier League',
        'German Cup' ,
        'Italian Cup',
        "UEFA Champions League",
        "UEFA Europa League",
    "UEFA Conference League",
    "English League Cup",
    'European Championships',
        'Misc'
    
        
    ]
    
    data=[]
    for i,b in slovar2.items():
        if b in asd:
            data.append(i)
        else:
            pass
        
        
        
    import pandas as pd
    header = ['0'] 
    df = pd.DataFrame(data, columns=header)
    df[['part1', 'part2', 'part3']] = df['0'].str.split('/', expand=True)
    
    del df['0']
    cols = ['part2', 'part3']
    df[cols] = df[cols].astype(float)
    df['max'] = df[cols].max(axis=1)
    df = df.sort_values('max', ascending=False)
    print(df)
  
    date_new533 = str(datetime.now())
    print(date_new533)
    
    b123=time.time()
    delta1=b123-a123
    name_fun='asi78'
    
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
    
    wer = gc.open("Test789").sheet8
    wer.clear()
    wer.update([df.columns.values.tolist()]+df.values.tolist())
    
    wks2 = gc.open("Test789").get_worksheet(1)
    list_of_lists = wks2.get_all_values()
    df5 = pd.DataFrame(list_of_lists)
    new_header = df5.iloc[0]
    df5 = df5[1:]
    df5.rename(columns=new_header, inplace=True)
    df7=pd.concat([df5,df2])
    wks2.update([df7.columns.values.tolist()]+df7.values.tolist())


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


asi78()
