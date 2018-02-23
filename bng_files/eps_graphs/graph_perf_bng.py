## Functions

import IPython
import matplotlib 
#get_ipython().magic('matplotlib inline')
import sys,os
import copy
import random
path = os.path.abspath('../dev/')
if path not in sys.path:
    sys.path.append(path)

import numpy as np
import scipy as scipy
import scipy.misc as misc 
import matplotlib.pyplot as plt

from cycler import cycler

monochrome = (cycler('color', ['k']) * cycler('linestyle', ['-', '--', ':', '=.']) * cycler('marker', ['^',',', '.']))


plt.rcParams['axes.grid'] = True
plt.rcParams['axes.prop_cycle'] = monochrome
plt.rcParams['axes.spines.top'] = False
plt.rcParams['axes.spines.right'] = False
plt.rcParams['axes.spines.bottom'] = False
plt.rcParams['axes.spines.left'] = False

bar_cycle = (cycler('hatch', ['++++++', 'xxxxxx', '------', 'xxx', '\\\\']) *cycler('zorder', [14]))

styles = bar_cycle()

snmap = [0.6158344, 0.8967936, 1.6114536, 2.9460543, 4.948393, 5.9701824, 6.8265914]
dpdk = [0.9095854, 1.3183887, 2.4583342, 4.6926316, 9.017905, 9.9998288, 10.0050222]
netmap = [0.8523912, 1.2343993, 2.1573043, 3.8503649, 6.5491623, 7.8112216, 8.7416229]

xtick = np.arange(0,np.size(snmap))

xlabel = ['82', '128', '256', '512', '1024', '1280', '1518']
ytick = np.arange(0,10,10)


fig = plt.figure()
ax = fig.gca()

#ax.bar(xtick-0.3,v1, 0.3, label='Socket mmap', **next(styles))
#ax.bar(xtick,v3, 0.3, label='DPDK', **next(styles))
#ax.bar(xtick+0.3,v2, 0.3, label='Netmap', **next(styles))
#ax.grid()
#ax.bar(xtick-0.3,v1, 0.28, color="#73215C", edgecolor="black", linewidth=1 )
#ax.bar(xtick,v3, 0.28,color="#29B7B4", edgecolor="black")
#ax.bar(xtick+0.3,v2,0.28, color="#C8FE2E", edgecolor="black")
ax.bar(xtick,dpdk, 0.28, color="#73215C")
ax.bar(xtick,netmap, 0.28, color="#29B7B4" )
ax.bar(xtick,snmap, 0.28, color="#C8FE2E")

plt.xticks(xtick,xlabel )
#plt.title("Packet size (between CPE and BNG")
ax.set_ylabel('Throughput (Gbps)')
ax.set_xlabel('Packet size (between CPE and BNG)')

#plt.title("Performance comparison for diferents NIC drivers")
#ax.legend(["Socket-netmap", "Netmap", "DPDK"] )
ax.legend(["DPDK", "Netmap", "Socket-mmap"], edgecolor = "white" )

ax.set_prop_cycle(monochrome)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(True)
ax.spines['left'].set_visible(True)



plt.grid()
plt.show()
plt.savefig('bng_perform.eps', format='eps', dpi=500)
