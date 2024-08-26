import numpy as np
import matplotlib.pyplot as plt
n=int (input("Enter starting point: "))
n2=int(input("Enter ending point: "))
l=[]
for i in range(n,n2+1):
	y=round(2*np.cos(0.9*np.pi*i)+9*np.sin(0.25*np.pi*i),3)
	l.append(y)
print(l)
t=np.linspace(n,n2,len(l),endpoint=True)
plt.plot(t,y)
plt.show()
