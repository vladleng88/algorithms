from scipy.interpolate import interpolate
import matplotlib.pyplot as plt
import numpy as np
p = [5510.50000,  5201.50000,  5098.50000,  4995.50000,  4944.00000,  5005.79980,	5150.00000,  5510.50000,  5768.00000 , 5871.00000,  5974.00000]
M = [0.00000 ,    0.10000,     0.20000,     0.30000  ,   0.40000   ,  0.50000	,0.60000   ,  0.80000   ,  0.90000    , 1.00000   ,  1.21000]
f = interpolate.interp1d(M, p)
print(f(0.25))
#p2 = [2290,	1770,	1240,	720,	196]
p2 = [482,446,409,373,337]
#g2 = [1901,	1494,	1102,	725,	341]
g2 = [452,417,382,350,320]
f2 = interpolate.interp1d(p2, g2, kind='slinear', fill_value='extrapolate')
#p_max = 3271.428571
p_max = 688.5714286
g20 = f2(p_max)
ce = g20/p_max
print(g20, ce)
"""fig, ax = plt.subplots()
ax.plot([g20]+g2, [p_max]+p2)
plt.show()"""


a = {'a':[1], 'b': [2]}
def func():
    t = {}
    vsp = a
    t['a'] = np.array(a['a'])
    t['b'] = a['b']
    return t
print('a',a)
b = func()
print('funt',b)
b['a'][0] = 2
b['b'][0] = 3
print('a',a)
print('funt',b)
c= np.array([1,2,3])
print(c*[1,2,3])
print(np.array(c))
