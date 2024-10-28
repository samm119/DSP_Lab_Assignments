import matplotlib.pyplot as plt
import  numpy as np
fs=8000#int(input("Enter Sampling Frequency: "))
Fc=2000#int(input("Enter Max Freuquency of the signal must be leass than or equal to fs/2: "))
N=16#int(input("Enter The no.of DFT Points: "))
k=[]
H_k=np.zeros(N-1)
for i in range(0,int(N/2)):
    k.append(i)
F=[]
for i in k:
    F.append(int(fs/N)*i)
kc=int(F.index(Fc))
# print(kc)
H_k[:kc]=1
H_k[kc:int(N/2)]=0
H_k[int(N/2):int(N/2)+kc]=0
H_k[int(N/2)+kc:N-1]=1

print(H_k)
# print("Enter Elements for x(n): ")
x_n=[1,2,3,4,5,6,7,8,9,1,1,2,3,4,5,6]
# for i in range(N):
#     x=int(input("Element: "))
#     x_n.append(x)
M=len(x_n)

X_k=[]
omega=np.arange(0,2*np.pi,(2*np.pi/M))
for i in range(0,M):
    f=[]
    for j in range(0,M):
        a=x_n[j]*np.exp(-1j*(2*np.pi*j*i)/M)
        f.append(a)
    X_k.append(sum(f))
Y=[]
print(len(X_k))
for i in range(N):
    Y.append(X_k[i]*H_k[i])
print(len(Y))





                 