##### 새기업 설립 시 타당성 조사를 위한 경상수지 비교 기본 프로그램 #######
import pandas
# 환경 데이터로 바로 결과값 도출하도록 함(순서: 현행 수입, 인건비, 운영비, 공단방식 수입, 인건비, 운영비 순으로 입력)
env_data = [0,40144,461034,736255,356785,777226]

#usecsv의 값을 저장하도록 함 
import csv, os
import numpy as np
def writecsv(filename, the_list):
    with open(filename,'w',newline='') as f:
        a=csv.writer(f, delimiter=',')
        a.writerows(the_list)
# 현행방식과 공기업 방식의 인플레이션 인덱스 부여
# 물가상승률
price_index = .011
# 인건비 상승률
salary_increase = 0.0414
# 새 회사의 인건비 상승률 
salary_increase_new_company = 0.0371
# 수입증가율
income_increase = .011
start_year = 2022
# 분석기간(년도)
num_years = 5

def inflator(intinial_value, increasing_ratio, num_years): 
  new_list =[]
  for i in range(num_years):
    new_list.append(round(intinial_value*(1+increasing_ratio)**i))
  return new_list
result_list = []
result_list.append(inflator(env_data[0],price_index, num_years))
result_list.append(inflator(env_data[1],salary_increase, num_years))
result_list.append(inflator(env_data[2],price_index, num_years))
result_list.append(inflator(env_data[3],income_increase, num_years))
result_list.append(inflator(env_data[4],salary_increase_new_company, num_years))
result_list.append(inflator(env_data[5],price_index, num_years))
# 배열로 만듦
array = np.array(result_list)
label =np.array([['수입'],['인건비'],['운영비'],['수입'],['인건비'],['운영비']])
label_plus = np.hstack([label , array])
print(label_plus)
import os
os.chdir(r'### 이 곳에 경로 삽입 ###')
# 최종명령
pandas.DataFrame(label_plus).to_csv('result_.csv',encoding ='cp949')
 