# 특정 저널: 홈페이지에서 제목만 출력하기 기본예제
# Extracting the titles of articles in the main page of a journal
import os , codecs, re, datetime, requests
import urllib.request as ur
from bs4 import BeautifulSoup as bs
url = 'https://www.economist.com/'
soup=bs(ur.urlopen(url).read(),'html.parser')
for i in soup.find_all('div',{'class':'teaser__text'}):
	print(i.text)