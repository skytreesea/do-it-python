# 놀이공원 사업수익성 분석  (Do it 파이썬 생활프로그래밍) 초판 2020: 186페이지
import numpy as np 
cf = [-750, -250, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]

cashflow = np.array(cf)

# 순현재가치 구하기 
print(np.irr(cashflow))
# 사업수익률 구하기
print(np.npv(0.045, cashflow))
