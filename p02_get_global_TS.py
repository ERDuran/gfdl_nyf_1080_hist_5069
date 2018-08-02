import numpy as np
import os

years = np.arange(501,525)

v = 'SST'

output = 'ice_month'

os.system('ncrcat /g/data/e14/erd561/mom/gfdl_nyf_1080_hist_5069/' + output + '*' + '_' + v + '.nc /g/data/e14/erd561/mom/gfdl_nyf_1080_hist_5069/' + output + '501to524' + '_' + v + '.nc')

os.system('ncwa -a xt,yt ' + '/g/data/e14/erd561/mom/gfdl_nyf_1080_hist_5069/' + output + '501to524' + '_' + v + '.nc /g/data/e14/erd561/mom/gfdl_nyf_1080_hist_5069/' + output + '501to524' + '_' + v + 'ncwa_xtyt.nc')
