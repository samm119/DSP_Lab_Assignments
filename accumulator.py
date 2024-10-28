import numpy as np
import matplotlib.pyplot as plt
x=[1,2,3,4,5,6]
coe=[0.2,0.2,0.2,0.2]
out_sig=np.zeros(len(x))
out_sig[0]=x[0]
for i in range(1,len(x)):
    out_sig[i]+=x[i-1]+x[i]
print(out_sig)
plt.plot(out_sig)
plt.show()
