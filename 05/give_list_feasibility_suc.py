##### 공기업 설립 시 타당성 조사를 위한 경상수지 비교 기본 프로그램 #######
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
# 현행방식, 공단방식 이익
profit_current = array[0]-(array[1]+array[2])
profit_new = array[3]-(array[4]+array[5])
# 현행방식, 공단방식 경상수지 
balance_current = array[0]/(array[1]+array[2])
balance_new = array[3]/(array[4]+array[5])
# 출력 영역
print(array)
print('현행 영업이익')
print(profit_current)
print(balance_current)
print(round(balance_current.mean(),3))
print('공기업 방식 영업이익')
print(profit_new)
print(balance_new)
print(round(balance_new.mean(),3))
if balance_new.mean() >= .5:
    print('공기업 방식 경상수지 비율 5할 이상 충족, 경상수지 비율:', round(balance_new.mean(),3) )
else:
    print('공기업 방식 경상수지 비율 5할 이상 미충족, 경상수지 비율:', round(balance_new.mean(),3) )
#수지개선효과
improving_impact = profit_new-profit_current
print(improving_impact, '\n',improving_impact.sum(), "천원 수지개선 효과")
