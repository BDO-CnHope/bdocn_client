# @Time    : 2021/07/10
# @Author  : Naunter
# @Page    : https://github.com/Naunters
# @Page    : https://github.com/BDO-CnHope/bdocn_client

from pathlib import Path
from time_template import time_template

user_home = str(Path.home())
bdocn_conf_dir = (user_home + r'\AppData\Roaming\bdocn_client')

bdo_gamepath = (bdocn_conf_dir + r'\bdocn_gamepath.txt')
bdo_confpath = (bdocn_conf_dir + r'\bdocn_confpath.txt')

bdo_downloadpath = (bdocn_conf_dir + r'\bdocn_downloadpath.txt')
bdo_hanhuapath = (bdocn_conf_dir + r'\bdocn_hanhuapath.txt')
bdo_langpath = (bdocn_conf_dir + r'\bdocn_langpath.txt')

def create_bdocn_conf_dir():
    time_template()
    print("save_bdocn_conf.py >>> def create_bdocn_conf_dir()")
    print("save_bdocn_conf.py >>> def create_bdocn_conf_dir() >>> bdocn_conf_dir: "+str(bdocn_conf_dir))
    if Path(bdocn_conf_dir).is_dir() is True:
        return bdocn_conf_dir
    else:
        Path(bdocn_conf_dir).mkdir(parents=True, exist_ok=True)
        return bdocn_conf_dir

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

def check_save_bdo_downloadpath():
    time_template()
    print("save_bdocn_conf.py >>> def check_save_bdo_downloadpath()")
    if Path(bdo_downloadpath).is_file() is True and Path(bdo_downloadpath).stat().st_size != 0:
        f = open(bdo_downloadpath)
        conf = f.read()
        f.close()
        print("save_bdocn_conf.py >>> def check_save_bdo_downloadpath() >>> True, conf: "+str(conf))
        return conf
    else:
        print("save_bdocn_conf.py >>> def check_save_bdo_downloadpath() >>> False")
        return False

def check_save_bdo_hanhuapath():
    time_template()
    print("save_bdocn_conf.py >>> def check_save_bdo_hanhuapath()")
    if Path(bdo_hanhuapath).is_file() is True and Path(bdo_hanhuapath).stat().st_size != 0:
        f = open(bdo_hanhuapath)
        conf = f.read()
        f.close()
        print("save_bdocn_conf.py >>> def check_save_bdo_hanhuapath() >>> True, conf: "+str(conf))
        return conf
    else:
        print("save_bdocn_conf.py >>> def check_save_bdo_hanhuapath() >>> False")
        return False

def check_save_bdo_langpath():
    time_template()
    print("save_bdocn_conf.py >>> def check_save_bdo_langpath()")
    if Path(bdo_langpath).is_file() is True and Path(bdo_langpath).stat().st_size != 0:
        f = open(bdo_langpath)
        conf = f.read()
        f.close()
        print("save_bdocn_conf.py >>> def check_save_bdo_langpath() >>> True, conf: "+str(conf))
        return conf
    else:
        print("save_bdocn_conf.py >>> def check_save_bdo_langpath() >>> False")
        return False

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

def save_bdo_downloadpath(path):
    time_template()
    print("save_bdocn_conf.py >>> def save_bdo_downloadpath(dir)")
    print("save_bdocn_conf.py >>> def save_bdo_downloadpath(dir) >>> bdo_downloadpath: "+str(bdo_downloadpath))
    f = open(bdo_downloadpath,"w+")
    t = str(path)
    f.write(t)
    f.close()

def save_bdo_hanhuapath(path):
    time_template()
    print("save_bdocn_conf.py >>> def save_bdo_hanhuapath(dir)")
    print("save_bdocn_conf.py >>> def save_bdo_hanhuapath(dir) >>> bdo_hanhuapath: "+str(bdo_hanhuapath))
    f = open(bdo_hanhuapath,"w+")
    t = str(path)
    f.write(t)
    f.close()

def save_bdo_langpath(path):
    time_template()
    print("save_bdocn_conf.py >>> def save_bdo_langpath(dir)")
    print("save_bdocn_conf.py >>> def save_bdo_langpath(dir) >>> bdo_langpath: "+str(bdo_langpath))
    f = open(bdo_langpath,"w+")
    t = str(path)
    f.write(t)
    f.close()