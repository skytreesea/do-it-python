import os, re
import requests #urllib보다 requests가 간단하고 더 범용적으로 쓰임
from bs4 import BeautifulSoup  # BeautifulSoup를 있는 그대로 씀(많은 사람들이 사용하는 방식)
os.chdir(r'C:\Users\skytr\Documents\GitHub\do-it-python\06')

url='https://media.daum.net/'
# 기본 세 줄을 붙여 넣으면 soup가 생성됩니다. 
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
res = requests.get(url, headers = headers)
soup = BeautifulSoup(res.text, 'lxml')  

# 특정 클래스 속성을 출력하기
for i in soup.find_all('div', {"class" : "cont_thumb"}):
    print(i.find('a').text)
    print(i.find('a').get('href'))
 