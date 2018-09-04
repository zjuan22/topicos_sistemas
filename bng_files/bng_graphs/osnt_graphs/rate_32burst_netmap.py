#import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from cycler import cycler

plt.rcParams['axes.spines.right'] = True 
plt.rcParams['axes.spines.bottom'] = True
plt.rcParams['axes.spines.left'] = True 
plt.rcParams['axes.axisbelow'] = True
plt.rcParams['axes.axisbelow'] = True
plt.rcParams['figure.figsize'] = 7.6, 3.5 


markers = ["*","^","."]

x_values= ["128","256","512","1024","1280","1518"]

osnt_l2=[1.481,2.836,5.244,8.767,9.846,9.865]
nfpa_l2=[1.604,2.911,5.179,8.953,9.988,9.989]
osnt_l3=[1.453,2.835,5.231,8.756,9.846,9.86]
nfpa_l3=[1.572,2.784,4.802,8.596,9.699,9.81]
osnt_nu=[1.215,2.495,4.938,8.74,9.843,9.861]
nfpa_nu=[1.556,2.792,5.062,8.815,9.774,9.998]
osnt_nd=[1.23,2.45,4.938,8.738,9.846,9.86]
nfpa_nd=[1.436,2.668,4.987,8.757,9.854,10]
osnt_al=[8.649,9.775,9.82,9.828,9.828,9.868]
nfpa_al=[10,10,10,10,10,10]


#l2 =      [np.nan,]
#l3 =      [
#nat_ul=   [857,np.nan]
#nat_dl=   [875,np.nan]

ind = np.arange(len(x_values))

width = 0.3
fig = plt.figure()
ax = fig.add_subplot(111)
#ax.set_ylim([0, 10])

linestyles = ['-', '--', '-.', ':']
dashList = [(4,2,20,2),(2,3),(5,1),(4,3,2,2),(8,4,3,1)] 
verde_oscuro="#006633"
azul_cielo="#2248E1"

fucsia="#DA22E1"
cafe="#A91524"

azul_mar="#161673"
azul_claro="#1AE2E2"

tomate="#E88411"
verde_fosfo="#B2E835"

ax.yaxis.grid(color='gray' )
ax.plot(ind, osnt_l2,  color=azul_cielo,   linestyle="-.", dashes=dashList[0], lw=2, )
ax.plot(ind, nfpa_l2,  color=verde_oscuro, linestyle="-.", dashes=dashList[0], lw=2)

ax.plot(ind, osnt_l3,  color="red",   dashes=dashList[1], lw=2)
ax.plot(ind, nfpa_l3,  color="green", dashes=dashList[1], lw=2)

ax.plot(ind, osnt_nu,  color=cafe,   dashes=dashList[2], lw=2)
ax.plot(ind, nfpa_nu,  color=fucsia, dashes=dashList[2], lw=2)

ax.plot(ind, osnt_nd,  color=azul_mar,   dashes=dashList[3], lw=2)
ax.plot(ind, nfpa_nd,  color=azul_claro, dashes=dashList[3], lw=2)

ax.plot(ind, osnt_al,  color="black",   dashes=dashList[4], lw=2)
ax.plot(ind, nfpa_al,  color=tomate,    dashes=dashList[4], lw=2)

#ax.set_xticks(ind+6*(width/2))
#xticks = ax.xaxis.get_major_ticks()

font_size= 14
ax.set_xticklabels(x_values, fontsize=font_size)

ax.set_ylabel('Throughput (Gbps)',fontsize=font_size)
#ax.yaxis.set_label_coords(-0.08,0.9)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.yaxis.set_ticks_position('left')
#ax.tick_params(axis='y',length=6)
ax.xaxis.set_ticks_position('bottom')
ax.set_xlabel("Packet size (Bytes)", fontsize=font_size)
ax.xaxis.set_label_coords(0.5,-0.2)
ax.yaxis.grid(linestyle='--')

#ax.text(5, -1.2, u'Socket-mmap',fontsize=font_size)
#ax.text(19, -1.2, u'Netmap',fontsize=font_size)
#ax.text(33, -1.2, u'DPDK',fontsize=font_size)
#ax.set_ylim([0,7.4])

leg= plt.legend(['OSNT-L2', 'NFPA-L2','OSNT-L3', 'NFPA-L3', 'OSNT-NAT-UL', 'NFPA-NAT_UL', 'OSNT-NAT-DL', 'NFPA-NAT_DL', 'OSNT-Standalone','NFPA-Standalone'], loc='center right',frameon=False, fontsize= 11)

leg.get_frame().set_linewidth(0.0)

plt.tight_layout(pad=0.3, w_pad=0.5, h_pad=1)

filename="rate_32burst_netmap"
#plt.savefig("vxlan.png")
plt.savefig(filename+".eps")
plt.savefig(filename+".svg")
plt.savefig(filename+".png")
