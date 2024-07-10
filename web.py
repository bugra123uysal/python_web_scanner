import requests
from bs4 import BeautifulSoup


""" yazı alma  """
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

def gor():
   uurl='https://tr.wikipedia.org/wiki/At'
   a=requests.get(uurl)
   b=a.content
   c=BeautifulSoup(b,'html.parser')

   w=c.find_all('img')
   imgurl=[img['src']for img in w if 'src' in img.attrs]

   print(imgurl)

   
gor()   


