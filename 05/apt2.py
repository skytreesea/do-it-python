# 부동산실거래가 다루기 pandas  (Do it 파이썬 생활프로그래밍) 초판 2020: 192페이지
import pandas as pd
# 자신의 파일을 불러옵니다. 불러오는 방법--> 경로복사해서 따옴표 앞에 r을 붙임, 한글 포함할 경우 encoding을 지정해주어야 하는 경우가 있
df = pd.read_csv(r"C:\Users\skytr\Documents\GitHub\do-it-python\05\apt2308.csv", thousands = ',' )
print(len(df))
# df의 대략적인 정보 파악하기 
print(df.head())
print(df.tail())
#빈도분석
print(df['시군구'])
print(df['전용면적'] > 80 )
# [기존원고수정] 54
print(df[df['전용면적'] > 80] )
# 130제곱 이하 3억 이상  
print(df['단지명'][(df['전용면적'] > 130 ) & (df['거래금액'] < 30000) ])
#130제곱 이하이거나 3억 이상  
print(df['단지명'][(df['전용면적'] > 130 ) | (df['거래금액'] < 30000) ])
# result = df.groupby('구')['가격'].mean() 
print(df.loc[:10, ['단지명', '거래금액']])
#기초통계 요약: describe
print(df.loc[:, ['단지명', '거래금액']][df['거래금액'] > 100000])
df['단가'] = df['거래금액'] / df['전용면적']

print(df.loc[:10, ('거래금액', '전용면적', '단가')])
print(df.sort_values(by = '거래금액').loc[:,('거래금액','시군구')])

print(df.sort_values(by = '거래금액', ascending=False).loc[:,('거래금액','시군구')])

print(df[df['거래금액'] > 40000].sort_values(by = '전용면적').loc[:, ('거래금액', '전용면적', '시군구')])

print(df.head())

print(df['시군구'].str.contains('강릉'))

print(df[df['시군구'].str.contains('강릉') ])

dfF =df[df['시군구'].str.contains('강릉') ]

print(dfF['거래금액'].mean()) 

