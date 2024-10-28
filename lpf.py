import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, lfilter, freqz
fs = 500 
t = np.arange(0, 2, 1/fs)

# Create a noisy signal: a 5 Hz sine wave + 50 Hz noise
freq_signal = 5  # Frequency of the signal (Hz)
freq_noise = 50 
signal = np.cos(2 * np.pi * freq_signal * t)  # Clean sine wave
noise = 0.5 * np.sin(2 * np.pi * freq_noise * t)  # Noise (higher frequency)
noisy_signal = signal + noise  # Noisy signal (signal + noise)

# FIR Filter design parameters
cutoff_freq = 10  # Cutoff frequency of the low-pass filter (Hz)
num_taps = 101    # Number of filter coefficients (the higher, the sharper the filter)
nyquist_rate = fs / 2  # Nyquist frequency

# Design the FIR low-pass filter
fir_coeffs = firwin(num_taps, cutoff_freq / nyquist_rate)

# Apply the FIR filter to the noisy signal
filtered_signal = lfilter(fir_coeffs, 1.0, noisy_signal)

# Frequency response of the filter
w, h = freqz(fir_coeffs, worN=8000)
frequencies = w * nyquist_rate / np.pi

# Plot the results
plt.figure(figsize=(12, 8))

# Original noisy signal
plt.subplot(3, 1, 1)
plt.plot(t, noisy_signal, label='Noisy Signal')
plt.title("Noisy Signal (5 Hz + 50 Hz noise)")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.legend()

# Filtered signal
plt.subplot(3, 1, 2)
plt.plot(t, filtered_signal, label='Filtered Signal (Low-Pass)', color='green')
plt.title(f"Filtered Signal (Low-Pass with cutoff = {cutoff_freq} Hz)")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.legend()


plt.subplot(3, 1, 3)
plt.plot(frequencies, np.abs(h), 'r', label='Filter Frequency Response')
plt.title("Frequency Response of the FIR Low-Pass Filter")
plt.xlabel("Frequency [Hz]")
plt.legend()
plt.show()
