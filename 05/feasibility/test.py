
a = 11223
import re
i = ['abc','32323','23232']
print([i[0]]+[format(int(j),',') for j in i if re.search('\d{3}',j) ])

a=0
b=2
try:
    c= b/a
except:
    print('sorry')

import numpy as np
a = np.array([[0,0,0]])

if a.any():
    print(a)
else: 
    print('----')
