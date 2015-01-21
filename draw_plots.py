import numpy as np
import matplotlib.pyplot as plt
# import mpld3
from mpld3 import plugins

N = 800
T = 0.1  # generated data sample period in seconds
Ts = 4   # sample period in seconds
Tt = 3   # tumble period in seconds
wt = 2 * np.pi / Tt # rad/s
A = 1367 / 100.  # Watts

t = T * np.arange(N)
ts = Ts * np.arange(N)
noise = 0.05 * A * np.random.randn(N)
signal = A * np.sin(wt*t) + noise
i_samples = np.array([int(t0) for t0 in np.floor((np.floor(t / Ts) * Ts / T))])
samples = signal[i_samples]

def exponential_smoother(x, alpha=0.5, beta=None):
    beta = beta or 1 - alpha
    y = [0]  
    for x0 in x[:-1]:
        y += [alpha * x0 + beta * y[-1]]
    return y

smoothed = np.array(exponential_smoother(signal, alpha=0.01))
smoothed_samples = smoothed[i_samples]
t = t[:N/2]
table = np.array([signal[N/2:],samples[N/2:],smoothed[N/2:],smoothed_samples[N/2:]])

xlabel, ylabel, title = 'Time (s)', 'Power (W)', 'Solar Panel Output'
fontdict={'fontsize': 12, 'fontweight': 'bold', 'family': 'sans-serif'}

fig1, ax1 = plt.subplots(1, 1)
lines = ax1.plot(t, table[1], 'r', linewidth=2.5)
plt.xlabel(xlabel, fontdict=fontdict)
plt.ylabel(ylabel, fontdict=fontdict)
plt.title(title, fontdict=fontdict)
plt.grid(color='gray')
plt.show(block=False)

# # only scatter plots seem to work with hover tooltips
labels = ["{0:.2g} W @ {1:.2g} s".format(s0, t0) for t0, s0  in zip(t, table[0])]
tooltip = plugins.PointLabelTooltip(lines[0], labels)
# plugins.clear(fig1)  # clear all plugins from the figure
plugins.connect(fig1, tooltip)
plt.savefig('fig1-1a-nyquist.png')
plt.show(block=False)
# mpld3.show()


fig2, ax2 = plt.subplots(1, 1)
ax2.plot(t, table[0], 'b', t, table[1], 'r', linewidth=2.5)
plt.xlabel(xlabel, fontdict=fontdict)
plt.ylabel(ylabel, fontdict=fontdict)
plt.title(title, fontdict=fontdict)
plt.grid(color='gray')
plt.legend(['Truth', 'Sampled'])
plt.savefig('fig1-1b-nyquist.png')
plt.show(block=False)
# mpld3.show()


fig, ax = plt.subplots(1, 1)
lines = ax.plot(t, table[3], 'r', linewidth=2.5)
plt.xlabel(xlabel, fontdict=fontdict)
plt.ylabel(ylabel, fontdict=fontdict)
plt.title(title, fontdict=fontdict)
plt.grid(color='gray')
plt.savefig('fig1-1c-antialiasing.png')
plt.show(block=False)



fig, ax = plt.subplots(1, 1)

ax.plot(t, table[2], 'b', t, table[3], 'r', linewidth=2.5)
plt.xlabel(xlabel, fontdict=fontdict)
plt.ylabel(ylabel, fontdict=fontdict)
plt.title('With Anti-Aliasing Filter', fontdict=fontdict)
plt.grid(color='gray')
plt.legend(['Filtered', 'Sampled'])
plt.savefig('fig1-1d-antialiasing.png')
plt.show(block=False)

from scipy import signal
i_rand = np.arange(N)[np.rand(N) <= 0.2]  # randomly select 20% of the sample time indices
t_rand = (T * np.arange(N))[i_rand]
samples_rand = signal[t_rand]
freqs = 0.1 * np.arange(40) / Tt  # from a tenth the tumble rate to 4x the tumble rate
periodogram = signal.lombscargle(t_rand, samples_rand)