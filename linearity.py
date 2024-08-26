import numpy as np
import matplotlib.pyplot as plt
x1=[1,2,3,4]
x2=[4,3,2,1]
x3=[]
for i in range(0,len(x1)):
	x3.append(x1[i]+x2[i])
print(x3)
r1=[]
r2=[]
r3=[]
n=np.arange(0,100,1)
N1=len(x1)
N2=len(x2)
omega=np.arange(-1*np.pi,np.pi,0.001*np.pi)
for i in range(0,len(x1)):
    r1.append(x1[i]*np.exp(-1j*omega*i))
    r2.append(x2[i]*np.exp(-1j*omega*i))
    r3.append(x3[i]*np.exp(-1j*omega*i))
s1=sum(r1)+sum(r2)
s3=sum(r3)
s=np.abs(s1)
#s2=np.abs(s2)
s2=np.abs(s3)
print("x1+x2",(s1))
print("x3",s3)
fig,ax=plt.subplots(nrows=1,ncols=2)
ax[0].plot(omega,(s))
ax[0].set_title("x1+x2")
ax[1].plot(omega,s2)
ax[1].set_title("x3")
fig.suptitle("Linearity",fontsize=25,color='red')
plt.show()
