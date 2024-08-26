import librosa as librosa
import sounddevice as sd
import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf

a_p = "/home/rguktrkvalley/doggy.wav"
d, sar = librosa.load(a_p, sr=None)
du = len(d) / sar
t = np.linspace(0, du, len(d))  # Time axis with same length as audio data

s_f = 0.5
y_s = librosa.effects.time_stretch(d, 0.5)

sd.play()
sd.wait()

# Optional plotting (uncomment and adjust time axis if needed)
# plt.stem(t, d)  # Plot original audio
# plt.stem(t, y_s)  # Plot stretched audio
# plt.show()

