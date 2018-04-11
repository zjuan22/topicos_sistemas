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
markers = []
line_styles = markers + [
    r'$\lambda$',
    r'$\bowtie$',
    r'$\clubsuit$',
    r'$\circlearrowleft$',
    r'$\clubsuit$',
    r'$\langle$',
r'$\gamma$']
markers = ["*","^","."]
linestyles = ['-', '--', '-.', ':']

#plt.rcParams['axes.grid'] = True
plt.rcParams['axes.prop_cycle'] = monochrome
plt.rcParams['axes.spines.top'] = False
plt.rcParams['axes.spines.right'] = False
plt.rcParams['axes.spines.bottom'] = True
plt.rcParams['axes.spines.left'] = False
#plt.rcParams['figure.figsize'] = 15, 3.4 
plt.rcParams['figure.figsize'] = 20, 4

#plt.axes().get_yaxis().set_visible(True)

#bar_cycle = (cycler('hatch', ['++++++', 'xxxxxx', '------', 'xxx', '\\\\']) *cycler('zorder', [14]))
#bar_cycle = (cycler('hatch', ['\\\\\\']) *cycler('zorder', [14]))
bar_cycle = (cycler('hatch', ['\\\\\\', '']) *cycler('zorder', [14]))

styles = bar_cycle()

snmap_64 =  [ 0.1349, 0.1925, 0.0376, 0.0271, 0.0004 ]   
dpdk_64 =   [ 9.9043 ,9.9044, 9.9044, 9.9075, 9.9742 ] 
netmap_64 = [ 5.5006 ,7.1007, 6.5135, 5.4042, 5.358 ] 

snmap_128 = [ 0.1692, 0.3466, 0.3316, 0.0007, 0.0426 ] 
dpdk_128 =  [ 9.9964, 9.9957, 9.9957, 9.9957, 9.9934] 
netmap_128 =[ 8.6587, 9.9955, 9.9957, 8.8772, 8.3508] 

snmap_256 = [ 0.4326, 0.6183, 0.7095, 0.6235, 0.8818 ] 
dpdk_256 =  [ 9.9039, 9.9042, 9.9042, 9.9042, 9.9042] 
netmap_256 =[ 9.904 , 9.9038, 9.9042, 9.9066, 9.9061 ]



 
pps_smmap_64 =   [(snmap_64[0]*1000)/((20+64)*8), (snmap_64[1]*1000)/((20+64)*8), (snmap_64[2]*1000)/((20+64)*8), (snmap_64[3]*1000)/((20+64)*8), (snmap_64[4]*1000)/((20+64)*8)  ]  
pps_smmap_128 =  [(snmap_128[0]*1000)/((20+128)*8), (snmap_128[1]*1000)/((20+128)*8), (snmap_128[2]*1000)/((20+128)*8), (snmap_128[3]*1000)/((20+128)*8), (snmap_128[4]*1000)/((20+128)*8)  ]  
pps_smmap_256 =  [(snmap_256[0]*1000)/((20+256)*8), (snmap_256[1]*1000)/((20+256)*8), (snmap_256[2]*1000)/((20+256)*8), (snmap_256[3]*1000)/((20+256)*8), (snmap_256[4]*1000)/((20+256)*8)  ]  

pps_dpdk_64 =    [(dpdk_64[0]*1000)/((20+64)*8),    (dpdk_64[1]*1000)/((20+64)*8), (dpdk_64[2]*1000)/((20+64)*8), (dpdk_64[3]*1000)/((20+64)*8), (dpdk_64[4]*1000)/((20+64)*8)  ]  
pps_dpdk_128 =   [(dpdk_128[0]*1000)/((20+128)*8), (dpdk_128[1]*1000)/((20+128)*8), (dpdk_128[2]*1000)/((20+128)*8), (dpdk_128[3]*1000)/((20+128)*8), (dpdk_128[4]*1000)/((20+128)*8)  ]  
pps_dpdk_256 =   [(dpdk_256[0]*1000)/((20+256)*8), (dpdk_256[1]*1000)/((20+256)*8), (dpdk_256[2]*1000)/((20+256)*8), (dpdk_256[3]*1000)/((20+256)*8), (dpdk_256[4]*1000)/((20+256)*8)  ]  

pps_netmap_64 =  [(netmap_64[0]*1000)/((20+64)*8), (netmap_64[1]*1000)/((20+64)*8), (netmap_64[2]*1000)/((20+64)*8), (netmap_64[3]*1000)/((20+64)*8), (netmap_64[4]*1000)/((20+64)*8)  ]  
pps_netmap_128 = [(netmap_128[0]*1000)/((20+128)*8), (netmap_128[1]*1000)/((20+128)*8), (netmap_128[2]*1000)/((20+128)*8), (netmap_128[3]*1000)/((20+128)*8), (netmap_128[4]*1000)/((20+128)*8)  ]  
pps_netmap_256 = [(netmap_256[0]*1000)/((20+256)*8), (netmap_256[1]*1000)/((20+256)*8), (netmap_256[2]*1000)/((20+256)*8), (netmap_256[3]*1000)/((20+256)*8), (netmap_256[4]*1000)/((20+256)*8)  ]  

#pps_smmap_64 =   [  0.1983777, 0.2844025,  0.0829268, 0.0373987,  0.0006123 ]  
#pps_smmap_128 =  [  0.1397185, 0.2181505,  0.1179953, 0.2289735,  0.0336097 ]  
#pps_smmap_256 =  [  0.1505477, 0.2772149,  0.1054852, 0.2785108,  0.3126653 ]  
#
#pps_dpdk_64 =    [ 14.8883949,14.8879949, 14.887872, 14.8920443, 14.7844936 ]
##pps_dpdk_128 =   [  8.4421463, 8.4417797,  8.4417797, 8.4417797,  8.4408202 ]
#pps_dpdk_128 =   [  8.4421463, 8.4417797,  8.4417797, 8.4417797,  8.4408202 ]
#pps_dpdk_256 =   [  4.5311221, 4.5309885,  4.5309885, 4.5309885,  4.5309885 ]   
#
#pps_netmap_64 =  [  8.1812423, 9.7615546,  9.6330745, 7.9977912,  7.9628553 ] 
#pps_netmap_128 = [  7.302157 , 8.4417622,  8.0220733, 7.4567338,  7.0401164 ]  
#pps_netmap_256 = [  4.1330245, 4.5308948,  4.5308948, 4.5318384,  4.531815 ] 


v6_smmap_64 =   [ 0.13,   0.0616, 0.0895,  0.0774, 0.1507 ]
v6_smmap_128 =  [ 0.235,  0.459,  0.0006,  0.479,  0.0989 ]
v6_smmap_256 =  [ 0.437,  0.7027, 0.7279,  0.8658, 0.9242 ] 
                                                     
v6_dpdk_64 =    [ 9.9053 ,9.9047, 9.9972, 10.0085, 9.957 ]
v6_dpdk_128 =   [ 9.9957 ,9.9957, 9.9957,  9.9957, 9.9957 ]
v6_dpdk_256 =   [ 9.9042 ,9.9042, 9.9042,  9.9042, 9.9042 ]
                                                     
v6_netmap_64 =  [ 6.9165 ,6.0503, 5.7415,  4.872,  4.935 ]
v6_netmap_128 = [ 9.9955 ,9.824,  8.3625,  7.7755, 6.4519 ]
v6_netmap_256 = [ 9.9584 ,9.9054, 9.9042,  9.9059, 7.6802 ]

v6_pps_smmap_64 =   [(v6_smmap_64[0]*1000)/((20+64)*8), (v6_smmap_64[1]*1000)/((20+64)*8), (v6_smmap_64[2]*1000)/((20+64)*8), (v6_smmap_64[3]*1000)/((20+64)*8), (v6_smmap_64[4]*1000)/((20+64)*8)  ]  
v6_pps_smmap_128 =  [(v6_smmap_128[0]*1000)/((20+128)*8), (v6_smmap_128[1]*1000)/((20+128)*8), (v6_smmap_128[2]*1000)/((20+128)*8), (v6_smmap_128[3]*1000)/((20+128)*8), (v6_smmap_128[4]*1000)/((20+128)*8)  ]  
v6_pps_smmap_256 =  [(v6_smmap_256[0]*1000)/((20+256)*8), (v6_smmap_256[1]*1000)/((20+256)*8), (v6_smmap_256[2]*1000)/((20+256)*8), (v6_smmap_256[3]*1000)/((20+256)*8), (v6_smmap_256[4]*1000)/((20+256)*8)  ]  

v6_pps_dpdk_64 =   [(v6_dpdk_64[0]*1000)/((20+64)*8), (v6_dpdk_64[1]*1000)/((20+64)*8), (v6_dpdk_64[2]*1000)/((20+64)*8), (v6_dpdk_64[3]*1000)/((20+64)*8), (v6_dpdk_64[4]*1000)/((20+64)*8)  ]  
v6_pps_dpdk_128 =  [(v6_dpdk_128[0]*1000)/((20+128)*8), (v6_dpdk_128[1]*1000)/((20+128)*8), (v6_dpdk_128[2]*1000)/((20+128)*8), (v6_dpdk_128[3]*1000)/((20+128)*8), (v6_dpdk_128[4]*1000)/((20+128)*8)  ]  
v6_pps_dpdk_256 =  [(v6_dpdk_256[0]*1000)/((20+256)*8), (v6_dpdk_256[1]*1000)/((20+256)*8), (v6_dpdk_256[2]*1000)/((20+256)*8), (v6_dpdk_256[3]*1000)/((20+256)*8), (v6_dpdk_256[4]*1000)/((20+256)*8)  ]  

v6_pps_netmap_64 =   [(v6_netmap_64[0]*1000)/((20+64)*8), (v6_netmap_64[1]*1000)/((20+64)*8), (v6_netmap_64[2]*1000)/((20+64)*8), (v6_netmap_64[3]*1000)/((20+64)*8), (v6_netmap_64[4]*1000)/((20+64)*8)  ]  
v6_pps_netmap_128 =  [(v6_netmap_128[0]*1000)/((20+128)*8), (v6_netmap_128[1]*1000)/((20+128)*8), (v6_netmap_128[2]*1000)/((20+128)*8), (v6_netmap_128[3]*1000)/((20+128)*8), (v6_netmap_128[4]*1000)/((20+128)*8)  ]  
v6_pps_netmap_256 =  [(v6_netmap_256[0]*1000)/((20+256)*8), (v6_netmap_256[1]*1000)/((20+256)*8), (v6_netmap_256[2]*1000)/((20+256)*8), (v6_netmap_256[3]*1000)/((20+256)*8), (v6_netmap_256[4]*1000)/((20+256)*8)  ]  

total_smmap_64 = [snmap_64[0], snmap_64[0], snmap_64[0], snmap_64[0], snmap_64[0],0, v6_snmap_64[0], v6_snmap_64[0], v6_snmap_64[0], v6_snmap_64[0], v6_snmap_64[0]] 
total_smmap_128 = [snmap_128[0], snmap_128[0], snmap_128[0], snmap_128[0], snmap_128[0],0, v6_snmap_128[0], v6_snmap_128[0], v6_snmap_128[0], v6_snmap_128[0], v6_snmap_128[0]] 
total_smmap_256 = [snmap_256[0], snmap_256[0], snmap_256[0], snmap_256[0], snmap_256[0],0, v6_snmap_256[0], v6_snmap_256[0], v6_snmap_256[0], v6_snmap_256[0], v6_snmap_256[0]] 

entries = ["100","1k","10k","100k","1M","","100","1k","10k","100k","1M"]

#ind = np.arange(len(cores))

xtick = np.arange(0,np.size(entries) )

fig = plt.figure()
ax = fig.add_subplot(111)

ax.bar(xtick-0.34, snmap_64  ,0.34,   color="#E0E0E0", edgecolor="black")
ax.bar(xtick,netmap_64   , 0.34,       color="white", edgecolor="black", **next(styles))
ax.bar(xtick+0.34, dpdk_64 , 0.34,     color="#606060",edgecolor="black", **next(styles))
ax.set_ylabel('Gbps')
ax.set_ylim([0, y1_lim])
ax.yaxis.tick_left() # doesnt work :(
ax.axes.get_xaxis().set_visible(False)



#xtick = np.arange(0,np.size(snmap_128) )
#print xtick
#
#f, (ax,ax2,ax3,ax4,ax5,ax6) = plt.subplots(1, 6, sharey=True, )
#f.subplots_adjust(hspace=0.2, wspace=0.05)
##y1_lim = 16 
#y1_lim = 12 
##ax.bar(xtick-0.3,v1, 0.3, label='Socket mmap', **next(styles))
##ax.bar(xtick-0.3,v1, 0.28, color="#73215C", edgecolor="black", linewidth=1 )
##ax.bar(xtick,v3, 0.28,color="#29B7B4", edgecolor="black")
##ax.bar(xtick+0.3,v2,0.28, color="#C8FE2E", edgecolor="black")
#ax.bar(xtick-0.34, snmap_64  ,0.34,   color="#E0E0E0", edgecolor="black")
#ax.bar(xtick,netmap_64   , 0.34,       color="white", edgecolor="black", **next(styles))
#ax.bar(xtick+0.34, dpdk_64 , 0.34,     color="#606060",edgecolor="black", **next(styles))
#ax.set_ylabel('Gbps')
#ax.set_ylim([0, y1_lim])
#ax.yaxis.tick_left() # doesnt work :(
#ax.axes.get_xaxis().set_visible(False)
#
#line = ax.twinx()
#line.set_ylim([0, 16])
#line.plot(xtick-0.35, pps_smmap_64,  color="black", marker=markers[2])
#line.plot(xtick    , pps_netmap_64,  color="black", marker=markers[1] , markersize=8, linestyle=linestyles[0])
#line.plot(xtick+0.35, pps_dpdk_64,   color="black", marker=markers[0],  markersize=8, linestyle=linestyles[3])
#line.axes.get_yaxis().set_visible(False)
#
#ax2.set_ylim([0, y1_lim])
#ax2.bar(xtick-0.35,snmap_128  , 0.35, color="#E0E0E0", edgecolor="black")
#ax2.bar(xtick    ,netmap_128 , 0.35,  color="white" , edgecolor="black", **next(styles))
#ax2.bar(xtick+0.35,dpdk_128   , 0.35, color="#606060",   edgecolor="black", **next(styles))
#ax2.axes.get_yaxis().set_visible(False)
#ax2.axes.get_xaxis().set_visible(False)
#
#line2 = ax2.twinx()
#line2.set_ylim([0, 16])
#line2.plot(xtick-0.35,pps_smmap_128,  color="black", marker=markers[2])
#line2.plot(xtick    ,pps_netmap_128, color="black", marker=markers[1] , markersize=8)
#line2.plot(xtick+0.35,pps_dpdk_128,   color="black", marker=markers[0], markersize=8, linestyle=linestyles[3])
#line2.axes.get_yaxis().set_visible(False)
#
#ax3.set_ylim([0, y1_lim])
#ax3.bar(xtick-0.35,snmap_256  , 0.35,  color="#E0E0E0", edgecolor="black")
#ax3.bar(xtick    ,netmap_256 , 0.35,   color="white" , edgecolor="black", **next(styles))
#ax3.bar(xtick+0.35,dpdk_256   , 0.35,  color="#606060",   edgecolor="black", **next(styles))
#ax3.axes.get_yaxis().set_visible(False)
#ax3.axes.get_xaxis().set_visible(False)
#
#line3 = ax3.twinx()
#line3.set_ylim([0, 16])
#line3.plot(xtick-0.35,pps_smmap_256, color="black", marker=markers[2])
#line3.plot(xtick    ,pps_netmap_256,color="black", marker=markers[1], markersize=8)
#line3.plot(xtick+0.35,pps_dpdk_256,  color="black", marker=markers[0] , markersize=8, linestyle=linestyles[3])
#line3.axes.get_yaxis().set_visible(False)
#
## ipv6
#
#ax4.set_ylim([0, y1_lim])
#ax4.bar(xtick-0.35,v6_smmap_64  , 0.35, color="#E0E0E0", edgecolor="black")                
#ax4.bar(xtick    ,v6_netmap_64 , 0.35,  color="white" , edgecolor="black", **next(styles))
#ax4.bar(xtick+0.35,v6_dpdk_64   , 0.35, color="#606060",   edgecolor="black", **next(styles))                
#ax4.axes.get_yaxis().set_visible(False)
#ax4.axes.get_xaxis().set_visible(False)
#
#line4 = ax4.twinx()
#line4.set_ylim([0, 16])
#line4.plot(xtick-0.35, v6_pps_smmap_64,  color="black", marker=markers[2])
#line4.plot(xtick    , v6_pps_netmap_64, color="black", marker=markers[1], markersize=8)
#line4.plot(xtick+0.35, v6_pps_dpdk_64,   color="black", marker=markers[0] , markersize=8, linestyle=linestyles[3])
#line4.axes.get_yaxis().set_visible(False)
#
#
#
#
#ax5.set_ylim([0, y1_lim])
#ax5.bar(xtick-0.35,v6_smmap_128  , 0.35,  color="#E0E0E0", edgecolor="black")                
#ax5.bar(xtick    ,v6_netmap_128 , 0.35,   color="white" , edgecolor="black", **next(styles))
#ax5.bar(xtick+0.35,v6_dpdk_128   , 0.35,  color="#606060",   edgecolor="black", **next(styles))                
#ax5.axes.get_yaxis().set_visible(False)
#ax5.axes.get_xaxis().set_visible(False)
#line5 = ax5.twinx()
#line5.set_ylim([0, 16])
#line5.plot(xtick-0.35, v6_pps_smmap_128,  color="black", marker=markers[2])
#line5.plot(xtick    , v6_pps_netmap_128, color="black", marker=markers[1], markersize=8)
#line5.plot(xtick+0.35, v6_pps_dpdk_128,   color="black", marker=markers[0] , markersize=8, linestyle=linestyles[3])
#line5.axes.get_yaxis().set_visible(False)
#
#
#
#ax6.set_ylim([0, y1_lim])
#ax6.bar(xtick-0.35,v6_smmap_256  , 0.35, color="#E0E0E0", edgecolor="black")                
#ax6.bar(xtick    ,v6_netmap_256 , 0.35,  color="white" , edgecolor="black", **next(styles))
#ax6.bar(xtick+0.35,v6_dpdk_256   , 0.35, color="#606060",   edgecolor="black", **next(styles))                
#ax6.axes.get_yaxis().set_visible(False)
#ax6.axes.get_xaxis().set_visible(False)
#line6 = ax6.twinx()
#line6.set_ylim([0, 16])
#line6.plot(xtick-0.35, v6_pps_smmap_256,  color="black", marker=markers[2])
#line6.plot(xtick    , v6_pps_netmap_256, color="black", marker=markers[1], markersize=8)
#line6.plot(xtick+0.35, v6_pps_dpdk_256,   color="black", marker=markers[0] , markersize=8, linestyle=linestyles[3])
#line6.tick_params(labelsize=11)
#line6.set_ylabel('Mpps')
#
#
##plt.xticks(xtick,xlabel )
##plt.title("Packet size (between CPE and BNG")
#
##ax.set_xlabel  ("100     1k     10k   100k   1M",fontsize=5 )
##ax2.set_xlabel ("100     1k     10k   100k   1M",fontsize=5 )
##ax3.set_xlabel ("100     1k     10k   100k   1M",fontsize=5 )
##ax4.set_xlabel ("100     1k     10k   100k   1M",fontsize=5 )
##ax5.set_xlabel ("100     1k     10k   100k   1M",fontsize=5 )
##ax6.set_xlabel ("100     1k     10k   100k   1M",fontsize=5 )
##ax.set_ylabel ("                  2               4               6               8               10")
#
#ticklabelpad = mpl.rcParams['xtick.major.pad']
##ypos= 19 # label for limit y1 12 
#xpos= 37 # label for limit y1 12
#
# 
#ypos= 33 # label for limit y1 12  XXXXXXX 
##xpos= 30 # label for limit y1 12
#
#ax.annotate('2', xy=(0, 1),  xytext=(-ypos+1,17), ha='center', va='center',  textcoords='offset points',        fontsize=11)
#ax.annotate('4', xy=(0, 1),  xytext=(-ypos+1,17+xpos), ha='center', va='center',  textcoords='offset points',   fontsize=11)
#ax.annotate('6', xy=(0, 1),  xytext=(-ypos+1,17+2*xpos), ha='center', va='center',  textcoords='offset points', fontsize=11)
#ax.annotate('8', xy=(0, 1),  xytext=(-ypos+1,17+3*xpos), ha='center', va='center',  textcoords='offset points', fontsize=11)
#ax.annotate('10', xy=(0, 1), xytext=(-ypos-2,17+4*xpos), ha='center', va='center',  textcoords='offset points', fontsize=11)
#ax.annotate('12', xy=(0, 1), xytext=(-ypos-2,17+5*xpos), ha='center', va='center',  textcoords='offset points', fontsize=11)
##ax.annotate('14', xy=(0, 1), xytext=(-ypos-2,13+6*xpos), ha='center', va='center',  textcoords='offset points', fontsize=11)
##ax.annotate('16', xy=(0, 1), xytext=(-ypos-2,13+7*xpos), ha='center', va='center',  textcoords='offset points', fontsize=11)
#
#
#
#
#
#xposi=165
#yposi=0
#
#line.annotate("100     1k     10k   100k   1M", xy=(1,0), xytext=(-xposi, -ticklabelpad-yposi), ha='left', va='top',   fontsize=11, xycoords='axes fraction', textcoords='offset points')
#line2.annotate("100     1k     10k   100k   1M", xy=(1,0), xytext=(-xposi, -ticklabelpad-yposi), ha='left', va='top',  fontsize=11, xycoords='axes fraction', textcoords='offset points')
#line3.annotate("100     1k     10k   100k   1M", xy=(1,0), xytext=(-xposi, -ticklabelpad-yposi), ha='left', va='top',  fontsize=11, xycoords='axes fraction', textcoords='offset points')
#line4.annotate("100     1k     10k   100k   1M", xy=(1,0), xytext=(-xposi, -ticklabelpad-yposi), ha='left', va='top',  fontsize=11, xycoords='axes fraction', textcoords='offset points')
#line5.annotate("100     1k     10k   100k   1M", xy=(1,0), xytext=(-xposi, -ticklabelpad-yposi), ha='left', va='top',  fontsize=11, xycoords='axes fraction', textcoords='offset points')
#line6.annotate("100     1k     10k   100k   1M", xy=(1,0), xytext=(-xposi, -ticklabelpad-yposi), ha='left', va='top',  fontsize=11, xycoords='axes fraction', textcoords='offset points')
#
#
#
#yposi= 15 
#xposi=90
#
#ax.annotate('64B', xy=(1,0),  xytext=(-xposi,  -ticklabelpad-yposi), ha='left', va='top', fontsize=13, xycoords='axes fraction', textcoords='offset points')
#ax2.annotate('128B', xy=(1,0),xytext=(-xposi, -ticklabelpad-yposi), ha='left', va='top',  fontsize=13, xycoords='axes fraction', textcoords='offset points')
#ax3.annotate('256B', xy=(1,0),xytext=(-xposi, -ticklabelpad-yposi), ha='left', va='top',  fontsize=13, xycoords='axes fraction', textcoords='offset points')
#ax4.annotate('64B', xy=(1,0), xytext=(-xposi,  -ticklabelpad-yposi), ha='left', va='top', fontsize=13, xycoords='axes fraction', textcoords='offset points')
#ax5.annotate('128B', xy=(1,0),xytext=(-xposi, -ticklabelpad-yposi), ha='left', va='top',  fontsize=13, xycoords='axes fraction', textcoords='offset points')
#ax6.annotate('256B', xy=(1,0),xytext=(-xposi, -ticklabelpad-yposi), ha='left', va='top',  fontsize=13, xycoords='axes fraction', textcoords='offset points')
#
#
#ax4.annotate('Packet Size', xy=(1,0), xytext=(-yposi-54, -ticklabelpad-xposi-5), ha='left', va='top', fontsize=8, xycoords='axes fraction', textcoords='offset points')
#
##ax.set_yticklabels(['0','1','2','3','4','5','6','7','8','9','10'])
##ax2.set_yticklabels([])
#ax3.set_yticklabels([])
#ax4.set_yticklabels([])
#ax5.set_yticklabels([])
#
#
#ax6.set_xticklabels([])
#ax5.set_xticklabels([])
#ax4.set_xticklabels([])
#ax3.set_xticklabels([])
#ax2.set_xticklabels([])
#ax.set_xticklabels([])
#
#line.set_yticklabels([])
#line2.set_yticklabels([])
#line3.set_yticklabels([])
#line4.set_yticklabels([])
#line5.set_yticklabels([])
##line3.set_yticklabels([])
#
##plt.title("Performance comparison for diferents NIC drivers")
#ax2.legend(["Socket-mmap", "Netmap","DPDK" ], edgecolor = "white", loc=9, fontsize=10, bbox_to_anchor=(0.6,1.1) )
#line6.legend(["Socket-mmap", "Netmap","DPDK" ], edgecolor = "white", loc=9, fontsize=10, bbox_to_anchor=(0.6,1.1) )
#
##ax.set_prop_cycle(monochrome)
##ax.spines['top'].set_visible(False)
#ax6.spines['right'].set_visible(True)
#ax.spines['left'].set_visible(True)
#ax.spines['bottom'].set_visible(True)
#ax.spines['left'].set_visible(True)

#plt.grid()
#plt.show()
#plt.savefig('sine.eps', format='eps', dpi=600)
plt.savefig('sine.png', format='png', dpi=600)

#plt.savefig('figure.png', format='png', dpi=800)
