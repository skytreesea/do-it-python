# 부동산실거래가 다루기 pandas  (Do it 파이썬 생활프로그래밍) 초판 2020: 192페이지

import pandas as pd
import re, os
# 자신의 파일을 불러옵니다. 
os.chdir(r'C:\Users\skytr\Documents\GitHub\do-it-python\05')
df = pd.read_csv("apt201302.csv", encoding = 'cp949')
result = df.groupby('단지명')['단가'].mean() 
result.to_clipboard()