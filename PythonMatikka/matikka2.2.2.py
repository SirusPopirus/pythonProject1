import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3 * np.pi, 3 * np.pi, 1000)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.figure(figsize=(6.4 * 3, 4.8))

plt.plot(x, y_sin, color="blue", linestyle="--", label="sin(x)")
plt.plot(x, y_cos, color="red", linestyle=":", label="cos(x)")

plt.legend()

plt.show()
