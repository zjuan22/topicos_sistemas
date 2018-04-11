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
plt.rcParams['axes.spines.bottom'] = True
plt.rcParams['axes.spines.left'] = False
plt.rcParams['figure.figsize'] = 10,5

#plt.axes().get_yaxis().set_visible(True)

bar_cycle = (cycler('hatch', ['++++++', 'xxxxxx', '------', 'xxx', '\\\\']) *cycler('zorder', [14]))

styles = bar_cycle()

snmap_64 =  [ 0.1349, 0.1925, 0.0376, 0.0271, 0.0004 ]   
dpdk_64 =   [ 9.9043 ,9.9044, 9.9044, 9.9075, 9.9742 ] 
netmap_64 = [ 5.5006 ,7.1007, 9.9044, 5.4042, 5.358 ] 

snmap_128 = [ 0.1692, 0.3466, 0.3316, 0.0007, 0.0426 ] 
dpdk_128 =  [ 9.9964, 9.9957, 9.9957, 9.9957, 9.9934] 
netmap_128 =[ 8.6587, 9.9955, 9.9957, 8.8772, 8.3508] 

snmap_256 = [ 0.4326, 0.6183, 0.7095, 0.6235, 0.8818 ] 
dpdk_256 =  [ 9.9039, 9.9042, 9.9042, 9.9042, 9.9042] 
netmap_256 =[ 9.904 , 9.9038, 9.9042, 9.9066, 9.9061 ] 

pps_smmap_64 =   [  0.1983777, 0.2844025,  0.0829268, 0.0373987,  0.0006123 ]  
pps_smmap_128 =  [  0.1397185, 0.2181505,  0.1179953, 0.2289735,  0.0336097 ]  
pps_smmap_256 =  [  0.1505477, 0.2772149,  0.1054852, 0.2785108,  0.3126653 ]  

pps_dpdk_64 =    [ 14.8883949,14.8879949, 14.887872, 14.8920443, 14.7844936 ]
pps_dpdk_128 =   [  8.4421463, 8.4417797,  8.4417797, 8.4417797,  8.4408202 ]
pps_dpdk_256 =   [  4.5311221, 4.5309885,  4.5309885, 4.5309885,  4.5309885 ]   

pps_netmap_64 =  [  8.1812423, 9.7615546,  9.6330745, 7.9977912,  7.9628553 ] 
pps_netmap_128 = [  7.302157 , 8.4417622,  8.0220733, 7.4567338,  7.0401164 ] 
pps_netmap_256 = [  4.1330245, 4.5308948,  4.5308948, 4.5318384,  4.531815 ] 


v6_smmap_64 =   [ 0.13,   0.0616, 0.0895,  0.0774, 0.1507 ]
v6_smmap_128 =  [ 0.235,  0.459,  0.0006,  0.479,  0.0989 ]
v6_smmap_256 =  [ 0.437,  0.7027, 0.7279,  0.8658, 0.9242 ] 
                                                     
v6_dpdk_64 =    [ 9.9053 ,9.9047, 9.9972, 10.0085, 9.957 ]
v6_dpdk_128 =   [ 9.9957 ,9.9957, 9.9957,  9.9957, 9.9957 ]
v6_dpdk_256 =   [ 9.9042 ,9.9042, 9.9042,  9.9042, 9.9042 ]
                                                     
v6_netmap_64 =  [ 6.9165 ,6.0503, 9.9972,  4.872,  4.935 ]
v6_netmap_128 = [ 9.9955 ,9.824,  9.9957,  7.7755, 6.4519 ]
v6_netmap_256 = [ 9.9584 ,9.9054, 9.9042,  9.9059, 7.6802 ]

v6_pps_smmap_64 =   [  0.1840123,  0.1677052,  0.1449258, 0.1951453, 0.1803625 ]
v6_pps_smmap_128 =  [  0.1926118,  0.3352464,  0.3139102, 0.348658,  0.3430172 ]
v6_pps_smmap_256 =  [  0.1799195,  0.315867,   0.2351163, 0.316668,  0.2672616 ]
                                                                       
v6_pps_dpdk_64 =    [ 14.8893573, 14.8878317, 14.8874925, 4.0092874, 0.3764334 ]
v6_pps_dpdk_128 =   [  8.4417797,  8.4417797,  8.4417797, 8.4417797, 8.4417797 ]
v6_pps_dpdk_256 =   [  4.5309885,  4.5309885,  4.5309885, 4.5309885, 4.5309885 ]
                                                                       
v6_pps_netmap_64 =  [ 10.0573071,  8.8877591,  8.5307575, 7.1329885, 6.4717325 ]
v6_pps_netmap_128 = [  8.4416536,  8.1401565,  7.0519913, 2.8252815, 5.4320285 ]
v6_pps_netmap_256 = [  4.2394418,  4.5315902,  4.5311035, 4.5317728, 3.4778146 ]    
    
  
  

  
  
  

 
 
 






 
 
 





xtick = np.arange(0,np.size(snmap_128) )

#xlabel = ['82', '128', '256', '512', '1024', '1280', '1518']
#xlabel = ['100', '1k', '10k', '100K', '1M']
ytick = np.arange(0,10,10)

#f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex=')
#f, ((ax, line), (ax2, line2), (ax3, line3)) = plt.subplots(2, 3, sharey'True')  //no funciona

f, (ax,ax2,ax3) = plt.subplots(1, 3, sharey=True)



#ax.bar(xtick-0.3,v1, 0.28, color="#73215C", edgecolor="black", linewidth=1 )
#ax.bar(xtick,v3, 0.28,color="#29B7B4", edgecolor="black")
#ax.bar(xtick+0.3,v2,0.28, color="#C8FE2E", edgecolor="black")
ax.bar(xtick-0.3,snmap_64  , 0.3,   color="#C8FE2E")
ax.bar(xtick    ,netmap_64 , 0.3,   color="#29B7B4")
ax.bar(xtick+0.3,dpdk_64   , 0.3,   color="#73215C")
ax.set_ylabel('Gbps')
ax.set_ylim([0, 10])
line = ax.twinx()
line.set_ylim([0, 16])
line.plot(xtick-0.3, pps_smmap_64,  color="black")
line.plot(xtick    , pps_netmap_64, color="black")
line.plot(xtick+0.3, pps_dpdk_64,   color="black")


ax2.set_ylim([0, 10])
ax2.bar(xtick-0.3,snmap_128  , 0.3, color="#C8FE2E")
ax2.bar(xtick    ,netmap_128 , 0.3, color="#29B7B4" )
ax2.bar(xtick+0.3,dpdk_128   , 0.3, color="#73215C")

line2 = ax2.twinx()
line2.set_ylim([0, 16])
line2.plot(xtick-0.3,pps_smmap_128,  color="black")
line2.plot(xtick    ,pps_netmap_128, color="black")
line2.plot(xtick+0.3,pps_dpdk_128,   color="black")

ax3.set_ylim([0, 10])
ax3.bar(xtick-0.3,snmap_256  , 0.3,   color="#C8FE2E")
ax3.bar(xtick    ,netmap_256 , 0.3,  color="#29B7B4" )
ax3.bar(xtick+0.3,dpdk_256   , 0.3,    color="#73215C")

line3 = ax3.twinx()
line3.set_ylim([0, 16])
line3.plot(xtick-0.3,pps_smmap_256, color="black")
line3.plot(xtick    ,pps_netmap_256,color="black")
line3.plot(xtick+0.3,pps_dpdk_256,  color="black")
line3.set_ylabel('Mpps')

#plt.xticks(xtick,xlabel )
#plt.title("Packet size (between CPE and BNG")

ax.set_xlabel ("100     1k     10k   100k   1M")
#ax.set_ylabel ("                  2               4               6               8               10")
ax2.set_xlabel("100     1k     10k   100k   1M")
ax3.set_xlabel("100     1k     10k   100k   1M")

ticklabelpad = mpl.rcParams['xtick.major.pad']

ax.annotate('2', xy=(0, 1), xytext=(-30,28), ha='center', va='center',  textcoords='offset points', fontsize=10)
ax.annotate('4', xy=(0, 1), xytext=(-30,84), ha='center', va='center',  textcoords='offset points', fontsize=10)
ax.annotate('6', xy=(0, 1), xytext=(-30,138), ha='center', va='center',  textcoords='offset points', fontsize=10)
ax.annotate('8', xy=(0, 1), xytext=(-30,198), ha='center', va='center',  textcoords='offset points', fontsize=10)
ax.annotate('10', xy=(0, 1), xytext=(-33,248), ha='center', va='center',  textcoords='offset points', fontsize=10)

ax.annotate('64B', xy=(1,0), xytext=(-100, -ticklabelpad-20), ha='left', va='top',
            xycoords='axes fraction', textcoords='offset points')

ax2.annotate('128B', xy=(1,0), xytext=(-100, -ticklabelpad-20), ha='left', va='top',
            xycoords='axes fraction', textcoords='offset points')

ax3.annotate('256B', xy=(1,0), xytext=(-100, -ticklabelpad-20), ha='left', va='top',
            xycoords='axes fraction', textcoords='offset points')

#ax.set_yticklabels(['0','1','2','3','4','5','6','7','8','9','10'])
#ax2.set_yticklabels([])
ax3.set_yticklabels([])

ax3.set_xticklabels([])
ax2.set_xticklabels([])
ax.set_xticklabels([])

line.set_yticklabels([])
line2.set_yticklabels([])
#line3.set_yticklabels([])

#plt.title("Performance comparison for diferents NIC drivers")
ax3.legend(["Socket-mmap", "Netmap", "DPDK" ], edgecolor = "white", loc=2 )
line3.legend(["Socket-mmap", "Netmap","DPDK" ], edgecolor = "white", loc=6 )

#ax.set_prop_cycle(monochrome)
#ax.spines['top'].set_visible(False)
ax3.spines['right'].set_visible(True)
ax.spines['left'].set_visible(True)
#ax.spines['bottom'].set_visible(True)
#ax.spines['left'].set_visible(True)

#plt.grid()
#plt.show()
plt.savefig('figure.png', format='png', dpi=500)
