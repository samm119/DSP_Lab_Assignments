x=[1,2,3,4,5,6]
res=[]
y=int(input("Enter order: "))
for i in range(0,len(x)):
    if(i==(len(x)-(y-1))):
        x.append(0)
    gr=x[i:i+y]
    ave=round(sum(gr)/y,3)
    res.append(ave)
    print(gr)
print(res)