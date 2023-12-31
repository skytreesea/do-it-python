import requests
from bs4 import BeautifulSoup

# 검색할 이름
search_name = '김창현'

# Google Scholar 검색 URL
url = f'https://scholar.google.com/scholar?q={search_name}'

# HTTP GET 요청을 보내고 응답을 받습니다.
response = requests.get(url)

# 응답을 파싱합니다.
soup = BeautifulSoup(response.text, 'html.parser')

# 논문 제목을 가져오기 위해 적절한 선택자를 사용합니다.
titles = soup.find_all('h3', class_='gs_rt')

# 검색 결과에서 논문 제목을 출력합니다.
for i, title in enumerate(titles, 1):
    print(f"{i}. {title.get_text()}")
