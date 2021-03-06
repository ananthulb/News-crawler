# -*- coding: utf-8 -*-
"""TechCruch HomePage Crawler.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UTOpdzmyXuhHubBSEA4qFxzmqv4LNbET

Techcruch page crawler

package installation and selenium configure
"""

!pip install selenium
!apt-get update # to update ubuntu to correctly run apt install
!apt install chromium-chromedriver
!cp /usr/lib/chromium-browser/chromedriver /usr/bin
!pip install beautifulsoup4!apt-get update # to update ubuntu to correctly run apt install
import sys
sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)

"""Crawling data"""

from bs4 import BeautifulSoup
driver.get("https://techcrunch.com/")
newsContent=[]
content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('article', attrs={'class':'post-block post-block--image post-block--unread'}):
  name=a.find('a', attrs={'class':'post-block__title__link'})
  description=a.find('div', attrs={'class':'post-block__content'})
  createdAt=a.find('time', attrs={'class':'river-byline__full-date-time'})
  image=a.find('img')
  newsContent.append({
      "name":name.text,
      "description":description.text,
      "image":image.attrs['src'],
      "time":createdAt.text,
      "link":"https://techcrunch.com"+name.attrs['href']
  })
print('news',newsContent)

"""For medium page crawling

"""

from bs4 import BeautifulSoup
driver.get("https://medium.com/")
newsContentMedium=[]
content = driver.page_source
soup = BeautifulSoup(content)
print('check',soup)
for a in soup.findAll('div', attrs={'class':'aj dr'}):
  pgsource=a.find('h4', attrs={'class':'ca gb ii ib jq jr js jt ju jv jw cd jx'})
  mediumTitle=a.find('h2', attrs={'class':'ca hz kv kw kx ky kz la lb lc ld le lf lg lh li lj lk ll lm ln lo jq js jt ka jv jw cd'})
  mediumDescription=a.find('h3', attrs={'class':'ca b eo cc jq jz js jt ka jv jw ij'})
  mediumCreatedAt=a.find('span', attrs={'class':'ca b ii cc ij'})
  mediumurlLink=a.find('a', attrs={'class':'bd be bf bg bh bi bj bk bl bm bn bo bp bq br'})
  mediumImage=a.find('img')
  print('check',pgsource)
  newsContentMedium.append({
      "source":pgsource.text,
      "name":mediumTitle.text,
      "description":mediumDescription.text,
      "image":mediumImage.attrs['src'],
      "time":mediumCreatedAt.text,
      "link":"https://medium.com"+mediumurlLink.attrs['href']
  })
print('news',newsContentMedium)

"""Crawler for google news technology page"""

from bs4 import BeautifulSoup
driver.get("https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGRqTVhZU0FtVnVHZ0pPV2lnQVAB?hl=en-NZ&gl=NZ&ceid=NZ:en")
newsContentGoogle=[]
content = driver.page_source
soup = BeautifulSoup(content)
# print('check',soup)
for a in soup.findAll('div', attrs={'class':'DBQmFf NclIid BL5WZb Oc0wGc xP6mwf j7vNaf'}):
  pgsource=a.find('a', attrs={'class':'wEwyrc AVN2gc uQIVzc Sksgp'})
  googleTitle=a.find('a', attrs={'class':'DY5T1d RZIKme'})
  # mediumDescription=a.find('h3', attrs={'class':'ca b eo cc jq jz js jt ka jv jw ij'})
  # mediumCreatedAt=a.find('span', attrs={'class':'ca b ii cc ij'})
  # mediumurlLink=a.find('a', attrs={'class':'bd be bf bg bh bi bj bk bl bm bn bo bp bq br'})
  googleImage=a.find('img', attrs={'class':'tvs3Id QwxBBf'})
  # print('check',mediumTitle)
  newsContentGoogle.append({
      "source":pgsource.text,
      "name":googleTitle.text,
      # "description":mediumDescription.text,
      "image":googleImage.attrs['src'],
      # "time":mediumCreatedAt.text,
      "link":"https://news.google.com"+googleTitle.attrs['href']
  })
print('news',newsContentGoogle)