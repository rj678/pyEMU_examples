import os
import shutil
import pandas as pd
import numpy as np
import pyemu
import flopy

exe_name = 'mf2005dbl.exe'
nam_file = 'name.nam'

pyemu.helpers.run('{0} {1}'.format(exe_name,nam_file))