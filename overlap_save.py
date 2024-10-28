import numpy as np
def circular_convolution(x, h):
    N = len(x)
    result = np.zeros(N)
    
    for n in range(N):
        for m in range(N):
            result[n] +=int( x[m] * h[(n - m) % N])
    
    return result
x = [1,-2,3,2,-3,4,3,-4]
h = [1,2 ,-1]
m=len(h)
N = len(x)
l = 4
k = [x[i:i + l] for i in range(0, len(x), l)]
for i in range(l-1):
    h.append(0)
for i in range(m-1):
    k[0].insert(0,0)
for i in range(1,m):
    k[i].insert(0,k[i-2][-1])
    k[i].insert(0,k[i-2][-2])
l=[]
for i in range(0,len(k)):
 l.append(list(circular_convolution(k[i],h)))
print("Convolution Result: ",l)
for i in l:
    del i[0:m-1]
res=[]
for i in range(len(l)):
    for j in range(len(l[0])):
        res.append(l[i][j])
print("Final Output: ",res)
