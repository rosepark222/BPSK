import numpy as np
import matplotlib.pyplot as plt

# --- 1. Setup Parameters ---
fs = 1000          # Sampling frequency (Hz)
T = 0.1            # Bit duration (seconds)
t = np.arange(0, T, 1/fs)
f0 = 50            # Space frequency (Bit 0)
f1 = 150           # Mark frequency (Bit 1)
bits = [1, 0, 1, 1, 0] # Input data

# --- 2. Modulation ---
signal = []
for bit in bits:
    freq = f1 if bit == 1 else f0
    signal.extend(np.cos(2 * np.pi * freq * t))
signal = np.array(signal)

# --- 3. Demodulation (Coherent Correlation) ---
decoded_bits = []
samples_per_bit = len(t)

for i in range(len(bits)):
    # Extract segment for current bit
    segment = signal[i*samples_per_bit : (i+1)*samples_per_bit]
    
    # Correlate with local reference carriers
    corr1 = np.sum(segment * np.cos(2 * np.pi * f1 * t))
    corr0 = np.sum(segment * np.cos(2 * np.pi * f0 * t))
    
    # Decision: choose frequency with higher correlation
    decoded_bits.append(1 if corr1 > corr0 else 0)

print(f"Original: {bits}")
print(f"Decoded:  {decoded_bits}")
