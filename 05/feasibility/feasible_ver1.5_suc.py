##### 새기업 설립 시 타당성 조사를 위한 경상수지 비교 기본 프로그램 #######
import pandas as pd
# 환경 데이터로 바로 결과값 도출하도록 함(순서: 현행 수입, 인건비, 운영비, 공단방식 수입, 인건비, 운영비 순으로 입력)
import os,re
os.chdir(r'C:\Users\ERC\Documents\GitHub\do-it-python\05\feasibility\data')
#usecsv의 값을 저장하도록 함 
import csv, os
import numpy as np
#csv 읽고 쓰기 
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

#퍼센트 만들기 
percent = lambda x: str(round(x*100,2))+'%'
#어떤 사업의 결과를 불러낼 것인지
number = 3
#불러온 데이터에서 필요한 경상수지부분만 data_basic으로 전환
data_basic = opencsv('주요데이터입력.csv')
name = data_basic[number][0] +'_'+ data_basic[number][1]
data = [float(i) for i in data_basic[number][2:]]
# 현행방식과 공기업 방식의 인플레이션 인덱스 부여
# 물가상승률
price_index = data[6]
# 인건비 상승률
salary_increase =data[7]
# 대상사업수입증가율
income_increase = data[8]
# 새 회사의 인건비 상승률 
salary_increase_new_company = data[9]
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
def line(np_row):
# 평균과 합을 추가해주는
    sum = np_row.sum()
    mean = np_row.mean()
    new = np.append(np_row,sum)
    new = np.append(new,mean)
    return new

# 현행(수입)
new_array = np.array([line(array[0])])
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


# # np로 계산한 것을 리스트로 만들어 csv로 저장
total=[]
total.append(['사업명',	name])
total.append(['',	'물가상승률','인건비상승률',	'수입증가율'+percent(income_increase),	'인건비상승률',	'시작년도'	])
total.append(['',percent(price_index),percent(salary_increase),percent(income_increase),percent(salary_increase_new_company),str(start_year),'(단위:천원)'])
total.append(['현행'])
total.append(['구분','2022',	'2023',	'2024',	'2025',	'2026',	'계',	'평균'])
k=0
# 2번째 요소부터 퍼센트가 들어있는 리스트를 퍼센트 형태로 바꿔주는 함수 
def percent_list(list_of_percent) : 
    new = [percent(float(i)) for  i in list_of_percent[1:]]
    new.insert(0,list_of_percent[0])
    return new

for i in label_plus:  
    if re.search('비율',i[0]):
        total 
        total.append(percent_list(i))
    else: 
        total.append(i)
    if k == 5:
        total.append(['공단방식'])
        total.append(['구분',	'2022',	'2023',	'2024',	'2025',	'2026',	'계',	'평균'])
    if k == 11:
        total.append(['수지분석 결과'])

    k+=1
if balance_new.mean() >= .5:
    final_result =  "가능"
    total.append(['충족', '경상수지 비율:', percent(balance_new.mean()), final_result] )
else:
    final_result =  "불가능"
    total.append(['미충족', '경상수지 비율:', percent(balance_new.mean()),final_result] )
# 최종명령
writecsv(name+'_'+final_result+'_물상'+str(price_index)+'인상'+str(salary_increase_new_company)+'수입증가'+str(income_increase)+'.csv',total)
print(name,final_result, '물가상승률',percent(price_index),"공무원인건비상승률",percent(salary_increase))