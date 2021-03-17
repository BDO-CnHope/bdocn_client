# @Time    : 2021/03/15
# @Author  : Naunter
# @Page    : https://github.com/Naunters
# @Page    : https://github.com/BDO-CnHope/bdocn_client

from pathlib import Path
from time_template import time_template

user_home = str(Path.home())
bdocn_conf_dir = (user_home + r'\AppData\Roaming\bdocn_client')
bdo_gamepath = (bdocn_conf_dir + r'\bdocn_gamepath.txt')
bdo_confpath = (bdocn_conf_dir + r'\bdocn_confpath.txt')

def check_save_bdo_gamepath():
    time_template()
    print("save_bdocn_conf.py >>> def check_save_bdo_gamepath()")
    if Path(bdo_gamepath).is_file() is True and Path(bdo_gamepath).stat().st_size != 0:
        f = open(bdo_gamepath)
        conf = f.read()
        f.close()
        print("save_bdocn_conf.py >>> def check_save_bdo_gamepath() >>> True, conf: "+str(conf))
        return conf
    else:
        print("save_bdocn_conf.py >>> def check_save_bdo_gamepath(): False")
        return False

def check_save_bdo_confpath():
    time_template()
    print("save_bdocn_conf.py >>> def check_save_bdo_confpath()")
    if Path(bdo_confpath).is_file() is True and Path(bdo_confpath).stat().st_size != 0:
        f = open(bdo_confpath)
        conf = f.read()
        f.close()
        print("save_bdocn_conf.py >>> def check_save_bdo_confpath() >>> True, conf: "+str(conf))
        return conf
    else:
        print("save_bdocn_conf.py >>> def check_save_bdo_confpath() >>> False")
        return False

def create_bdocn_conf_dir():
    time_template()
    print("save_bdocn_conf.py >>> def create_bdocn_conf_dir()")
    print("save_bdocn_conf.py >>> def create_bdocn_conf_dir() >>> bdocn_conf_dir: "+str(bdocn_conf_dir))
    if Path(bdocn_conf_dir).is_dir() is True:
        return bdocn_conf_dir
    else:
        Path(bdocn_conf_dir).mkdir(parents=True, exist_ok=True)
        return bdocn_conf_dir

def save_bdo_gamepath(path):
    time_template()
    print("save_bdocn_conf.py >>> def save_bdo_gamepath(dir)")
    print("save_bdocn_conf.py >>> def save_bdo_gamepath(dir) >>> bdo_gamepath: "+str(bdo_gamepath))
    f = open(bdo_gamepath,"w+")
    t = str(path)
    f.write(t)
    f.close()

def save_bdo_confpath(path):
    time_template()
    print("save_bdocn_conf.py >>> def save_bdo_confpath(dir)")
    print("save_bdocn_conf.py >>> def save_bdo_confpath(dir) >>> bdo_confpath: "+str(bdo_confpath))
    f = open(bdo_confpath,"w+")
    t = str(path)
    f.write(t)
    f.close()