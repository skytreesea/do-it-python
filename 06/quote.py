# 명언 수집  (Do it 파이썬 생활프로그래밍) 초판 2020: 218페이지
import os , re, usecsv
import requests 

from bs4 import BeautifulSoup  
url = 'http://quotes.toscrape.com/' 
html = requests.get(url)
soup = BeautifulSoup(html.text, 'lxml')
# 책에서 마법의 명령어라고 부르는 것
soup = BeautifulSoup(requests.get(url).text, 'lxml')
soup = BeautifulSoup(requests.get('http://quotes.toscrape.com/' ).text, 'lxml')
#명언 하나만 가져오기
print(soup.find_all('span',{'class':'text'}))
quote = soup.find_all('span',{'class':'text'})
# 첫번째 인용구만 출력하기
print(quote[0].text) 

# 해당 페이지의 명언 모두 출력하기
for i in soup.find_all('div',{"class":"quote"}):
	print(i.text)
 