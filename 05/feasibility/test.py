##### 새기업 설립 시 타당성 조사를 위한 경상수지 비교 기본 프로그램 #######
import pandas as pd
import matplotlib.pyplot as plt
# 환경 데이터로 바로 결과값 도출하도록 함(순서: 현행 수입, 인건비, 운영비, 공단방식 수입, 인건비, 운영비 순으로 입력)
import os,re
#os.chdir(r'###주요데이터입력.csv 와 결과값을 저장할 경로삽입###')
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

def inflator(intinial_value, increasing_ratio, num_years): 
  # 매년 increasing_ratio 씩 num_year 동안 증가, initial_value 입력
  new_list =[]
  for i in range(num_years):
    new_list.append(round(intinial_value*(1+increasing_ratio)**i))
  return new_list

def line(np_row):
# 평균과 합을 추가해주는
    sum = np_row.sum()
    mean = np_row.mean()
    new = np.append(np_row,sum)
    new = np.append(new,mean)
    return new
#퍼센트 만들기 
percent = lambda x: str(round(x*100,2))+'%'

def main(number):

#불러온 데이터에서 필요한 경상수지부분만 data_basic으로 전환
    data_basic = opencsv('주요데이터입력(취합).csv')
    k=0
 #어떤 사업의 결과를 불러낼 것인지
    name = data_basic[number][0] +'_'+ data_basic[number][1]
    data_name = [i for i in data_basic[number][2:]]
    data = [float(i) for i in data_basic[number][2:]]
    price_index = data[6]
# 인건비 상승률
    salary_increase =data[7]
# 대상사업수입증가율
    income_increase = data[8]
# 새 회사의 인건비 상승률 
    salary_increase_new_company = data[9]
# 새 회사의 운영비 상승률
    operation_increase_new_company = data[10]
    start_year = 2022
# 분석기간(년도)
    num_years = 5
    result_list=[]
    print(name, salary_increase, salary_increase_new_company)
    
main(1)