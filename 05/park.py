import numpy as np
import numpy_financial as npf
import usecsv

discount = .05
cashflow = 100

cash_flows = np.array([-1000, 200, 300, 400, 500])  # 예시 캐시플로우
discount = 0.045  # 할인율

def presentvalue(n):
    return (cashflow / ((1 + discount ) ** n))

print(presentvalue(1))
print(presentvalue(2))

for i in range(20):
    print(presentvalue(i))
    

loss = [-750]
# 첫 해(Y0)에는 부지비와 공사비가 들어가서 비용만 발생합니다. 
profit = [100] * 10
# 10년동안 이익 10억이 발생한다고 가정합니다. 
print(profit)
cf = loss + profit
print(cf)

cashflow = np.array(cf)
print(cashflow)

npv = npf.npv(0.045, cashflow)
print(f"할인률 4.5%일 때 순현재가치 {npv}")
 
irr = npf.irr(cashflow)
print(f"내부수익률 {irr}")