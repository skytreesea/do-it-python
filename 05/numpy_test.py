import numpy as np 
import usecsv

# 2*2 배열 만들기 
a = np.array([[2, 3], [5, 2]]) 

print(a)

d = np.array([2, 3, 4, 5, 6])

# 배열의 크기 알아내기 
print(d.shape)

e = np.array([[1, 2, 3, 4], [3, 4, 5, 6]])
# e 출력하기 
print(e)
# e 배열의 크기 알아내기 
print(e.shape)
print(e.dtype)

data = np.arange(1, 5)
print(data.dtype)
# float64로 바꿈
print(data.astype('float64'))
 
# 0으로 만들어진 배열 만들기 
print(np.zeros((2,10)))
# 0으로 만들어진 배열 만들기 
print(np.ones((2,10)))
# 2 이상 10 미만의 원소로 이루어진 1차원 배열을 만듭니다
print(np.arange(2,10))

a = np.ones((2, 3))
# tranpsose로 행열 바꾸기
b = np.transpose(a)
print(b)

arr1 = np.array([[2, 3, 4], [6, 7, 8]])
arr2 = np.array([[12, 23, 14], [36, 47, 58]])

# 배열의 덧셈
print(arr1 + arr2)
# 배열의 곱셈
print(arr1 * arr2)
# 배열의 나눗셈
print(arr1 / arr2)

arr3 = np.array([100, 200, 300])

print(arr1)
print(arr3)

print(arr1 + arr3)

arr4 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(arr4.shape)
print(arr1.shape)
arr5 = np.array([[9], [3]])
 
print(arr5 + arr1)

d = np.array([[1, 2, 3, 4, 5], [2, 4, 5, 6, 7], [5, 7, 8, 9, 9]])
d[:2] = 0

print(d)

arr4 = np.arange(10)
print(arr4)

# 자신의 파일이 위치한 주소와 파일명을 입력하세요. 
quest = r"C:\Users\skytr\Documents\GitHub\do-it-python\05\quest.csv"
# np 배열로 불러오기 
quest = np.array(usecsv.switch(usecsv.opencsv(quest)))
# 5 초과한 경우만 출력하기
print(quest > 5)

# 5 초과한 값은 모두 5로 바꿈
quest[quest > 5] = 5

print(quest)

usecsv.writecsv('resultcsv.csv', list(quest))