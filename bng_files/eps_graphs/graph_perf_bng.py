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
import matplotlib as mpl

from cycler import cycler

monochrome = (cycler('color', ['k']) * cycler('linestyle', ['-', '--', ':', '=.']) * cycler('marker', ['^',',', '.']))


#plt.rcParams['axes.grid'] = True
plt.rcParams['axes.prop_cycle'] = monochrome
plt.rcParams['axes.spines.top'] = False
plt.rcParams['axes.spines.right'] = False
plt.rcParams['axes.spines.bottom'] = False
plt.rcParams['axes.spines.left'] = False
plt.rcParams['figure.figsize'] = 10, 3.5

#bar_cycle = (cycler('hatch', ['++++++', 'xxxxxx', '------', 'xxx', '\\\\']) *cycler('zorder', [14]))
bar_cycle = (cycler('hatch', ['\\\\\\', '.....']) *cycler('zorder', [14]))

styles = bar_cycle()

snmap = [0.55962, 0.8967936, 1.6114536, 2.9460543, 4.948393, 5.9701824 ]
dpdk = [0.9095854, 1.3183887, 2.4583342, 4.6926316, 9.017905, 9.9998288]
netmap = [0.8523912, 1.2343993, 2.1573043, 3.8503649, 6.5491623, 7.8112216]

tcp_snmap = [0.358344, 0.67936, 1.11456, 1.543, 2.8493, 3.70124 ]
tcp_dpdk = [0.909854, 2.1887, 4.4582, 6.9236, 9.9195, 9.9998]
tcp_netmap = [0.81291, 1.833993, 4.157343, 5.50649, 8.54916, 8.91216]

xtick = np.arange(0,np.size(snmap))

#xlabel = ['82', '128', '256', '512', '1024', '1280', '1518']
ytick = np.arange(0,10,10)

f, (ax,ax2) = plt.subplots(1, 2, sharey=True, )

#fig = plt.figure()
#ax = fig.gca()

#ax.bar(xtick-0.3,v1, 0.3, label='Socket mmap', **next(styles))
#ax.bar(xtick,v3, 0.3, label='DPDK', **next(styles))
#ax.bar(xtick+0.3,v2, 0.3, label='Netmap', **next(styles))
#ax.grid()
#ax.bar(xtick-0.3,v1, 0.28, color="#73215C", edgecolor="black", linewidth=1 )
#ax.bar(xtick,v3, 0.28,color="#29B7B4", edgecolo="black")
#ax.bar(xtick+0.3,v2,0.28, color="#C8FE2E", edgecolor="black")
ax.bar(xtick-0.3,snmap, 0.3,   color="#E0E0E0",edgecolor="black")                  
ax.bar(xtick,netmap, 0.3,      color="white", edgecolor="black", **next(styles))
ax.bar(xtick+0.3,dpdk, 0.3,    color="gray", edgecolor="black", **next(styles))              
ax.axes.get_xaxis().set_visible(False)

ax2.bar(xtick-0.3,tcp_snmap, 0.3,  color="#E0E0E0",edgecolor="black")                  
ax2.bar(xtick,tcp_netmap, 0.3,     color="white", edgecolor="black", **next(styles))
ax2.bar(xtick+0.3,tcp_dpdk, 0.3,   color="gray", edgecolor="black", **next(styles))              

ax2.axes.get_xaxis().set_visible(False)
ax2.axes.get_yaxis().set_visible(False)

ticklabelpad = mpl.rcParams['xtick.major.pad']
xposi=240
yposi= 4 
ax.annotate ("82       128       256      512     1024     1280", xy=(1,0), xytext=(-xposi, -ticklabelpad-yposi), ha='left', va='top',   fontsize=11, xycoords='axes fraction', textcoords='offset points')
ax.annotate("Packet size (For UL, between CPE and BNG)" , xy=(1,0), xytext=(-xposi+5, -ticklabelpad-yposi-13), ha='left', va='top',   fontsize=10, xycoords='axes fraction', textcoords='offset points')
ax2.annotate("82       128       256      512     1024     1280", xy=(1,0), xytext=(-xposi, -ticklabelpad-yposi), ha='left', va='top',   fontsize=11, xycoords='axes fraction', textcoords='offset points')
ax2.annotate("Packet size (For DL, between Server and BNG)" , xy=(1,0), xytext=(-xposi+5, -ticklabelpad-yposi-13), ha='left', va='top',   fontsize=10, xycoords='axes fraction', textcoords='offset points')



#plt.title("Packet size (between CPE and BNG")
ax.set_ylabel('Gbps')
ax.set_xlabel('Packet size (between CPE and BNG)')

#plt.title("Performance comparison for diferents NIC drivers")
#ax.legend(["Socket-netmap", "Netmap", "DPDK"] )
ax.legend(["DPDK", "Netmap", "Socket-mmap"], edgecolor = "white" )

ax.set_prop_cycle(monochrome)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(True)
ax.spines['left'].set_visible(True)

ax2.spines['bottom'].set_visible(True)

#plt.grid()
#plt.show()
#plt.savefig('bng_perform.eps', format='eps', dpi=400)
plt.savefig('bng_perform.png', format='png', dpi=400)
