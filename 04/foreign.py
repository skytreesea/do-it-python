# 외국인비율 구하기  (Do it 파이썬 생활프로그래밍) 초판 2020: 149페이지
# 이 명령을 실행하기 전에, 같은 폴더에 'usecsv.py'가 복사되어 있거나, usecsv.py가 전체 경로에서 이동될 수 있도록 설정해야 합니다. 
# Git-hub에 올릴 때 한글이 깨지는 경우가 있어 부득이 구 이름을 영어로 표기했습니다. 

import os, re		## os 모듈과 re 모듈은 항상 필요하기 때문에 먼저 임포트 합니다
import usecsv		## usecsv 모듈을 임포트 합니다		
os.chdir(r'C:\Users\skytr\Documents\GitHub\do-it-python\04')	## popSeoul.csv 파일을 저장한 경로로 이동합니다

# 파일 열기 
total = usecsv.opencsv('popSeoul.csv')	

# 콤마 등을 제거하는 함수 usecsv.switch를 사용합니다. 
newPop = usecsv.switch(total)	
# 4번째 구까지만 시험으로 출력해봅니다. 
print(newPop[:4])

for i in newPop:
	foreign = 0
## 한 번 루프가 돌고 나면 foreign을 다시 지정해주어야 하므로 foreign을 0으로 먼저 지정합니다
	try:
		foreign = round(i[2] / (i[1] + i[2]) * 100, 1)
		print(i[0], foreign)
## i[0]에는 지역구 이름이 저장되어 있고, foreign은 공식대로 우리가 계산한 외국인 비율입니다
	except:
		pass

print(i)
new = [['구', '한국인', '외국인', '외국인 비율(%)']]   
new.append([i[0], i[1],i[2],foreign])
# 강동구 정보가 남아 있습니다. 
print(new)
# 등록외국인의 비율이 3이 넘을 때만 넘을 때만 출력합니다. 
for i in newPop:
    foreign = 0 
    try:
        foreign = round(i[2] / (i[1] + i[2]) * 100, 1)
        if foreign > 3:		 
            new.append([i[0], i[1],i[2],foreign])
    except:
        pass

# 3% 넘는 구만 파일로 저장하기
usecsv.writecsv('newPop.csv',new)
