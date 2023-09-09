import usecsv, csv, re, os
# 자기 경로를 입력해야 합니다.  
# csv 파일이 같은 폴더에 있는지 먼저 확인하세요.
#apt = usecsv.switch(usecsv.opencsv(r'C:\Users\skytr\Documents\GitHub\do-it-python\05\\apt2308.csv'))
os.chdir(r'C:\Users\skytr\Documents\GitHub\do-it-python\05')
apt=usecsv.opencsv(r'apt2308.csv' )
apt = usecsv.switch(apt)
# 불러오는 데 성공 
for i in apt[:6]:
    print(i[0],i[4],i[-8]) 
    
for i in apt:
	try:
# 오류가 날 경우를 대비해 예외 처리를 사용하겠습니다
		if i[5] >= 120 and i[8] <= 30000 and re.match('강원', i[0]):
# 면적(i[5]) 120㎡ 이상, 가격(i[8]) 3억 이하, 시군구(i[0])에는 '강원'을 포함하는 조건입니다
			print(i[0], i[4], i[8])
# 시군구, 아파트 단지명, 가격 순으로 출력합니다. 
	except: 
		pass

new_list = []
# 어떤 이름으로든 빈 리스트를 만드는 것이 CSV형 리스트를 만드는 첫걸음입니다

for i in apt:
	try: 
		if i[5] >= 120 and i[8] <= 30000 and re.match('강원', i[0]):
# 앞에서 만든 조건을 그대로 입력합니다			
			new_list.append([i[0], i[4], i[8]])
# 앞에서 출력했던 시군구, 아파트 단지명, 가격을 new_list에 저장합니다 
	except: 
		pass

print(new_list)
usecsv.writecsv(r'result_over120_lower30000.csv', new_list)
# writecsv() 함수로 new_list 객체에 저장된 CSV형 리스트를 CSV 파일로 저장합니다

