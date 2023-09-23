import os , requests, datetime
from bs4 import BeautifulSoup  
# 저장하고 싶은 경로를 추가합니다. (의무 아님)
# os.chdir(r'C:\Users\skytr\Documents\GitHub\do-it-python\06')
url = 'https://news.daum.net/'
f = open(str(datetime.date.today()) + '_articles.txt','w')
soup = BeautifulSoup(requests.get(url).text)
for i in soup.find_all('div',{"class":"cont_thumb"}):
    try:
        f.write(i.text+'\n')
        f.write(i.find('a').get('href') + '\n')
        soup2 = BeautifulSoup(requests.get(i.find('a').get('href')).text)
        for j in soup2.find_all('p'):
            f.write(j.text)
    except:
        pass
f.close()