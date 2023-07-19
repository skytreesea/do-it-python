import os, re
import requests #urllib보다 requests가 간단하고 더 범용적으로 쓰임
from bs4 import BeautifulSoup  # BeautifulSoup를 있는 그대로 씀(많은 사람들이 사용하는 방식)

url='https://v.daum.net/v/20230720000056433'
# 기본 세 줄을 붙여 넣으면 soup가 생성됩니다. 
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
res = requests.get(url, headers = headers)
soup = BeautifulSoup(res.text, 'lxml')  

#def로 url을 입력하면 soup를 생성하는 함수 만들기 
def soupMaker(url):
    headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
    res = requests.get(url, headers = headers)
    return BeautifulSoup(res.text, 'lxml') 
    
soup = soupMaker(url)

# 특정 클래스 속성을 출력하기
for i in soup.find_all('p'):
    try:
        print(i.text)
    except UnicodeEncodeError as e:
        print(f"Error encoding character: {e}")
        # 유니코드 인코드 에러는 챗GPT로 해결 