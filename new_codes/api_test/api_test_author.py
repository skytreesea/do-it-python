# 이 코드는 책에 들어갈 정도로 성공한 코드입니다. api_key는 본인의 키를 활용하세요.
import requests 
from bs4 import BeautifulSoup

api_key = 'your_key'
# 내 서비스키를 이용해서 만든 예제 코드 
base_url = f'http://apis.data.go.kr/9720000/searchservice/basic?serviceKey={api_key}&pageno=1&displaylines=10&search=자료명,미국'
 
# 일반 크롤링 코드와 유사합니다. 
response = requests.get(base_url) 
print(response)
soup = BeautifulSoup(response.text, 'lxml') 

# soup를 출력합니다. 
print(soup.find_all('item'))

# 각 item에서 name과 value를 각각 찾아봅니다. 
for item in soup.find_all('item'):
    print(item.find('name'), item.find('value'))
     
# 기사명만 찾기
for item in soup.find_all('item'):
    if item.find('name').text == '기사명':
        print(item.find('value').text)
     
# 저자명과 기사명 
for item in soup.find_all('item'):
    if item.find('name').text == '기사명':
        print(item.find('value').text)
    if item.find('name').text == '저자명':
        print(item.find('value').text)