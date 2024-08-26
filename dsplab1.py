import numpy as np
import matplotlib.pyplot as plt
t=np.arange(0,0.5,0.003)
y=np.sin(2*np.pi*5000*t)
plt.stem(t,y)
plt.show()
