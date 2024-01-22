# api 실습 파일 260
import requests
from bs4 import BeautifulSoup # 파싱하려면 BeautifulSoup를 임포트 합니다
api_key = "your_api_key"
base_url = f'http://apis.data.go.kr/9720000/searchservice/basic?serviceKey={api_key}&pageno=1&displaylines=10&search=자료명,미국'
response = requests.get(base_url)
soup = BeautifulSoup(response.text, 'lxml')
print(soup)
print(soup.find_all('item'))
# 각 item에서 name과 value를 각각 찾아봅니다
for item in soup.find_all('item'):
    print(item.find('name'), item.find('value'))
    
for item in soup.find_all('item'):
    print(item.find('name').text, item.find('value').text)
    
#각 item에서 name과 value를 각각 찾아봅니다
for item in soup.find_all('item'):
    if item.find('name').text == '저자명':
        print(item.find('value').text)
        
# 저자명과 기사명
for item in soup.find_all('item'):
    if item.find('name').text == '기사명':
        print(item.find('value').text)
    if item.find('name').text == '저자명':
        print(item.find('value').text)
        
        
total = []
each_item = [] # each_item을 반복문 밖에 써야 조건문을 지날 때 초기화되는 것을 막을 수 있습니다
# soup에서 'item' 태그를 모두 찾아서 순회하기
for item in soup.find_all('item'):
    # 'name' 태그의 텍스트가 '기사명'일 때
    if item.find('name').text == '기사명':
        # 해당 'item'에서 'value' 태그의 텍스트를 each_item에 추가하기
        each_item.append(item.find('value').text)
    # 'name' 태그의 텍스트가 '저자명'일 때
    elif item.find('name').text == '저자명':
        # 해당 'item'에서 'value' 태그의 텍스트를 each_item에 추가하기
        each_item.append(item.find('value').text)
    # each_item에 '기사명'과 '저자명' 둘 다 있을 때
    if len(each_item) == 2:
        # total 리스트에 each_item 추가하기
        total.append(each_item)
# each_item을 초기화하여 다음 '기사명'과 '저자명'을 저장할 준비 하기
        each_item = []
        
import pandas as pd
df = pd.DataFrame(total, columns=['기사명', '저자명'])
# 변환한 데이터프레임 출력하기
print(df) 