# @Time    : 2021/03/13
# @Author  : Naunter
# @Page    : https://github.com/Naunters
# @Page    : https://github.com/BDO-CnHope/bdocn_client

from os.path import expandvars
from re import sub
from os.path import exists

bdo_conf_path = expandvars(R"C:\Users\$USERNAME\Documents\Black Desert\GameOption.txt")

def no_bdo_conf_dir():
    if not exists(bdo_conf_path):
        return True

def change_bdo_font_conf(dir):
    if dir == '':
        dir = bdo_conf_path

    print("BDO conf path: " + dir)
    # open GameOption.txt
    f = open(dir,"r+")
    conf = f.read()
    t = sub(r"(UIFontType =.*)", r"UIFontType = 1", conf)
    f.write(t)
    f.close()