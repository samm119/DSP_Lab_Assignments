import numpy as np
def cir_con(x,h):
    N=len(x)
    y=np.zeros(N)
    for n in range(N):
        for m in range(N):
            if(n-m>=0):
                y[n]+=x[n]*h[m-n]%N
            else:
             	y[n]+=x[n]*h[m-n]
    return y
x=np.array([1,2,3,4,5])
h=np.array([6,7,8,9,0])
print(cir_con(x,h))
