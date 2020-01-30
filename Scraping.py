
# Importando pacotes
# Import
import urllib.request
import numpy as np
import pandas as pd
import ast
import json as js
import re

# From packages
from bs4 import BeautifulSoup as bf4

# Obtenção de dados do ZAP
def find_substring(substring, string):
    indices = []
    index = -1  # Begin at -1 so index + 1 is 0
    while True:
        # Find next index of substring, by starting search from index + 1
        index = string.find(substring, index + 1)
        if index == -1:  
            break  # All occurrences have been found
        indices.append(index)
    return indices

#Url's de destino:
url_principal = 'https://www.zapimoveis.com.br/venda/apartamentos/rj+rio-de-janeiro/'

url_seletor = '#{"precomaximo":"2147483647","parametrosautosuggest":[{"Bairro":"","Zona":"","Cidade":"RIO%20DE%20JANEIRO","Agrupamento":"","Estado":"RJ"}],"pagina":'

url_final=',"ordem":"Valor","paginaOrigem":"ResultadoBusca","semente":"702111458","formato":"Lista"}'


def searchPrice(url_principal,url_seletor,url_final,pgs):
    for k in range(0,pgs):
        #vetor para guardar dados:
        p=[]
        url_pag = str(pgs)
        url = url_principal + url_seletor + url_pag + url_final

        req = urllib.request.Request(
            url, 
            data=None, 
            headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
            }
        )

        f = urllib.request.urlopen(req)
        content = bf4(f.read())
        content=str(content)
        positionI = find_substring('<div class="simple-card__prices simple-card__listing-prices"><p class="simple-card__price js-price heading-regular heading-regular__bolder align-left">',content)

        j=0
        while (j<len(positionI)):
            inicio = positionI[j]+156
            fim = inicio+12
            preco_j = content[inicio:fim]
            p.append(preco_j)
            j=j+1
    return p

ans = searchPrice(url_principal,url_seletor,url_final,2)
print(ans)



