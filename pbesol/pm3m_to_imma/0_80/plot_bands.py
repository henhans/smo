import matplotlib.pyplot as plt
from matplotlib import rcParamsDefault
import numpy as np

plt.rcParams["figure.dpi"]=150
plt.rcParams["figure.facecolor"]="white"
#plt.rcParams["figure.figsize"]=(8, 6)

# load data
data = np.loadtxt('smo_bands.dat.gnu')

k = np.unique(data[:, 0])
bands = np.reshape(data[:, 1], (-1, len(k)))

for band in range(len(bands)):
    plt.plot(k, bands[band, :], linewidth=1, alpha=0.5, color='k')
plt.xlim(min(k), max(k))

# Fermi energy
plt.axhline(13.5914, linestyle=(0, (5, 5)), linewidth=0.75, color='k', alpha=0.5)
# High symmetry k-points (check bands_pp.out)
plt.axvline(0.7066, linewidth=0.75, color='k', alpha=0.5)
plt.axvline(1.0604, linewidth=0.75, color='k', alpha=0.5)
plt.axvline(1.5607, linewidth=0.75, color='k', alpha=0.5)
plt.axvline(2.1723, linewidth=0.75, color='k', alpha=0.5)
plt.axvline(2.7851, linewidth=0.75, color='k', alpha=0.5)
plt.axvline(3.2840, linewidth=0.75, color='k', alpha=0.5)
# text labels
plt.xticks(ticks= [0, 0.7066, 1.0604, 1.5607, 2.1723, 2.7851, 3.2840], \
           labels=['$\Gamma$', 'X', 'M', '$\Gamma$', 'T', 'W'])
plt.ylabel("Energy (eV)")
#plt.text(2.3, 5.6, 'Fermi energy', fontsize= small)
plt.show()
