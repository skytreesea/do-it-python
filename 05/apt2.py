# 부동산실거래가 다루기 pandas  (Do it 파이썬 생활프로그래밍) 초판 2020: 192페이지
import pandas as pd
# 자신의 파일을 불러옵니다. 불러오는 방법--> 경로복사해서 따옴표 앞에 r을 붙임, 한글 포함할 경우 encoding을 지정해주어야 하는 경우가 있
df = pd.read_csv(r"C:\Users\skytr\Documents\GitHub\do-it-python\05\apt201302.csv", encoding = 'cp949')
#빈도분석
frequency = df['구'].value_counts()
print(frequency)
#평균
result = df.groupby('구')['가격'].mean() 
#기초통계 요약: describe
result = df.groupby('구')['가격'].describe() 
print(result)
# 클립보드에 붙여넣기 
result.to_clipboard() 
