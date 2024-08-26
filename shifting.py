import numpy as np
import matplotlib.pyplot as plt
x=[1,2,3,4,]
inp=int(input("Enter shift: "))
y=[]
for i in range(0,np.abs(inp)):
	y.append(0)
for i in range(0,len(x)):
	y.append(x[i])
print(y)
n=np.arange(0,100,1)
omega=np.arange(-1*np.pi,np.pi,0.001*np.pi)
X1=[]
X2=[]
for i in range(0,len(x)):
    X1.append((y[i]*np.exp(-1j*omega*i)))
    X2.append(x[i]*np.exp(-1j*omega*i))
h=[]
for i in range(0,len(X1)):
	h.append(np.sum(X1[i]*np.exp(-1j*omega*np.abs(inp)))
d=np.abs(h)
d1=np.abs(sum(X2))
plt.plot(omega,d1)
plt.plot(omega,d)
plt.show()
