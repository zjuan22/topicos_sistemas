
import sys,os
path = os.path.abspath('../dev/')
if path not in sys.path:
    sys.path.append(path)

import numpy as np
import scipy as scipy
import scipy.misc as misc 
import matplotlib.pyplot as plt
import matplotlib as mpl

from cycler import cycler

import IPython
import matplotlib
import copy
import random






markers = ["*","^","."]
linestyles = ['-', '--', '-.', ':']

#plt.rcParams['axes.grid'] = True
#plt.rcParams['axes.prop_cycle'] = monochrome
plt.rcParams['axes.spines.top'] = False
plt.rcParams['axes.spines.right'] = True 
plt.rcParams['axes.spines.bottom'] = True
plt.rcParams['axes.spines.left'] = True 
plt.rcParams['figure.figsize'] = 20, 4

plt.rcParams['axes.axisbelow'] = True


#plt.axes().get_yaxis().set_visible(True)

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

total_smmap = [snmap_64[0], snmap_64[1], snmap_64[2],snmap_64[3], snmap_64[4],np.nan,snmap_128[0], snmap_128[1], snmap_128[2], snmap_128[3], snmap_128[4],np.nan,snmap_256[0], snmap_256[1], snmap_256[2], snmap_256[3], snmap_256[4],np.nan,np.nan, v6_smmap_64[0], v6_smmap_64[1], v6_smmap_64[2], v6_smmap_64[3], v6_smmap_64[4],np.nan,v6_smmap_128[0], v6_smmap_128[1], v6_smmap_128[2], v6_smmap_128[3], v6_smmap_128[4],np.nan,v6_smmap_256[0], v6_smmap_256[1], v6_smmap_256[2], v6_smmap_256[3], v6_smmap_256[4]] 


total_netmap = [netmap_64[0], netmap_64[1], netmap_64[2],netmap_64[3], netmap_64[4],np.nan,netmap_128[0], netmap_128[1], netmap_128[2], netmap_128[3], netmap_128[4],np.nan,netmap_256[0], netmap_256[1], netmap_256[2], netmap_256[3], netmap_256[4],np.nan,np.nan,v6_netmap_64[0], v6_netmap_64[1], v6_netmap_64[2], v6_netmap_64[3], v6_netmap_64[4],np.nan,v6_netmap_128[0], v6_netmap_128[1], v6_netmap_128[2], v6_netmap_128[3], v6_netmap_128[4],np.nan,v6_netmap_256[0], v6_netmap_256[1], v6_netmap_256[2], v6_netmap_256[3], v6_netmap_256[4]] 

total_dpdk = [dpdk_64[0], dpdk_64[1], dpdk_64[2],dpdk_64[3], dpdk_64[4],np.nan,dpdk_128[0], dpdk_128[1], dpdk_128[2], dpdk_128[3], dpdk_128[4],np.nan,dpdk_256[0], dpdk_256[1], dpdk_256[2], dpdk_256[3], dpdk_256[4],np.nan,np.nan, v6_dpdk_64[0], v6_dpdk_64[1], v6_dpdk_64[2], v6_dpdk_64[3], v6_dpdk_64[4],np.nan,v6_dpdk_128[0], v6_dpdk_128[1], v6_dpdk_128[2], v6_dpdk_128[3], v6_dpdk_128[4],np.nan,v6_dpdk_256[0], v6_dpdk_256[1], v6_dpdk_256[2], v6_dpdk_256[3], v6_dpdk_256[4]]


pps_total_smmap = [pps_smmap_64[0], pps_smmap_64[1], pps_smmap_64[2],pps_smmap_64[3], pps_smmap_64[4],np.nan,pps_smmap_128[0], pps_smmap_128[1], pps_smmap_128[2], pps_smmap_128[3], pps_smmap_128[4],np.nan,pps_smmap_256[0], pps_smmap_256[1], pps_smmap_256[2], pps_smmap_256[3], pps_smmap_256[4],np.nan,np.nan, v6_pps_smmap_64[0], v6_pps_smmap_64[1], v6_pps_smmap_64[2], v6_pps_smmap_64[3], v6_pps_smmap_64[4],np.nan,v6_pps_smmap_128[0], v6_pps_smmap_128[1], v6_pps_smmap_128[2], v6_pps_smmap_128[3], v6_pps_smmap_128[4],np.nan,v6_pps_smmap_256[0], v6_pps_smmap_256[1], v6_pps_smmap_256[2], v6_pps_smmap_256[3], v6_pps_smmap_256[4]] 


pps_total_netmap = [pps_netmap_64[0], pps_netmap_64[1], pps_netmap_64[2],pps_netmap_64[3], pps_netmap_64[4],np.nan,pps_netmap_128[0], pps_netmap_128[1], pps_netmap_128[2], pps_netmap_128[3], pps_netmap_128[4],np.nan,pps_netmap_256[0], pps_netmap_256[1], pps_netmap_256[2], pps_netmap_256[3], pps_netmap_256[4],np.nan,np.nan,v6_pps_netmap_64[0], v6_pps_netmap_64[1], v6_pps_netmap_64[2], v6_pps_netmap_64[3], v6_pps_netmap_64[4],np.nan,v6_pps_netmap_128[0], v6_pps_netmap_128[1], v6_pps_netmap_128[2], v6_pps_netmap_128[3], v6_pps_netmap_128[4],np.nan,v6_pps_netmap_256[0], v6_pps_netmap_256[1], v6_pps_netmap_256[2], v6_pps_netmap_256[3], v6_pps_netmap_256[4]] 


pps_total_dpdk = [pps_dpdk_64[0], pps_dpdk_64[1], pps_dpdk_64[2],pps_dpdk_64[3], pps_dpdk_64[4],np.nan,pps_dpdk_128[0], pps_dpdk_128[1], pps_dpdk_128[2], pps_dpdk_128[3], pps_dpdk_128[4],np.nan,pps_dpdk_256[0], pps_dpdk_256[1], pps_dpdk_256[2], pps_dpdk_256[3], pps_dpdk_256[4],np.nan,np.nan, v6_pps_dpdk_64[0], v6_pps_dpdk_64[1], v6_pps_dpdk_64[2], v6_pps_dpdk_64[3], v6_pps_dpdk_64[4],np.nan,v6_pps_dpdk_128[0], v6_pps_dpdk_128[1], v6_pps_dpdk_128[2], v6_pps_dpdk_128[3], v6_pps_dpdk_128[4],np.nan,v6_pps_dpdk_256[0], v6_pps_dpdk_256[1], v6_pps_dpdk_256[2], v6_pps_dpdk_256[3], v6_pps_dpdk_256[4]] 

 

entries = ["100","1k","10k","100k","1M","","100","1k","10k","100k","1M","","100","1k","10k","100k","1M","","","100","1k","10k","100k","1M","","100","1k","10k","100k","1M","","100","1k","10k","100k","1M"]

fig2 = plt.figure(figsize=(20,4.5))
fig = plt.figure()
#fig.suptitle('bold figure suptitle', fontsize=11,  fontweight='bold')
#fig.subplots_adjust(bottom=0.1)

xtick = np.arange(len(entries) )
#print  len(entries)
print( "smmap"+ str(len(pps_total_smmap)))
print( "netmap" +str(len(pps_total_netmap)))
print( "dpdk"+ str(len(pps_total_dpdk)))

fig = plt.figure(figsize=(20,4))
ax = fig.add_subplot(111)
y1_lim = 16 


#width = 0.5
#ax.bar([p +2+ width for p in xtick+1] , pps_total_smmap  ,width,   color="#E0E0E0", edgecolor="black")
#ax.bar([p +2+ width for p in xtick+0.5],      pps_total_netmap , width,       color="white", edgecolor="black", **next(styles))
#ax.bar([p +2+ width for p in xtick], pps_total_dpdk   , width,     color="#606060",edgecolor="black", **next(styles))

width = 0.3
#ax.bar(xtick-width , pps_total_smmap  ,width,   color="#E0E0E0", edgecolor="black")
#ax.bar(xtick,      pps_total_netmap , width,       color="white", edgecolor="black", **next(styles))
#ax.bar(xtick+width, pps_total_dpdk   , width,     color="#606060",edgecolor="black", **next(styles))

ax.bar(xtick-width , pps_total_smmap  ,width, color="#FCD0A1",edgecolor="black",hatch="..", lw=1., zorder = 0)  
ax.bar(xtick,      pps_total_netmap , width,  color="#B1B695", edgecolor="black", lw=1., zorder = 0 )  
ax.bar(xtick+width, pps_total_dpdk   , width, color="#AFD2E9", edgecolor="black",hatch="OO", lw=1., zorder = 0)  

ax.set_ylabel('Throughtput (Mpps)')
ax.set_ylim([0, y1_lim])
ax.set_xticks(xtick)
#ax.set_xticks(xtick+2*(width/2)+2)
#xticks = ax.xaxis.get_major_ticks()
xticks = ax.xaxis.get_major_ticks()

xticks[5].set_visible(False)
xticks[11].set_visible(False)
xticks[17].set_visible(False)
xticks[18].set_visible(False)
xticks[24].set_visible(False)
xticks[30].set_visible(False)

ax.set_xticklabels(entries)
#ax.yaxis.tick_left() # doesnt work :(
#ax.axes.get_xaxis().set_visible(False)
ax.axes.get_yaxis().set_visible(True)

line = ax.twinx()
#plt.grid()
ax.yaxis.grid(color='gray', linestyle='dashed')
line.set_ylim([0, 16])
line.plot(xtick-0.35, total_smmap  ,  color="black", marker=markers[2])
#line.plot(xtick-0.35, total_smmap  , color="#FCD0A1",edgecolor="black",hatch="..", lw=1., zorder = 0)
line.plot(xtick    ,  total_netmap ,  color="black", marker=markers[1] , markersize=8, linestyle=linestyles[0])
#line.plot(xtick    ,  total_netmap , color="#B1B695", edgecolor="black", lw=1., zorder = 0 )
line.plot(xtick+0.35, total_dpdk   ,   color="black", marker=markers[0],  markersize=8, linestyle=linestyles[3])
#line.plot(xtick+0.35, total_dpdk   , color="#AFD2E9", edgecolor="black",hatch="OO", lw=1., zorder = 0) 
line.set_ylabel('Throughput (Gbps)')
sep= 5.4
ypos = -2.3
ax.text(1.9, ypos, u'64B',fontsize=11)
ax.text(2.2+sep, ypos, u'128B',fontsize=11)
ax.text((2+1)+(sep)*2, ypos, u'256B',fontsize=11)
ax.text((3+1.5)+(sep)*3, ypos, u'64B',fontsize=11)
ax.text((3+2)+(sep)*4, ypos, u'128B',fontsize=11)
ax.text((3+2.5)+(sep)*5, ypos, u'256B',fontsize=11)


ax.text(1.9+sep, ypos-1.5, u'L3-IPv4',fontsize=14)
ax.text((2.7+2)+(sep)*4, ypos-1.5, u'L3-IPv6',fontsize=14)

ypos = -2.3
ax.text(16, ypos-1.5, u'Number of entries',fontsize=14)
ax.text(16, ypos-2.5, u'Packet size (bytes)',fontsize=14)
#ax.text(4.65, -1, u'',fontsize=10)
#ax.text(6.75, -1, u'(I)',fontsize=10)

leg = ax.legend(["Socket-mmap", "Netmap","DPDK" ], edgecolor = "white", loc=1, fontsize=10, bbox_to_anchor=(0.088,1.03), fancybox=True )
leg.get_frame().set_alpha(0)

leg2=line.legend(["Socket-mmap", "Netmap","DPDK" ], edgecolor = "white", loc=2, fontsize=10, bbox_to_anchor=(0.91,1.03), markerfirst=False )
leg2.get_frame().set_alpha(0)

#ax.spines['top'].set_visible(True)
line.spines['right'].set_visible(True)
ax.spines['left'].set_visible(True)
#ax.spines['bottom'].set_visible(True)
#ax.spines['left'].set_visible(True)
plt.tight_layout(pad=4, w_pad=0.5, h_pad=2.5)

#plt.show()
#plt.savefig('/home/lion/ipv4_ipv6.svg', format='svg', dpi=40)
plt.savefig('/home/lion/ipv4_ipv6.eps', format='eps', dpi=40)
#plt.savefig('/home/lion/ipv6ipv6.png', format='pgn', dpi=600)
#plt.savefig('sine.png', format='png', dpi=600)

