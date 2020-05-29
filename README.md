<h1>Web_Scraping</h1>
<p>Objetivo do Repositório: colocar scripts relacionados a web scraping. Por exemplo, um deles se refere ao ZAP-Imóveis, colentando informações sobre os imóveis e um outro sobre o despacho térmico da ONS no site deles.</p>

<p> Algumas vezes o web scraping pode encontrar certas dificuldades devido a diversos fatores: bloqueio pelo servidor, 
conexão instável e etc. Por este motivo, em alguns códigos podem haver erros e pode ser preciso rodar de novo do ponto onde parou. Dessa forma tb é sugerido que seja feita
a utilização de pacotes como o tqdm para acompanhar o progresso do scraping.</p>

<p>Página de scraping do despacho térmico em <a href="http://sdro.ons.org.br/SDRO/DIARIO/index.htm">ONS</a></p>
<p>Página de scraping do <a href="https://www.zapimoveis.com.br/">ZAP-Imovéis </a></p>
<p>Página de scrpaing de <a href="https://pt.climate-data.org/">clima</a></p>

<h5>Linguagem</h5>
<p>Python 3.7</p>

<h5>Pacotes utilizados</h5>
<ul>
  <li>urllib.request</li>
  <li>BeautifulSoup (bf4)</li>
  <li>OS</li>
</ul>

<p>Futuramente o projeto vai se extender para a coleta e organização dos dados em um dataframe no Pandas.</p>

<p>Alguns links úteis</p>

<p><a href="https://www.anaconda.com/">https://www.anaconda.com/</a></p>
<p><a href="https://pypi.org/project/beautifulsoup4/">https://pypi.org/project/beautifulsoup4/</a></p>
<p><a href="https://docs.python.org/3/library/urllib.html">https://docs.python.org/3/library/urllib.html</a></p>
<p><a href="https://docs.python.org/3/library/os.html">https://docs.python.org/3/library/os.html</a></p>
<p><a href="https://pypi.org/project/tqdm/">https://pypi.org/project/tqdm/</a></p>
