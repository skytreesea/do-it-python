import os, re
import pandas as pd
df2 = pd.read_csv(r'C:\Users\skytr\Documents\GitHub\do-it-python\05\survey.csv')
print(df2.head())

print(df2.describe())

print(df2['income'].sum())

print(df2['income'].median())

print(df2['sex'].value_counts())

print(df2.groupby('sex').mean())

# 싸이파이 임포트 하기 
from scipy import stats
male = df2.income[df2.sex == 'm']
female = df2.income[df2.sex == 'f']

print(stats.ttest_ind(male, female))

ttest_result = stats.ttest_ind(male, female)
if ttest_result[1] > .05:
    print('p-value는 %f로 95%% 수준에서 유의하지 않음' % ttest_result[1])
else:
    print('p-value는 %f로 95%% 수준에서 유의함' % ttest_result[1])
    
# 두 변수 간 상관관계 df2[['변수1','변수2']].corr()
print(df2[['income','jobSatisfaction']].corr()) 
# 세 변수 간 상관관계(스피어만)
print(df2[['income','jobSatisfaction','stress']].corr(method = "spearman")) 

print(df2[['income','stress']].corr()) 

# df2[['income','stress']].corr().to_csv('파일이름.csv')