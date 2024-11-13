from matplotlib import pyplot as plt, patches
import numpy as np

fig = plt.figure()
ax = fig.subplots()

ymp = patches.Circle((0, 0), radius=1, fill=False, color='black', linestyle='--')
ax.add_patch(ymp)

ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.axis('equal')

kulmat_asteina = np.array([30, 45, 60, 90, 120, 150, 180, 270])

kulmat_radiaaneina = np.deg2rad(kulmat_asteina)

x_pisteet = np.cos(kulmat_radiaaneina)
y_pisteet = np.sin(kulmat_radiaaneina)

plt.scatter(x_pisteet, y_pisteet, color='blue', marker='X')

for i, kulma in enumerate(kulmat_asteina):
    plt.annotate(f'{kulma}°',
                 xy=(x_pisteet[i], y_pisteet[i]), xycoords='data',
                 xytext=(+10, +10), textcoords='offset points', fontsize=10,
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0.2"))

plt.show()
