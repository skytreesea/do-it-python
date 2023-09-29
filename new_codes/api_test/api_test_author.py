# 저자정보: 기본 url = https://www.data.go.kr/iim/api/selectAPIAcountView.do
import requests 
from bs4 import BeautifulSoup

# 내 서비스키를 이용해서 만든 예제 코드 
url = 'https://apis.data.go.kr/B552540/KCIOpenApi/artiInfo/openApiM330List?serviceKey=7JlKxM7fEbOErQRa32MtR3%2Fg%2FBxi3JTPbwPfCw781Ma4uvwql5x2r2wM0Zh051RRUK%2Bw7YSwijxr0Tklej3cOg%3D%3D&recordCnt=20&pageNo=1'
 
# 일반 크롤링 코드와 유사함
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
res = requests.get(url, headers = headers)
soup = BeautifulSoup(res.text, 'lxml') 
 
# 변수가 소문자로 되어 있음
for i in soup.find_all('item'):
    # 학교명 태그 
    print(i.find('belo_insi_nm').text)
    # 이름 태그 
    print(i.find('cret_kor_nm').text)