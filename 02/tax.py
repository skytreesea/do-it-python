# 서비스 요금과 부가세 계산  (Do it 파이썬 생활프로그래밍) 초판 2020: 52페이지
def service_price():
    service = input('서비스 종류를 입력하세요, a/b/c: ')	## 서비스 종류를 입력
    valueAdded = input('부가 가치세를 포함합니까? y/n: ')	## 부가세 포함 여부 입력
    if valueAdded == 'y':					## 부가세가 있을 때
        if service == 'a': 				## 서비스 종류가 a라면
            result = 23 * 1.1 				## 23만 원에 1.1을 곱하여 result에 저장
        if service == 'b':
            result = 40 * 1.1
        if service == 'c':
            result = 67 * 1.1 
    if valueAdded == 'n':					## 부가세가 없을 때
        if service == 'a':					## 서비스 종류가 a라면
            result = 23 					## 23만 원을 그대로 result에 저장
        if service == 'b':
            result = 40
        if service == 'c':
            result = 67		
    print(round(result,1), '만원입니다')

# 실행문
service_price()
