import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FuncFormatter

x = np.linspace(-3 * np.pi, 3 * np.pi, 1000)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.figure(figsize=(6.4 * 3, 4.8))

plt.plot(x, y_sin, color="blue", linestyle="--", label="sin(x)")
plt.plot(x, y_cos, color="red", linestyle=":", label="cos(x)")

plt.legend()

def pi_formatter(x, pos):
    denominator = int(np.pi)
    if x == 0:
        return "0"
    elif x == np.pi:
        return "π"
    elif x == -np.pi:
        return "-π"
    elif x % np.pi == 0:
        return f"{int(x / np.pi)}π"
    elif x % (np.pi / 2) == 0:
        return f"{int(2 * x / np.pi)}/2 π"
    else:
        return f"{x / np.pi:.1g}π"

plt.gca().xaxis.set_major_locator(MultipleLocator(base=np.pi / 2))
plt.gca().xaxis.set_major_formatter(FuncFormatter(pi_formatter))

plt.show()
