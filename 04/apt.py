import usecsv, os, re
from switch import switch 
# 자기 경로를 입력해야 합니다. 
os.chdir(r' ')
# csv 파일이 같은 폴더에 있는지 먼저 확인하세요.
apt = switch(usecsv.opencsv('apt_201910.csv'))
#apt = usecsv.makenewlist(apt)
#print(apt[3])
header = ['시군구', '번지', '본번', '부번', '단지명', '전용면적(㎡)', '계약년월', '계약일', '거래금액(만원)', '층', '건축년도', '도로명'] 
newlist = []
for i in apt:
	try: 
	#조건1: 100㎡ 이상, 10층에서 15층 사이, 5억이상
		#if i[5]> 100 and i [-3] > 10 and i [-3] < 15 and i[-4] > 50000:
	#조건2: 130㎡ 이상,4억 이하
		#if i[5] > 130 and i[-4] < 30000:
			#출력조건: 지역, 단지명, 크기, 층수, 거래금액 
			#newlist.append([re.match('[가-힣]+ [가-힣]+',i[0]).group(), i[4], i[5], i[-3], i[-4]])
		#조건3  단지명 아이파크
		#if re.search('래미안',i[4]):
			#출력조건: 지역, 단지명, 크기, 층수, 거래금액 
			#newlist.append([re.match('[가-힣]+ [가-힣]+',i[0]).group(), i[4], i[5], i[-3], i[-4]])
	#조건4: 20억 이상
		if i[-4]  > 150000:
			#출력조건: 지역, 단지명, 크기, 층수, 거래금액 
			newlist.append([re.match('[가-힣]+ [가-힣]+',i[0]).group(), i[4], i[5], i[-3], i[-4]])
	except: pass

print(newlist[0])
region = list(set([i[0] for i in newlist]))
summary = [ ]
nameApt = list(set([i[1] for i in newlist]))
price = [i[-1] for i in newlist]

k=0
# 각 지역에 해당 조건 아파트가 몇 채 있는지 summary
for j in region:
	for i in newlist:
		if i[0] == j:
			k += 1
	summary.append([j,k])
	k=0
usecsv.writecsv('apt_over150,000.csv', newlist)
usecsv.writecsv('apt_sum_over150,000.csv', summary)

import numpy as np 
price2=np.array([price])
print(price2.mean(), price2.max())
