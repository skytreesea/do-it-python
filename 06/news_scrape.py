import os  # 운영 체제와 상호 작용하기 위한 모듈을 가져옵니다.
import requests  # HTTP 요청을 보내기 위한 모듈을 가져옵니다.
from bs4 import BeautifulSoup  # HTML 파싱을 위한 BeautifulSoup 모듈을 가져옵니다.

# 다음 뉴스 메인 페이지 URL을 설정합니다.
main_url = 'https://news.daum.net/'

# HTTP 요청 헤더를 설정하여 서버에 브라우저 정보를 전달합니다.
headers = {'User-Agent': 'Mozilla/5.0'}

# HTTP GET 요청을 보내고 응답을 받습니다.
response = requests.get(main_url, headers=headers)
if response.status_code == 200:  # 응답 코드가 200(성공)인지 확인합니다.
    # 응답 본문을 HTML 파서로 파싱하여 BeautifulSoup 객체를 생성합니다.
    soup = BeautifulSoup(response.text, 'html.parser')
else:
    # 요청이 실패한 경우 에러 메시지를 출력하고 프로그램을 종료합니다.
    print(f"Failed to fetch the URL: {main_url}")
    exit()

# 주요 기사 링크를 저장할 리스트를 초기화합니다.
article_links = []
# 'https://v.daum.net/v/'로 시작하는 모든 링크를 선택합니다.
for link in soup.select('a[href^="https://v.daum.net/v/"]'):
    href = link.get('href')  # 링크의 href 속성을 가져옵니다.
    if href not in article_links:  # 중복된 링크가 아닌 경우
        article_links.append(href)  # 리스트에 추가합니다.

# 주어진 URL에서 기사 제목과 본문을 추출하는 함수를 정의합니다.
def extract_article(url):
    response = requests.get(url, headers=headers)  # 기사 페이지에 HTTP GET 요청을 보냅니다.
    if response.status_code == 200:  # 응답 코드가 200(성공)인지 확인합니다.
        # 응답 본문을 HTML 파서로 파싱하여 BeautifulSoup 객체를 생성합니다.
        article_soup = BeautifulSoup(response.text, 'html.parser')
        title = article_soup.find('h3')  # <h3> 태그에서 제목을 찾습니다.
        content = article_soup.find_all('p')  # 모든 <p> 태그에서 본문을 찾습니다.
        return {
            'title': title.text.strip() if title else 'No Title',  # 제목이 있으면 텍스트를 반환하고, 없으면 'No Title'을 반환합니다.
            'content': '\n'.join([p.text.strip() for p in content]) if content else 'No Content'  # 본문이 있으면 각 <p> 태그의 텍스트를 합쳐서 반환하고, 없으면 'No Content'를 반환합니다.
        }
    else:
        # 요청이 실패한 경우 에러 메시지를 출력하고 None을 반환합니다.
        print(f"Failed to fetch the article URL: {url}")
        return None

# 기사 정보를 저장할 리스트를 초기화합니다.
articles = []
# 추출한 각 기사 링크에 대해 반복합니다.
for link in article_links:
    article = extract_article(link)  # 기사 정보를 추출합니다.
    if article:  # 유효한 기사 정보인 경우
        articles.append(article)  # 리스트에 추가합니다.

# 결과를 저장할 파일 경로를 설정합니다.(앞에 r을 붙이고 주소를 가져와 붙여 주세요.)
output_file = r'C:\Users\ERC\Documents\GitHub\PythonBasic\crawling\newstotal_article.txt'
try:
    # 파일을 쓰기 모드로 열고 인코딩을 설정합니다.
    with open(output_file, 'w', encoding='utf-8') as f:
        # 각 기사에 대해 제목과 본문을 파일에 씁니다.
        for article in articles:
            f.write(f"Title:\n{article['title']}\n\n")  # 제목을 씁니다.
            f.write(f"Content:\n{article['content']}\n")  # 본문을 씁니다.
            f.write("="*80 + "\n")  # 구분선을 추가합니다.
    # 저장이 완료되면 성공 메시지를 출력합니다.
    print(f"\nArticles saved to {output_file}")
except Exception as e:
    # 파일 저장 중 에러가 발생하면 에러 메시지를 출력합니다.
    print(f"Error saving articles to file: {e}")
