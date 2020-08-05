# test numpy
import numpy as np
import matplotlib.pyplot as plt

a = np.matrix([[1, 2], [3, 4]])
print('a=', a)
print('a.shape=', a.shape)
print('a.size=', a.size)
print('a.dtype=', a.dtype)

print('aT=', a.T)
print('aI=', a.I)
print(a.I * a)

b = np.matrix([[7, 6], [5, 4]])
print('b=', b)

print('a*b=', a * b)

x = np.linspace(0, 2 * np.pi, 50)
plt.plot(x, np.sin(x), 'r-o',
         x, np.sin(2 * x), 'b-^')
plt.xlabel('Rads')
plt.ylabel('Result')
plt.title('Sin and Cos Wave')
plt.show()

x2 = np.random.randn(100)
plt.hist(x, 50)
plt.show()
