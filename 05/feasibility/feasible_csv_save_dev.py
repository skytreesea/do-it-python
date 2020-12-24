##### 새기업 설립 시 타당성 조사를 위한 경상수지 비교 기본 프로그램 #######
import pandas as pd
# 환경 데이터로 바로 결과값 도출하도록 함(순서: 현행 수입, 인건비, 운영비, 공단방식 수입, 인건비, 운영비 순으로 입력)
import os
os.chdir(r'C:\Users\ERC\Documents\GitHub\do-it-python\05\feasibility')
env_data = [25636,40144,461034,736255,356785,777226]
name = 'new사업명'
#usecsv의 값을 저장하도록 함 
import csv, os
import numpy as np
def opencsv(filename):
    f=open(filename, 'r')
    reader=csv.reader(f)
    output=[]
    for i in reader:
        output.append(i)
    return output
def writecsv(filename, the_list):
    with open(filename,'w',newline='') as f:
        a=csv.writer(f, delimiter=',')
        a.writerows(the_list)
#불러온 데이터에서 필요한 경상수지부분만 data_basic으로 전환
data_basic = opencsv('input_data.csv')[1][1:7]
data = [int(i) for i in data_basic]

print(data)
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
  # 매년 increasing_ratio 씩 num_year 동안 증가, initial_value 입력
  new_list =[]
  for i in range(num_years):
    new_list.append(round(intinial_value*(1+increasing_ratio)**i))
  return new_list
result_list=[]
result_list.append(inflator(data[0],price_index, num_years))
result_list.append(inflator(data[1],salary_increase, num_years))
result_list.append(inflator(data[2],price_index, num_years))
result_list.append(inflator(data[3],income_increase, num_years))
result_list.append(inflator(data[4],salary_increase_new_company, num_years))
result_list.append(inflator(data[5],price_index, num_years))
array = np.array(result_list)
# 현행방식, 공단방식 경상수지 비율
balance_current = np.array(array[0]/(array[1]+array[2]))
balance_new = array[3]/(array[4]+array[5])
# 현행방식 공단방식 이익
profit_current = array[0]-(array[1]+array[2])
profit_new = array[3]-(array[4]+array[5])
# new_array에 저장
# 평균과 합을 추가해주는
def line(np_row):
    sum = np_row.sum()
    mean = np_row.mean()
    new = np.append(np_row,sum)
    new = np.append(new,mean)
    return new
# 현행(수입)
new_array = np.array([line(array[0])])
print(new_array)
# 영업비용
new_array = np.r_[new_array, [line(array[1]+array[2])]]
# 인건비
new_array = np.r_[new_array, [line(array[1])]]
# 운영비
new_array = np.r_[new_array, [line(array[2])]]
# 영업이익
new_array = np.r_[new_array, [line(profit_current)]]
# 경상수지비율
new_array = np.r_[new_array, [line(balance_current)]] 

# 공단(수입)
new_array = np.r_[new_array, [line(array[3])]] 
# 영업비용
new_array = np.r_[new_array, [line(array[4]+array[5])]]
# 인건비
new_array = np.r_[new_array, [line(array[4])]]
# 운영비
new_array = np.r_[new_array, [line(array[5])]]
# 영업이익
new_array = np.r_[new_array, [line(profit_new)]]
# 경상수지비율
new_array = np.r_[new_array, [line(balance_new)]] 
# 현행영업이익
new_array = np.r_[new_array, [line(profit_current)]]
# 공단영업이익
new_array = np.r_[new_array, [line(profit_new)]]
# 수지개선효과
new_array = np.r_[new_array, [line(profit_new - profit_current)]]
# 레이블은 맨 마지막에 붙이면 됨
label =np.array([['영업이익','영업비용','인건비','운영비','영업이익','경상수지비율','영업이익','영업비용','인건비','운영비','영업이익','경상수지비율','현행영업이익','공단영업이익','수지개선']]).transpose() 
label_plus = np.hstack([label,new_array])

if balance_new.mean() >= .5:
    print('새기업 방식 경상수지 비율 5할 이상 충족, 경상수지 비율:', round(balance_new.mean(),3) )
else:
    print('새기업 방식 경상수지 비율 5할 이상 미충족, 경상수지 비율:', round(balance_new.mean(),3) )

# # np로 계산한 것을 리스트로 만들어 csv로 저장
total=[]
total.append(['현행',	'2022',	'2023',	'2024',	'2025',	'2026',	'계',	'평균'])
k=0
for i in label_plus:  
   total.append(i)
   k+=1
   if k == 6:
       total.append(['공기업방식',	'2022',	'2023',	'2024',	'2025',	'2026',	'계',	'평균'])

# 최종명령
writecsv(name+'_result.csv',total)