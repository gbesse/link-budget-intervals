import math
from .common import number,integer,identifier
def interval(x):
 if not isinstance(x,list)or len(x)!=2:raise ValueError('interval')
 a,b=[number(v,-1e18,1e18)for v in x]
 if a>b:raise ValueError('order')
 return a,b
def run(d):
 f=interval(d['frequency_hz']);r=interval(d['range_m']);rate=interval(d['bitrate']);
 if min(f+r+rate)<=0:raise ValueError('positive')
 fspl=[20*math.log10(4*math.pi*r[i]*f[i]/299792458)for i in [0,1]]
 terms={k:interval(d[k])for k in ['tx_dbw','tx_gain_dbi','rx_gain_dbi','loss_db','noise_density_dbw_hz','required_ebn0_db']}
 lo=terms['tx_dbw'][0]+terms['tx_gain_dbi'][0]+terms['rx_gain_dbi'][0]-terms['loss_db'][1]-fspl[1]-terms['noise_density_dbw_hz'][1]-10*math.log10(rate[1])-terms['required_ebn0_db'][1]
 hi=terms['tx_dbw'][1]+terms['tx_gain_dbi'][1]+terms['rx_gain_dbi'][1]-terms['loss_db'][0]-fspl[0]-terms['noise_density_dbw_hz'][0]-10*math.log10(rate[0])-terms['required_ebn0_db'][0]
 return dict(free_space_loss_db=fspl,margin_db=[lo,hi],verdict='positive'if lo>=0 else 'negative'if hi<0 else 'uncertain')
