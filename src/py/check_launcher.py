# @Time    : 2021/03/12
# @Author  : Naunter
# @Page    : https://github.com/Naunters
# @Page    : https://github.com/BDO-CnHope/bdocn_client

from os.path import expandvars
from re import sub
import os

bdo_conf_path = expandvars(R"C:\Users\$USERNAME\Documents\Black Desert\GameOption.txt")

def no_bdo_conf_dir():
    if not os.path.exists(bdo_conf_path):
        return True

def change_bdo_font_conf():
    # open GameOption.txt
    f = open(bdo_conf_path,"r+")
    conf = f.read()
    t = sub(r"(UIFontType =.*)", r"UIFontType = 1", conf)
    f.write(t)
    f.close()