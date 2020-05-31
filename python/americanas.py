# import
import urllib.request
import pandas as pd
import numpy as np

# from
from bs4 import BeautifulSoup
from tqdm import tqdm

url='https://www.americanas.com.br/categoria/celulares-e-smartphones/m/samsung'

# Configurando o request:
user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3'
headers = { 'User-Agent' : user_agent }
req = urllib.request.Request(url, None, headers)
response = urllib.request.urlopen(req)

# Lendo a página:
page = response.read()

# Fechando a conexão:
response.close()

soup = BeautifulSoup(page, 'html.parser')

x = soup.findAll("span", class_="PriceUI-bwhjk3-11 cmTHwB PriceUI-sc-1q8ynzz-0 dHyYVS TextUI-sc-12tokcy-0 bLZSPZ")

print(len(x))


# print(soup)

# PriceUI-bwhjk3-11 cmTHwB PriceUI-sc-1q8ynzz-0 dHyYVS TextUI-sc-12tokcy-0 bLZSPZ
