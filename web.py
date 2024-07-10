import requests
from bs4 import BeautifulSoup



def arst():
  
    
  url = 'https://tr.wikipedia.org/wiki/Python '
  """ url yi alır """
  al=requests.get(url)
  """ sayfadaki içerikleri alınır """
  içerik=al.content
  b=BeautifulSoup(içerik,'html.parser')
  """ veriler çekilir """
  tür=b.find_all('p')
  for x in tür:
      
      print(x.text)


arst()