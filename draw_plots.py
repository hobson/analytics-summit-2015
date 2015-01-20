import numpy as np
import matplotlib.pyplot as plt
import mpld3
from mpld3 import plugins

N = 1000
T = 0.1  # generated data sample period in seconds
Ts = 10  # sample period in seconds
Tt = 3   # tumble period
wt = 2 * np.pi / Tt # rad/s
A = 1367 / 100.  # Watts

t = T * np.arange(N)
ts = Ts * np.arange(N)
noise = 0.05 * A * np.random.randn(N)
signal = A * np.sin(wt*t) + noise
i_samples = np.array([int(t0) for t0 in np.floor((np.floor(t / Ts) * Ts / T))])
samples = signal[i_samples]
table = np.array([signal,samples])

xlabel, ylabel, title = 'Time (s)', 'Power (W)', 'Solar Panel Output'
fontdict={'fontsize': 12, 'fontweight': 'bold', 'family': 'sans-serif'}

fig1, ax1 = plt.subplots(1, 1)
lines = ax1.plot(t, table[0], linewidth=2.5)
ax1.xlabel(xlabel, fontdict=fontdict)
ax1.ylabel(ylabel, fontdict=fontdict)
plt.title(title, fontdict=fontdict)
ax1.grid(color='lightgray', alpha=0.7)
plt.show(fig=fig1, block=False)

# # only scatter plots seem to work with hover tooltips
labels = ["{0:.2g} W @ {1:.2g} s".format(s0, t0) for t0, s0  in zip(t, table[0])]
tooltip = plugins.PointLabelTooltip(lines[0], labels)
# plugins.clear(fig1)  # clear all plugins from the figure
plugins.connect(fig1, tooltip)
plt.savefig('fig1-1a-nyquist.png')
plt.show(block=False)
# mpld3.show()


fig2, ax2 = plt.subplots(1, 1)
ax2.plot(t, table.T, linewidth=2.5)
ax2.xlabel(xlabel, fontdict=fontdict)
ax2.ylabel(ylabel, fontdict=fontdict)
plt.title(title, fontdict=fontdict)
ax2.grid(color='lightgray', alpha=0.7)
plt.savefig('fig1-1b-nyquist.png')
plt.show(block=False)
# mpld3.show()
