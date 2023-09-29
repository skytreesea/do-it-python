import requests 
from bs4 import BeautifulSoup
api_key = "7JlKxM7fEbOErQRa32MtR3%2Fg%2FBxi3JTPbwPfCw781Ma4uvwql5x2r2wM0Zh051RRUK%2Bw7YSwijxr0Tklej3cOg%3D%3D"  # 발급받은 API 키로 변경해야 합니다.
 

base_url = f"http://apis.data.go.kr/9760000/WinnerInfoInqireService2/getWinnerInfoInqire?sgId=20170509&sgTypecode=1&sdName=전국&sggName=대한민국&pageNo=1&numOfRows=10&resultType=xml&serviceKey=" + api_key 
    
# 일반 크롤링 코드와 유사함
# 변수가 소문자로 되어 있음
response = requests.get(base_url)

# BeautifulSoup을 사용한 파싱
soup = BeautifulSoup(response.text, 'html.parser')   
print(soup)