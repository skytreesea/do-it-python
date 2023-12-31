# 영어점수 직업만족도 회귀분석  (Do it 파이썬 생활프로그래밍) 초판 2020: 218페이지
import os, re
import numpy as np

# 데이터프레임 다루기 
import pandas as pd
# 기초 통계분석 패키지
from scipy import stats
# 그래프 그리기  
import matplotlib.pyplot as plt
#회귀분석 가능 패키지
import statsmodels.api as sm
import statsmodels.formula.api as smf

os.chdir(r'C:\Users\skytr\Documents\GitHub\do-it-python\05')

# 직업만족도
# survey 변수들:  name sex  income  English  jobSatisfaction  stress
df = pd.read_csv("survey.csv")

# 독립표본 t-검정
# 변수생성
male = df.income[df.sex == "m"] # 남성
female = df.income[df.sex == "f"] # 여성

#Levene의 등분산 검정 
l_result = stats.levene(male, female)

# 유의 수준 표시하기 
if l_result[1] > .05:
    print('P value는 %f 로 95 수준에서 유의하지 않음' % l_result[1])
else :
    print('P value는 %f 로 95 percent 수준에서 유의함' % l_result[1])

print( '남성', round(male.mean(),2), '여성',round(female.mean(),2),'\n등분산검정 결과 LeveneResult(F) : %.3f \np-value : %.3f' % (l_result)) 


# 가상의 분석자료로 회귀분석 결과 구하기(변수 2개 영어 --> 직업만족도)
model = smf.ols(formula = 'jobSatisfaction ~ English ', data = df)
# 가상의 분석자료로 회귀분석 결과 구하기 변수 3개
model = smf.ols(formula = 'jobSatisfaction ~ English + stress + income', data = df)
result = model.fit()
print(result.summary())
