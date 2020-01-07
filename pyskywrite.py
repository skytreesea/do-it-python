import os, csv, re
#***경로 찾아서 입력하기 (창에서 경로를 붙여와서 작은 따옴표 안에 넣습니다.)
os.chdir(r'***')
# csv파일의 첫 열에는 주어, 두번째 열에는 설명이라는 규칙으로 csv파일을 만듭니다. 

def checkForJosa(c):
	# 받침이 있으며 True를 받침이 없으면 False를 반환합니다. 
    return (int((ord(c) - 0xAC00) % 28) != 0)

def opencsv(filename):
	# csv 파일 불러오기 
    f=open(filename, 'r')
    reader=csv.reader(f)
    output=[]
    for i in reader:
        output.append(i)
    return output

# ***파일 이름 입력하기
total = opencsv('***')

for i in total:
	if checkForJosa(i[0][-1]):
		print("%s은 %s입니다. " % (i[0],i[1] ))
	elif checkForJosa(i[0][-1]) is not True:
		print("%s는 %s입니다." % (i[0],i[1] ) )
	
