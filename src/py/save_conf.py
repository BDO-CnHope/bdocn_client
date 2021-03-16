# @Time    : 2021/03/15
# @Author  : Naunter
# @Page    : https://github.com/Naunters
# @Page    : https://github.com/BDO-CnHope/bdocn_client

from pathlib import Path
from datetime import datetime

time_stamp = datetime.now()

user_home = str(Path.home())
bdocn_conf_dir = (user_home + r'/AppData/Roaming/bdocn_client')
bdo_gamepath = (bdocn_conf_dir + r'/bdocn_gamepath.txt')
bdo_confpath = (bdocn_conf_dir + r'/bdocn_confpath.txt')

def save_bdocn_conf_dir():
    print("save_bdocn_conf_dir: user_home: " + user_home)
    print("bdocn_conf_dir: is_dir(): " + str(Path(bdocn_conf_dir).is_dir()))
    if Path(bdocn_conf_dir).is_dir is True:
        return(str(bdocn_conf_dir))
    else:
        Path(bdocn_conf_dir).mkdir(parents=True, exist_ok=True)
        return(str(bdocn_conf_dir))

def save_bdo_gamepath(path):
    f = open(bdo_gamepath,"w+")
    t = str(path)
    f.write(t)
    f.close()

def save_bdo_confpath(path):
    f = open(bdo_confpath,"w+")
    t = str(path)
    f.write(t)
    f.close()
