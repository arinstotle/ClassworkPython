import hashlib
import numpy as np
import matplotlib.pyplot as plt

def noise(x, y):
    hashval = hashlib.sha256(f"{x},{y}".encode('utf-8')).hexdigest()
    return int(hashval, 16) % 100 / 100.0

noise_array = np.fromfunction(np.vectorize(noise), (1000, 1000))

plt.figure(figsize=(18,6))
plt.plot(noise_array[0, :], color='red')
# plt.plot(noise_array[1, :], color='yellow')
# plt.plot(noise_array[2, :], color='green')
# plt.plot(noise_array[3, :], color='blue')
plt.show()