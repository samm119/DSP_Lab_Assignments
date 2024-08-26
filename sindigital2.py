import numpy as np
import matplotlib.pyplot as plt

# Parameters
frequency = 200  # Frequency of the sine wave in Hz
duration = 0.5   # Duration of the sine wave in seconds
sampling_rate = 5000  # Sampling rate in Hz
quantization_bits = 16  # Number of bits for quantization

# Generate the time vector
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

# Generate the sine wave
sine_wave = np.sin(2 * np.pi * frequency * t)

# Quantize the sine wave
max_amplitude = 2**(quantization_bits - 1) - 1
quantized_sine_wave = np.round(sine_wave * max_amplitude).astype(np.int16)

# Plotting
plt.figure(figsize=(10, 8))

# Original sine wave
plt.subplot(3, 1, 1)
plt.plot(t, sine_wave, label='Original Sine Wave')
plt.title('Original Sine Wave')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)

# Quantized sine wave
plt.subplot(3, 1, 2)
plt.plot(t, quantized_sine_wave / max_amplitude, label='Quantized Sine Wave')
plt.title('Quantized Sine Wave')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)

# Residual error
residual_error = sine_wave - quantized_sine_wave / max_amplitude
plt.subplot(3, 1, 3)
plt.plot(t, residual_error, label='Residual Error')
plt.title('Residual Error')
plt.xlabel('Time [s]')
plt.ylabel('Error')
plt.grid(True)

plt.tight_layout()
plt.show()
