# @Time    : 2021/03/14
# @Author  : Naunter
# @Page    : https://github.com/Naunters
# @Page    : https://github.com/BDO-CnHope/bdocn_client

from re import sub
from pathlib import Path
from getpass import getuser
from datetime import datetime

time_stamp = datetime.now()

user_name = getuser()
bdo_conf_path = (r'C:/Users/' + user_name + r'/Documents/Black Desert/')
bdo_conf = (r'C:/Users/' + user_name + r'/Documents/Black Desert/GameOption.txt')

def no_bdo_conf_dir():
    print("[BEGIN] no_bdo_conf_dir >>> " + str(time_stamp.strftime('%Y.%m.%d-%H:%M:%S')) + "\n")
    if not Path(bdo_conf_path).is_dir():
        return True

def no_bdo_conf():
    print("[BEGIN] no_bdo_conf >>> " + str(time_stamp.strftime('%Y.%m.%d-%H:%M:%S')) + "\n")
    if not Path(bdo_conf).is_file():
        return True

def change_bdo_font_conf(dir):
    print("[BEGIN] change_bdo_font_conf >>> " + str(time_stamp.strftime('%Y.%m.%d-%H:%M:%S')) + "\n")
    if dir == '' and no_bdo_conf() != True :
        dir = bdo_conf
    else:
        print("[ERROR] change_bdo_font_conf => no_bdo_conf() = True ")

    print("change_bdo_font_conf: BDO conf path: " + str(dir))
    # open GameOption.txt
    f = open(dir,"r+")
    conf = f.read()
    t = sub(r"(UIFontType =.*)", r"UIFontType = 1", conf)
    f.write(t)
    f.close()

