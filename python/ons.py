#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import urllib.request
import os


# In[2]:


for ano in [2015,2016,2017]:
    for mes in range(1,13):
        for dia in range(1,32):
            try:
                date1 = str(ano)+"_"+str("{:02d}".format(mes))+"_"+str("{:02d}".format(dia))
                date2 = str("{:02d}".format(dia))+"-"+str("{:02d}".format(mes))+"-"+str(ano)
                link = "http://sdro.ons.org.br/boletim_diario/"+date1+"/despacho_termico_arquivos/sheet001.htm"
                file_name = date2+".xlsx"
                response = urllib.request.urlretrieve(link,file_name)
                
                if not os.path.isdir(f'./arquivos/{ano}'):
                    os.system(f'mkdir ./arquivos/{ano}')
                os.system(f'mv {file_name} ./arquivos/{ano}')
            except:
                pass


# In[ ]:


for ano in [2017,2018,2019,2020]:
    for mes in range(1,13):
        for dia in range(1,32):
            try:
                date1 = str(ano)+"_"+str("{:02d}".format(mes))+"_"+str("{:02d}".format(dia))
                date2 = str("{:02d}".format(dia))+"-"+str("{:02d}".format(mes))+"-"+str(ano)
                link = "http://sdro.ons.org.br/SDRO/DIARIO/"+date1+"/HTML/12_MotivoDespachoTermico_"+date2+".xlsx"
                file_name = date2+".xlsx"
                response = urllib.request.urlretrieve(link,file_name)
                
                if not os.path.isdir(f'./arquivos/{ano}'):
                    os.system(f'mkdir ./arquivos/{ano}')
                os.system(f'mv {file_name} ./arquivos/{ano}')
            except:
                pass


# In[ ]:




