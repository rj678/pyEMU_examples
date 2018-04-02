import os
import shutil
import pandas as pd
import numpy as np
import pyemu
import flopy

working_dir = '.'

m = flopy.modflow.Modflow.load('mrgb.nam',model_ws=working_dir,load_only=[])

#os.chdir('all_layers')
for lay in range(m.nlay):
    pp_file = 'hk'+str(lay)+'pp.dat'
    factors_file = 'hk'+str(lay)+'pp.dat.fac'
    out_file = 'arrays/hk_Layer_'+str(lay)+'.ref'
    fill_value = 1e+1
    pyemu.utils.geostats.fac2real(pp_file=pp_file,factors_file=factors_file,
                            out_file=out_file,fill_value=fill_value)

#os.chdir('..')

exe_name = 'mf2005dbl'
nam_file = 'mrgb.nam'

#pyemu.helpers.run('mf2005 parent.nam >_mf2005.stdout')
pyemu.helpers.run('{0} {1}'.format(exe_name,nam_file))
#pyemu.helpers.run('Users/rishijumani/Modflow/temp/mf2005 parent.nam >_mf2005.stdout')
#pyemu.helpers.run('mp6 freyberg.mpsim >_mp6.stdout')
#pyemu.gw_utils.apply_mflist_budget_obs('freyberg.list')
#hds = flopy.utils.HeadFile('freyberg.hds')
#f = open('freyberg.hds.dat','wb')
#for data in hds.get_alldata():
#    data = data.flatten()
#    np.savetxt(f,data,fmt='%15.6E')
#endpoint_file = 'freyberg.mpenpt'
#lines = open(endpoint_file, 'r').readlines()
#items = lines[-1].strip().split()
#travel_time = float(items[4]) - float(items[3])
#with open('freyberg.travel', 'w') as ofp:
#    ofp.write('travetime {0:15.6e}{1}'.format(travel_time, '\n'))
#pyemu.gw_utils.modflow_read_hydmod_file('freyberg.hyd.bin')
