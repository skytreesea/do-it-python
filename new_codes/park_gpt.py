import numpy as np
import numpy_financial as npf

cf = [-750, -250, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
cashflow = np.array(cf)

# 순현재가치 구하기 
print(npf.irr(cashflow))

# 사업수익률 구하기
print(npf.npv(0.045, cashflow))
