import numpy as np
from matplotlib import pyplot as plt
N=4
n=np.arange(N)
x1=[1,2,3,4]
l1=len(x1)
o=np.linspace(-np.pi,np.pi,100)
for i in range(0,l1-1):
  y1=np.array([np.sum(x1[i]*np.exp(-1j*w*n)) for w in o])
x2=[4,3,2,1]
l2=len(x2)
for i in range(0,l2-1):
   y2=np.array([np.sum(x2[i]*np.exp(-1j*w*n)) for w in o])
print(y1)
print(y2)
y=reversed(y1)
print(y)
if(y.all()==y2.all()):
  print("time reversal")
else:
  print("not")
