import numpy as np

# Step 1: Define the input signal and filter coefficients (for example, a simple moving average filter)
input_signal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Input signal
coefficients = [0.2, 0.2, 0.2, 0.2, 0.2]  # FIR filter coefficients (a simple 5-point moving average)

# Step 2: Initialize accumulator output
output_signal = np.zeros(len(input_signal) - len(coefficients) + 1)

# Step 3: Accumulate the sum of products of input samples and filter coefficients
for i in range(len(output_signal)):
    accumulator = 0  # Initialize the accumulator for each output point
    for j in range(len(coefficients)):
        accumulator += input_signal[i + j] * coefficients[j]  # Multiply and accumulate
    output_signal[i] = accumulator  # Store the accumulated result as the output

# Step 4: Display the output signal (filtered signal)
print("Filtered Output Signal:", output_signal)
