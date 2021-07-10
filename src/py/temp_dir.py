# @Time    : 2021/03/15
# @Author  : Naunter
# @Page    : https://github.com/Naunters
# @Page    : https://github.com/BDO-CnHope/bdocn_client

from tempfile import mkdtemp
from time_template import time_template

def temp_loc_dir():
    time_template()
    print("temp_dir.py >>> temp_loc_dir()")
    dir = mkdtemp(prefix='loc_temp_')
    print("temp_dir.py >>> temp_loc_dir() >>> dir: "+str(dir))
    return dir

def temp_font_dir():
    time_template()
    print("temp_dir.py >>> temp_font_dir()")
    dir = mkdtemp(prefix='font_temp_')
    print("temp_dir.py >>> temp_font_dir() >>> dir: "+str(dir))
    return dir