# 부동산실거래가 다루기 pandas  (Do it 파이썬 생활프로그래밍) 초판 2020: 192페이지

import pandas as pd
import re, os
# 자신의 파일을 불러옵니다. 
os.chdir(r'J:\one-drive 20200728\MyScript\python\final_git_hub')
df = pd.read_csv("apt.csv", encoding = 'cp949')

# idle에서는 print를 붙이지 않아도 출력되지만, 프로그램에서는 print를 붙여주지 않으면 화면상에 아무런 결과물이 나타나지 않기 때문에 책과 다르게 print 명령어를 해주었습니다. 
# 자료 수 
print(len(df))

# 자료 파악하기
print(df.head())
print(df.tail())

# 특정 열 출력하기 
print(df.지역)
# 면적 130㎡이상, 가격이 1억5천만원 미만인 아파트 단지명 출력하기
print(df.아파트[(df.면적 > 130) | (df.가격 < 15000)])

#4억 원 이상의 가격으로 거래된 아파트
print(df.loc[:, ['아파트', '가격']] [df.가격 > 40000])
# 단가 구하기, 미립자 꿀팁, 판다스 활용할 때 df.가격 과 df['가격']이 거의 똑같은 의미를 가지지만 새로운 열을 생성할 때 df.가격 과 같은 형태로 생성하면 오류가 난다. 
# 아래와 같이 df['단가']라고 해야 새로운 열을 만들 수 있음: 책에는 이런 형태로 새로운 열을 만들었지만, df.단가 라고 하면 오류가 나온다는 말이 없음.  

df['단가']= df.가격/df.면적
# 가격 면적 단가 10개 출력해보기
print(df.loc[:10, ('가격', '면적', '단가')])
# 가격 오름차순 정렬하기
print(df.sort_values(by='가격').loc[:,('가격','지역')])
# 25억 넘는 아파트만 출력하기
print(df[df.가격 > 250000].sort_values(by = '계약일').loc[:,('가격','면적','계약일')])

# 강릉 아파트만 출력
print(df[df.지역.str.find('강릉') > -1])
# 강릉 아파트만 출력하여 각 변수 평균 출력
dfF = df[df.지역.str.find('강릉') > -1]
print(dfF.mean())

