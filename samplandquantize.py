import numpy as np
import matplotlib.pyplot as plt

f = 200
duration = 0.5
fs_original = 8000
fs_resample = 1000
quantization_levels = 8

t_original = np.arange(0, duration, 1/fs_original)
signal = np.sin(2 * np.pi * f * t_original)

t_resample = np.arange(0, duration, 1/fs_resample)
signal_resample = signal[::fs_original // fs_resample]

signal_min = np.min(signal_resample)
signal_max = np.max(signal_resample)
signal_normalized = (signal_resample - signal_min) / (signal_max - signal_min)
signal_quantized = np.round(signal_normalized * (quantization_levels - 1))
signal_quantized = signal_quantized / (quantization_levels - 1) * (signal_max - signal_min) + signal_min

plt.figure(figsize=(10, 6))
plt.subplot(3, 1, 1)
plt.plot(t_original, signal)
plt.title("Original Signal (8000 Hz sampling rate)")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")

plt.subplot(3, 1, 2)
plt.plot(t_resample, signal_resample)
plt.title("Resampled Signal (1000 Hz sampling rate)")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")

plt.subplot(3, 1, 3)
plt.plot(t_resample, signal_quantized)
plt.title("Quantized Signal (8 levels)")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()

print("Quantized Signal Levels:", signal_quantized)
