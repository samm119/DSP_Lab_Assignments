import numpy as np
from matplotlib import pyplot as pt
def circulardelay(x,m):
	N=len(x)
	y=[]
	for n in range(0,N):
		if n-m>=0:
			idx=(n-m)%N
		else:
			idx=N+n-m
		y.append(x[idx])
	return y
x1=[1,2,3,4,5]
m=3
y=circulardelay(x1,m)
pt.subplot(2,1,1)
pt.stem(x1)
pt.subplot(2,1,2)
pt.stem(y)
pt.show()
