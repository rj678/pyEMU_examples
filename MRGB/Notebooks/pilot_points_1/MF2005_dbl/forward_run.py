import os
import shutil
import pandas as pd
import numpy as np
import pyemu
import flopy
import platform

version = 'mf2005'
working_dir = '.'

if platform.system() == 'Windows':
    exe_name = r'D:\Work\exec_Win\MF2005.1_12\bin\mf2005dbl'
    exe_name += '.exe'
else:
    exe_name = '/Volumes/A_2TB/Work/exec_Mac/mf2005dbl'

#m = flopy.modflow.Modflow.load('name.nam',model_ws=working_dir,load_only=[])
m = flopy.modflow.Modflow.load('name.nam',model_ws=working_dir,exe_name=exe_name,
                                    version=version,check=False)

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
nam_file = 'name.nam'

#pyemu.helpers.run('mf2005 parent.nam >_mf2005.stdout')
pyemu.helpers.run('{0} {1}'.format(exe_name,nam_file))