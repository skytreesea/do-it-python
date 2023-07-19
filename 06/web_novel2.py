#기본: 네이버 크롤링 웹소설 100위 제목 모으기 
from bs4 import BeautifulSoup
import requests,re
url = ('https://series.naver.com/novel/top100List.series')

headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
res = requests.get(url, headers = headers)
soup = BeautifulSoup(res.text, 'lxml')  

 
 # 시리즈 웹소설 제목 크롤링 성공
for i in soup.find_all('div', {'class':'comic_cont'}):
    for j in i.find_all('a'):
        print(j.text)