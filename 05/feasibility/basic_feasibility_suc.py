##### 공기업 설립 시 타당성 조사를 위한 경상수지 비교 기본 프로그램 #######

#usecsv의 값을 저장하도록 함 
import csv, os
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
income_increase = 0
start_year = 2022
#현행방식
wage = int(input("[현행] 첫 해 총인건비 입력하세요(단위: 천원)"))
cost_operation = int(input("[현행] 첫 해 총운영비 입력하세요(단위: 천원)"))
#공단방식23
new_wage = int(input("[공기업(공단)] 첫 해 총인건비 입력하세요(단위: 천원)"))
new_cost_operation = int(input("[공기업(공단)] 첫 해 총운영비 입력하세요(단위: 천원)"))
list_of_initial_value = [wage, cost_operation, new_wage, new_cost_operation]

def inflator(intinial_value, increasing_ratio, num_years): 
  new_list =[]
  for i in range(num_years):
    new_list.append(round(intinial_value*(1+increasing_ratio)**i))
  return new_list


result_list = []
result_list.append([str(i+ start_year)+'년' for i in range(5) ])
result_list.append(inflator(wage,salary_increase, 5))
result_list.append(inflator(cost_operation,price_index, 5))
result_list.append(inflator(new_wage,salary_increase_new_company, 5))
result_list.append(inflator(new_cost_operation,price_index, 5))
print(result_list)

os.chdir(r'저장하고 싶은 파일 경로 ')
writecsv('feasibility_basic.csv',result_list)