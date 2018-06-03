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
#plt.rcParams['axes.axisbelow'] = True
#plt.rcParams['axes.axisbelow'] = True


#bar_cycle = (cycler('hatch', ['++++++', 'xxxxxx', '------', 'xxx', '\\\\']) *cycler('zorder', [14]))
bar_cycle = (cycler('hatch', ['\\\\\\', '.....']) *cycler('zorder', [14]))

styles = bar_cycle()

#snmap = [0.55962, 0.8967936, 1.6114536, 2.9460543, 4.948393, 5.9701824     ,np.nan,  0.358344, 0.6936, 1.11456, 1.543, 2.8493, 3.70124    ]
#dpdk = [0.9095854, 1.3183887, 2.4583342, 4.6926316, 9.017905, 9.9998288    ,np.nan,  1.59854, 2.1887, 4.4582, 6.9236, 9.9195, 9.9998      ]
#netmap = [0.8523912, 1.2343993, 2.1573043, 3.8503649, 6.5491623, 7.8112216 ,np.nan,  0.81291, 1.833993, 4.157343, 5.50649, 8.54916, 8.91216]
###n
#snmap = [0.55962, 0.8967936, 1.6114536, 2.9460543, 4.948393, 5.9701824     ,np.nan,  0.358344, 0.606, 0.81456, 1.83, 3.2493, 4.50124    ]
#dpdk = [0.9095854, 1.3183887, 2.4583342, 4.6926316, 9.017905, 9.9998288    ,np.nan,  1.59854, 2.1887, 4.4582, 6.9236, 9.9195, 9.9998      ]
#netmap = [0.8523912, 1.2343993, 2.1573043, 3.8503649, 6.5491623, 7.8112216 ,np.nan,  1.1291, 2.133993, 4.57343, 6.50649, 9.54916, 9.31216]

# netmap DL 2.172 3.593 6.327 9.573 9.781 9.823


snmap = [0.5945,0.8496,1.4905,2.9621,5.1309,6.5449 ,np.nan, 0.0900,0.3210,0.5110,2.2154,4.3171,5.4201 ]
dpdk = [1.1335,1.6696,3.2170,5.9669,9.9863,10.0049 ,np.nan, 2.4277,4.4272,7.6768,9.5736,9.7798,9.8238 ]

netmap =[0.6890,0.9894,1.7480,3.1499,5.5310,6.6292 ,np.nan, 1.7101,3.0008,4.6084,9.5732,9.7802,9.8238 ] 



 

#cp_snmap =  [0.358344, 0.67936, 1.11456, 1.543, 2.8493, 3.70124 ]
#cp_dpdk =   [0.909854, 2.1887, 4.4582, 6.9236, 9.9195, 9.9998]
#cp_netmap = [0.81291, 1.833993, 4.157343, 5.50649, 8.54916, 8.91216]

xtick = np.arange(0,np.size(snmap))

dpdk_p= dpdk
netmap_p=netmap
socket_p=snmap

cores =     ["82","128","256","512","1024","1280","","64","128","256","512","1024","1280"]
numb = [82,128,256,512,1024,1280,0,64,128,256,512,1024,1280]

for i in range(0,len(snmap)):
     if dpdk[i] != np.nan: 
                 print (str(netmap[i])) 
                 dpdk_p[i]=(dpdk[i]*1000)/((20+numb[i])*8)
                 netmap_p[i]=(netmap[i]*1000)/((20+numb[i])*8)
                 print (str(numb[i])+ "  result:  " + str(netmap_p[i]) )
                 socket_p[i]=(snmap[i]*1000)/((20+numb[i])*8)
     else: 
                 np.nan
ind = np.arange(len(cores))
width = 0.3
fig = plt.figure(figsize=(7,3.3))
ax = fig.add_subplot(111)
#ax.bar([p + width for p in ind], dpdk_p, width, color="#AFD2E9", edgecolor="black")
ax.bar(xtick-0.3, socket_p, width, color="#FCD0A1",edgecolor="black",hatch="..", lw=1., zorder = 0)
ax.bar(xtick, netmap_p, width, color="#B1B695", edgecolor="black", lw=1., zorder = 0)
ax.bar(xtick+0.3, dpdk_p, width, color="#AFD2E9", edgecolor="black",hatch="OO", lw=1., zorder = 0)
        


ax.set_xticks(ind+0.1*(width/3))
xticks = ax.xaxis.get_major_ticks()

xticks[6].set_visible(False)
ax.set_xticklabels(cores)
ax.set_ylabel('Throughput (Mpps)',fontsize=9)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')
ax.set_xlabel("Packet size(bytes)", fontsize=9)
ax.xaxis.set_label_coords(0.3,-0.32)
ax.yaxis.grid(linestyle='--')
ax.set_axisbelow(True)
ax.set_xlabel("Packet size (Bytes)", fontsize=9)
ax.xaxis.set_label_coords(0.5,-0.2)


#xlabel = ['82', '128', '256', '512', '1024', '1280', '1518']
ytick = np.arange(0,10,10)
plt.tight_layout(pad=0.3, w_pad=0.5, h_pad=1)
#f, (ax) = plt.subplots(1, 2, sharey=True, )

#fig = plt.figure()
#ax = fig.gca()

#ax.bar(xtick-0.3,v1, 0.3, label='Socket mmap', **next(styles))
#ax.bar(xtick,v3, 0.3, label='DPDK', **next(styles))
#ax.bar(xtick+0.3,v2, 0.3, label='Netmap', **next(styles))
#ax.grid()
#ax.bar(xtick-0.3,v1, 0.28, color="#73215C", edgecolor="black", linewidth=1 )
#ax.bar(xtick,v3, 0.28,color="#29B7B4", edgecolo="black")
#ax.bar(xtick+0.3,v2,0.28, color="#C8FE2E", edgecolor="black")

#socket_cl= "#FCD0A1"
#dpdk_cl= "#AFD2E9"
#netmap_cl= "#B1B695"
#
#
#ax.bar(xtick-0.3,socket_p, 0.3,   color="#FCD0A1",edgecolor="black",hatch="..", lw=1., zorder = 0 )                  
#ax.bar(xtick,netmap_p, 0.3,      color="#B1B695", edgecolor="black",lw=1., zorder = 0 )
#ax.bar(xtick+0.3,dpdk_p, 0.3,    color="#AFD2E9", edgecolor="black", hatch="OO", lw=1., zorder = 0)              
#ax.axes.get_xaxis().set_visible(False)
#
#
#ax2.bar(xtick-0.3,tcp_socket_p, 0.3,  color=socket_cl ,edgecolor="black",hatch="..", lw=1., zorder = 0 )                  
#ax2.bar(xtick,tcp_netmap_p, 0.3,     color=netmap_cl, edgecolor="black",lw=1., zorder = 0)
#ax2.bar(xtick+0.3,tcp_dpdk_p, 0.3,   color=dpdk_cl, edgecolor="black",hatch="OO", lw=1., zorder = 0 )              
#
#ax2.axes.get_xaxis().set_visible(False)
#ax2.axes.get_yaxis().set_visible(False)

#ticklabelpad = mpl.rcParams['xtick.major.pad']
#xposi=240
#yposi= 0 
#ax.annotate ("82       128       256      512     1024     1280", xy=(1,0), xytext=(-xposi, -ticklabelpad-yposi), ha='left', va='top',   fontsize=11, xycoords='axes fraction', textcoords='offset points')
#ax.annotate("Packet size (For UL, between CPE and BNG)" , xy=(1,0), xytext=(-xposi+5, -ticklabelpad-yposi-13), ha='left', va='top',   fontsize=10, xycoords='axes fraction', textcoords='offset points')
#ax2.annotate("82       128       256      512     1024     1280", xy=(1,0), xytext=(-xposi, -ticklabelpad-yposi), ha='left', va='top',   fontsize=11, xycoords='axes fraction', textcoords='offset points')
#ax2.annotate("Packet size (For DL, between Server and BNG)" , xy=(1,0), xytext=(-xposi+5, -ticklabelpad-yposi-13), ha='left', va='top',   fontsize=10, xycoords='axes fraction', textcoords='offset points')
#


#plt.title("Packet size (between CPE and BNG")
ax.set_ylabel('Throughput (Mpps)')

#plt.title("Performance comparison for diferents NIC drivers")
leg = ax.legend(["Socket-mmap", "Netmap", "DPDK"], edgecolor = "white" )
leg.get_frame().set_alpha(0)
#ax.legend(["Netmap", "Socket-mmap", "DPDK"], edgecolor = "white" )

ticklabelpad = mpl.rcParams['xtick.major.pad']
xposi=290
yposi= 15 
ax.annotate ("(For UL, between CPE and BNG)", xy=(1,0), xytext=(-xposi-90, -ticklabelpad-yposi), ha='left', va='top',   fontsize=8, xycoords='axes fraction', textcoords='offset points')
ax.annotate ("(For DL, between Server and BNG)", xy=(1,0), xytext=(-xposi+100, -ticklabelpad-yposi), ha='left', va='top',   fontsize=8, xycoords='axes fraction', textcoords='offset points')
ax.set_prop_cycle(monochrome)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(True)
ax.spines['left'].set_visible(True)
ax.yaxis.grid(linestyle='--')
ax.set_axisbelow(True)

#ax2.spines['bottom'].set_visible(True)
#ax2.yaxis.grid(linestyle='--')
#ax2.set_axisbelow(True)

#plt.grid()
#plt.show()
plt.savefig('/home/lion/bng_perform.eps', format='eps', dpi=50)
























































































































































#plt.savefig('bng_perform.png', format='png', dpi=400)
