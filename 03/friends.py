# 드라마 텍스트 가공  (Do it 파이썬 생활프로그래밍) 초판 2020: 52페이지
# friends.txt를 다운받아서 같은 폴더에 넣은 다음 프로그램을 실행합니다. 
import os, re, codecs
#자신의 저장경로를 입력해야 합니다. 
os.chdir(r' ')
f = open('friends101.txt', 'r', encoding = 'utf-8')
script101 = f.read()

# 문자열 객체 슬라이싱
print(script101[:100])

Line = re.findall(r'Monica:.+', script101)
#리스트 요소 중 앞에서 3개까지만 출력
print(Line[:3])
# 모니카의 대사만 모으기 
Line = re.findall(r'Monica:.+', script101)

# monica.txt 파일 만들기
f = open('monica.txt', 'w', encoding = 'utf-8')
monica = ''
for i in Line:
	monica += i +'\n'
f.write(monica)
# 파일 닫기 
f.close()	

# 모니카의 대사만 출력해보기
for item in Line[:3]:
    print(item)

# 등장인물 이름 모으기 
print(re.findall(r'[A-Z][a-z]+: ', script101) )

# 중복 지우기
print(set(re.findall(r'[A-Z][a-z]+: ', script101)))

# 캐릭터 이름 한 줄로 출력하기
character = [x[:-2] for x in list(set(re.findall(r'[A-Z][a-z]+: ',script101)))]

# 캐릭터 이름 각각 출력하기 
for i in character:
    print(i)

# 지문만 출력하기
re.findall(r'\([A-Za-z].+[a-z|\.]\)', script101, re.VERBOSE) [:6]
f = open('friends101.txt','r')
sentences = f.readlines()
# 20개만 출력해보기
for i in sentences[:20]:			## 먼저 문장 20개만 가져와 실험해 보겠습니다
    if re.match(r'[A-Z][a-z]+:', i): 	## match 문으로 문장 맨 앞에서 패턴을 찾습니다 
        print(i)

# would가 나오는 문장만 추출하기 
would = [ i for i in sentences if re.match(r'[A-Z][a-z]+:', i) and re.search('would', i)]
# take가 들어간 문장만 추출하기 
take = [ i for i in sentences if re.match(r'[A-Z][a-z]+:', i) and re.search(' take',i)]
# take가 들어간 문장 출력하기
for i in take:
	print(i)
 
# would가 들어간 문장 파일로 만들기 
newf = open('would.txt','w')	
newf.writelines(would)		
