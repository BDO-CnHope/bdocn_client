# @Time    : 2021/03/15
# @Author  : Naunter
# @Page    : https://github.com/Naunters
# @Page    : https://github.com/BDO-CnHope/bdocn_client

from re import sub
from pathlib import Path
from datetime import datetime

time_stamp = datetime.now()

user_home = str(Path.home())
default_bdo_conf_dir = (user_home + r'/Documents/Black Desert')
default_bdo_conf = (default_bdo_conf_dir + r'/GameOption.txt')

def no_bdo_conf_dir():
    print("[BEGIN] no_bdo_conf_dir >>> " + str(time_stamp.strftime('%Y.%m.%d-%H:%M:%S')) + "\n")
    print("no_bdo_conf_dir: user_home: " + user_home)
    print("no_bdo_conf_dir: default_bdo_conf_dir: " + default_bdo_conf_dir)
    print("no_bdo_conf_dir: is_dir(): " + str(Path(default_bdo_conf_dir).is_dir()))
    print("no_bdo_conf_dir: is_file(): " + str(Path(default_bdo_conf_dir).is_file()))
    if Path(default_bdo_conf_dir).is_dir() is False:
        print("no_bdo_conf_dir: can not find default_bdo_conf_dir")
        return True
    else:
        return False

def no_bdo_conf():
    print("[BEGIN] no_bdo_conf >>> " + str(time_stamp.strftime('%Y.%m.%d-%H:%M:%S')) + "\n")
    print("no_bdo_conf: user_home: " + user_home)
    print("no_bdo_conf: default_bdo_conf: " + default_bdo_conf)
    print("no_bdo_conf: is_dir(): " + str(Path(default_bdo_conf).is_dir()))
    print("no_bdo_conf: is_file(): " + str(Path(default_bdo_conf).is_file()))
    if Path(default_bdo_conf).is_file() is False:
        print("no_bdo_conf: can not find default_bdo_conf")
        return True
    else:
        return False

def change_bdo_font_conf(dir):
    print("[BEGIN] change_bdo_font_conf >>> " + str(time_stamp.strftime('%Y.%m.%d-%H:%M:%S')) + "\n")
    print("change_bdo_font_conf: user_home: " + user_home)
    print("change_bdo_font_conf: default_bdo_conf_dir: " + default_bdo_conf_dir)
    print("change_bdo_font_conf: default_bdo_conf: " + default_bdo_conf)
    if dir == '' and no_bdo_conf() is False :
        dir = default_bdo_conf
    else:
        print("[ERROR] change_bdo_font_conf => no_bdo_conf() = True ")

    print("change_bdo_font_conf: BDO conf path: " + str(dir))
    # open GameOption.txt
    f = open(dir,"r+")
    conf = f.read()
    t = sub(r"(UIFontType =.*)", r"UIFontType = 1", conf)
    f.write(t)
    f.close()

