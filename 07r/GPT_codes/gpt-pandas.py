import pandas as pd 

# Pandas의 내장 예시 데이터셋 'titanic'을 불러와 데이터프레임 생성
df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

# 데이터프레임의 처음 5개 행 출력
print(df.head()) 
# 데이터프레임 정보 출력 (데이터 타입, 결측치 여부 등)
print(df.info())

# 요약 통계 출력
print(df.describe())

# 그룹별 집계 연산 (예: 평균)
grouped = df.groupby('Pclass')['Fare'].mean()  # 'Pclass' 열을 기준으로 'Fare' 열의 평균 계산
print(grouped)
value_counts = df['Embarked'].value_counts()  # 'Embarked' 열의 고유값과 빈도 출력
print(value_counts)
