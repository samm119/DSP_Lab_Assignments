import numpy as np
import scipy
from scipy.fft import fft, fftshift
import matplotlib.pyplot as plt
# Parameters
sampling_rate = 44100  # Hz
duration = 2  # seconds
frequency = 440  # Hz

# Generate time vector
time = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

# Generate sine wave
signal = np.sin(2 * np.pi * frequency * time)
# Calculate the DFT
fft_result = fft(signal)

# Shift the zero frequency component to the center
fft_shifted = fftshift(fft_result)

# Calculate the frequency axis
freq = np.linspace(-sampling_rate/2, sampling_rate/2, len(fft_shifted))
# Plot the magnitude spectrum
plt.figure(figsize=(10, 4))
plt.plot(freq, np.abs(fft_shifted))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('DFT of a Sine Wave')
plt.grid(True)
plt.show()
