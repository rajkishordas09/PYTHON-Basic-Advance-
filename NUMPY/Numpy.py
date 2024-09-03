import numpy as np

a=np.array([1,2,3,4])
print(a)
b=np.zeros(3)
print(b)
b=np.ones(3)
print(b)
b=np.empty(2)#address
print(b)
b=np.arange(2)#address
print(b)
b=np.arange(2,10,3)#address
print(b)
b=np.linspace(2,10,5)#address
print(b)

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
print(np.concatenate((a, b)))
b = np.array([6,8,1,9])
print(np.sort(b))