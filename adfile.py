import librosa as lb
import sounddevice as sd
import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf
a_p="/home/rguktrkvalley/ghosts.wav"
d,sar=lb.load(a_p,sr=None)
du=len(d)/sar
t=np.linspace(0,du,len(d))
#n=np.linspace(0,len(d),2000)
s1=d[::-3]
s2=t[::5]
s_f=0.5
#y_s=lb.effects.time_stretch(d,0.5)





sd.play(d,0.5*sar)
sd.wait()
#plt.stem(n,d)
#plt.show()

