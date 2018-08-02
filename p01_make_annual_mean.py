import numpy as np
import os

years = np.arange(501,525)

v = 'SST'

output = 'ice_month'

for y in years:
    os.system('ncra -v ' + v + ' /short/e14/erd561/mom/archive/gfdl_nyf_1080_hist_5069/output' + str(y) + '/' + output + '.nc /g/data/e14/erd561/mom/gfdl_nyf_1080_hist_5069/' + output + str(y) + '_' + v + '.nc')
    print(str(y) + ' OK')


