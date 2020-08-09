import os, re
#경로 찾아서 입력하기 1번째 원소에는 주어를, 두번째 원소에는 설명을 적습니다. 주어에 따라서 "은/는"을 구분합니다. 
sample = [['사무자동화','60억원'], ['건축비','250억원'],['용역비','20억원'],['예비비','24억원'], ['이 사업','건축사업']]

def checkForJosa(c):
	# 받침이 있으며 True를 받침이 없으면 False를 반환합니다. 
    return (int((ord(c) - 0xAC00) % 28) != 0)

for i in sample:
	if checkForJosa(i[0][-1]):
		print("%s은 %s입니다. " % (i[0],i[1] ))
	elif checkForJosa(i[0][-1]) is not True:
		print("%s는 %s입니다." % (i[0],i[1] ) )
	
# 그냥 이 파일을 실행만 시켜보면 됩니다. 
