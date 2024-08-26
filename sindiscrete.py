# import matplotlib.pyplot as plt
# import numpy as np

# # Generate discrete values for x
# x = np.linspace(0, 2 * np.pi, 10)  # 100 points between 0 and 2π

# # Compute the sine of each x value
# y = np.sin(x)

# # Create a scatter plot to represent the discrete nature of the sine wave
# plt.stem(x, y, use_line_collection=True)
# plt.hist(x,bins=30)
# # Add titles and labels
# plt.title('Discrete Sine Wave')
# plt.xlabel('x')
# plt.ylabel('sin(x)')

# # Show the plot
# plt.show()



import numpy as np
import matplotlib.pyplot as plt

# Define parameters  # Amplitude
f = 2 # Frequency in Hz  # Phase in radians
Fs = 70  # Sampling rate in samples per second
T = 0.5    # Duration in seconds

# Generate time values
t = np.linspace(0, T, int(Fs * T), endpoint=False)

# Compute sine wave values
y =np.sin(2 * np.pi * f * t )
fig,(ax1,ax2)=plt.subplots(2,1,figsize=(8,8))
ax1.stem(t, y, label='Sampled Sine Wave')
ax1.set_title('Sampled Sine Wave')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Amplitude')
# ax1.set_legend()
# ax1.set_grid(True)

ax2.step(t, y, where='mid', label='Sampled Sine Wave')
ax2.set_title('digital Sine Wave')
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Amplitude')
# ax2.legend()
# ax2.grid(True)
ax2.axhline(0, color='red', linewidth=1.5)
plt.tight_layout()
plt.show()
