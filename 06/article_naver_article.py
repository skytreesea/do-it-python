# 네이버 경제 뉴스 크롤링 성공 코드 
import os, re
import requests #urllib보다 requests가 간단하고 더 범용적으로 쓰임
from bs4 import BeautifulSoup  # BeautifulSoup를 있는 그대로 씀(많은 사람들이 사용하는 방식)

url='https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=101'
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
for i in soup.find_all('div', {"class" : "sh_text"})[:10]:
    # 링크로 연결된 a태그의 텍스트 찾기
    url2 = i.find('a').get('href')
    print(i.find('a').text, url2)
    # 주소 얻기 
    soup2 = soupMaker(url2)
    for j in soup2.find_all('div', {"id" : "dic_area"}):
        try:
            print(j.text)
        except UnicodeEncodeError as e:
            print(f"Error encoding character: {e}")
        # 유니코드 인코드 에러는 챗GPT로 해결 
        
        
        