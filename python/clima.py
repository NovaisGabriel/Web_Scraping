#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import
import urllib.request
import pandas as pd
import numpy as np
import unidecode
import time

# from
from bs4 import BeautifulSoup
from tqdm import tqdm


# In[2]:


directory = "/home/novais/Desktop/Tese/dados/clima"
file = directory+"/"+"municipios.txt"
with open(file, "r") as f:
    list2 = []
    for item in f:
        list2.append(item)
raw = [x.replace('\n',"") for x in list2]
raw = [x.replace(' ',"+") for x in raw]
Mun = [unidecode.unidecode(x) for x in raw]


# In[3]:


def climaScrapper(municipio):
    # Escolhendo a URL: 
    url=r'https://pt.climate-data.org/search/?q=' + municipio

    # Configurando o request:
    user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3'
    headers = { 'User-Agent' : user_agent }
    req = urllib.request.Request(url, None, headers)
    response = urllib.request.urlopen(req)

    # Lendo a página:
    page = response.read()

    # Fechando a conexão:
    response.close()

    #Selecionando informações úteis:
    soup = BeautifulSoup(page, 'html.parser')
    try:
        data = str(soup.findAll("div", class_="data")[0]).split('\n')[1:-1]
        data = [x.replace("<span>","") for x in data]
        data = [x.replace("</span>","") for x in data]
        data = [x.replace("<div>","") for x in data]
        data = [x.replace("</div>","") for x in data]
        data = [x.replace('<span class="name">',"") for x in data]
        data = [x.replace('Clima: ',"") for x in data]
        data = [x.replace('Precipitação ',"") for x in data]
        data = [x.replace('Temperatura média: ',"") for x in data]
        data = [x.replace('°C',"") for x in data]
        data = [x.replace('mm',"") for x in data]
    except:
        data = [municipio,'NA','NA','NA','NA','NA']

    # Retornando o resultado:
    return data


# In[4]:


data = []
for i in tqdm(Mun):
    registro = climaScrapper(i)
    data.append(registro)
    rdTime = np.random.randint(3)
    time.sleep(rdTime)


# In[9]:


data_reserva = data.copy()
data_reserva


# In[10]:


for i in tqdm(Mun[1322:]):
    registro = climaScrapper(i)
    data.append(registro)
    rdTime = np.random.randint(3)
    time.sleep(rdTime)


# In[18]:


len(data)


# In[17]:


data_reserva_1 = data.copy()
data_reserva_1


# In[19]:


for i in tqdm(Mun[2646:]):
    registro = climaScrapper(i)
    data.append(registro)
    rdTime = np.random.randint(3)
    time.sleep(rdTime)


# In[22]:


data_reserva_2 = data.copy()
len(data_reserva_2)


# In[26]:


for i in tqdm(Mun[2769:]):
    registro = climaScrapper(i)
    data.append(registro)
    rdTime = np.random.randint(5)
    time.sleep(rdTime)


# In[27]:


climaData = pd.DataFrame.from_records(data)
climaData.columns = ['municipio','pais','estado','clima(Köppen e Geiger)','temperatura(°C)','precipitacao(mm)']
climaData.head()


# In[30]:


climaData


# In[28]:


len(data)


# In[32]:


climaData.to_csv('/home/novais/Desktop/Tese/dados/clima/clima_backup.csv')


# In[ ]:




