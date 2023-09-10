# 파이썬 생활프로그래밍 초판 225페이지부터 
import matplotlib.pyplot as plt
x = [1, 4, 9, 16, 25, 36, 49, 64]

plt.plot(x)
# 선 색깔 빨간 색으로 바꾸기
plt.plot(x, color = 'r')
# 선 색깔 파란 점으로 바꾸기
plt.plot(x, 'ob')

y = [i for i in range(1, 9)]
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('matplotlib sample')

# show가 맨 마지막에 있어서 지금까지 그린 모든 그림들이 다 출력됩니다. 
plt.show()