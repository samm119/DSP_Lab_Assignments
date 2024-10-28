f=[1,2,3,4,5]
g=[6,7,8,9,10]
len_res=len(f)+(len(g)-1)
res=len_res*[0]
for i in range(0,len_res-1):
    sum=0
    for k in range(0,len(f)-1):
        if(i-k)>=0 and (i-k)<len(g):
            sum=sum+f[k]*g[i-k]
    res[i]=sum

print(res)