import os, re
import requests
from bs4 import BeautifulSoup  
os.chdir(r'C:\Users\skytr\Documents\GitHub\do-it-python\06')

article1 = 'https://v.daum.net/v/20230924051025609'
soup = BeautifulSoup(requests.get(article1).text, 'lxml')
print(soup.find_all('a'))
url='https://media.daum.net/'
# 마법의 명령어
soup = BeautifulSoup(requests.get(url).text, 'lxml')

# 특정 클래스 속성을 출력하기
print(soup.find_all('div', {"class" : "item_issue"}))

# a 태그 5개만 출력해보기
print(soup.find_all('a')[:5])

# a 태그의 링크 5개만 출력해보기
for i in soup.find_all('a')[:5]:
	print(i.get('href'))

# 특정기사 본문 저장하기 
article1 ='https://news.v.daum.net/v/20200427090630709'

# soup2 객체로 열기 
soup2 = BeautifulSoup(requests.get(article1).text, 'lxml')

# 특정기사 본문 출력하기 
for i in soup2.find_all('p'):
    print(i.text)
headline = soup.find_all('div', {"class" : "item_issue"})

# 실습 헤드라인과 기사내용 한꺼번에 추출하기
for i in headline:
    print(i.text.replace('\n',''))
    soup3 = BeautifulSoup(requests.get(i.find('a').get('href')).text, 'lxml')
    for j in soup3.find_all('p'):
        print(j.text.replace('\n',''))

    
# 'links.txt"라는 제목의 쓰기 전용 파일을 열어줍니다.  
f= open('links.txt','w')

# 링크 파일만 모으기 
for i in soup.find_all('div',{"class":"item_issue"}):
    f.write(i.find('a').get('href')+'\n' )
f.close()

# 기사 모으기
url='https://news.daum.net/'
soup2 = BeautifulSoup(requests.get(url).text, 'lxml')
f= open('article_total.txt','w')
for i in soup.find_all('div',{"class":"item_issue"}):
    try:
# 여기서 try로 예외를 지정해주는 이유는 각 명령어를 실행하다가 혹시 그 어떤 곳에서 중단되더라도 마지막까지 실행되도록 하기 위해서입니다. 
        f.write(i.text+'\n')
# 제목을 추출하는 명령어입니다. '\n'를 붙이는 이유는 제목이 끝난 후 한 줄을 띄워주기 위해서입니다. 이하 동일합니다
        f.write(i.find_all('a')[0].get('href')+ '\n')
# 각 영역(div) 안에서 'a' 태그를 추출해내고, 그 안에서 하이퍼링크('href') 주소를 얻어냅니다. 그것을 바로 파일로 저장하고, 한 칸 띄워줍니다. 
        soup2 = BeautifulSoup(requests.get(i.find('a').get('href') ).text, 'lxml')
# 위에서 얻어낸 하이퍼링크 주소로 곧바로 뷰티풀소프 객체로 다시 저장합니다. 
        for j in soup2.find_all('p'):
# 다시 문단만 추출해냅니다. 기사 본문을 모을 수 있습니다. 
            f.write(j.text)
# 추출한 문단을 파일로 저장합니다. 
    except:
        pass
# try문을 쓰면 별 다른 예외처리를 하지 않더라도 except 구문을 써야 합니다. 
f.close()
