import os, re, codecs
# 프렌즈 대사 활용하기 
# 활용순서 1)  https://github.com/skytreesea/do-it-python/blob/master/friends101.txt 에서 friends101.txt 를 다운받는다. 
# 다음과 같이 저장경로로 찾아간다. 특이사항:  '앞에 r을 붙이고 ''안에 경로를 정확하게 붙여넣는다. 
os.chdir(r'#### friends101.txt ####를 저장한 경로')

# 아래  폴더에 이 파일을 넣고 아래 명령어를 실행해 본다. 
# friends101.txt 불러오기 
f  =  codecs.open('friends101.txt','r','utf-8')
script101  =  f.read()

# Monica의 대사만 불러오는 명령
Monica  =  re.compile(r'Monica:.+')
Line  =  re.findall(Monica, script101)
f.close()
#모니카의 대사만 모아서 출력해보기
print(Line[:3])

f  =  codecs.open('monica.txt','w','utf-8')
# 모니카의 대사만 모아서 'monica.txt'로 저장하기 
monica  = ''
for i in Line:
	monica += i
	#monica라는 문자열(객체)에 Line의 모든 원소를 추가하라
f.write(monica)
f.close()

char  =  re.compile(r'[A-Z][a-z]+: ')
re.findall(char, script101)
#set으로 중복 지우기 
a  =  [1,2,3,4,5,2,2]
# 중복되는 원소 지우기 test
print(set(a))

# 등장인물 모으기(중복되는 원소 지우기 활용)
print(set(re.findall(char, script101)))

# 다시 같은 파일 불러오기 
f  =  codecs.open('friends101.txt','r','utf-8')
# 시험삼아 앞 부분만 출력해보기 
sentences  =  f.readlines()
print(sentences[:4])

# 인물 다음 콜론(:) 지우기 연습
rachel  =  'Rachel:'
rachel  =  re.sub(':','',rachel)
print(rachel)

# 괄호 안 내용만 모으기 
re.findall( r'\([A-Za-z].+[a-z|\.]\)' ,  script101) [:6]

# 대사를 출력하기 
for i in sentences[:20]:
	if re.match(r'[A-Z][a-z]+:', i):
		print(i)

# 대사만 추출하기
sentences  =  [ i for i in sentences if re.match(r'[A-Z][a-z]+:', i)]
# would가 들어간 대사만 추출하기 
would  =  [ i for i in sentences if re.match(r'[A-Z][a-z]+:', i) and re.search('would',i)]
# take가 들어간 대사만 추출하기 
take  =  [ i for i in sentences if re.match(r'[A-Z][a-z]+:', i) and re.search(' take',i)]
# take가 들어간 대사만 출력하기
print(take)

# would.txt 로 'would'가 들어간 파일만 저장하기 
newf = open('would.txt','w')
newf.writelines(would)
newf.close()
newf.close()

