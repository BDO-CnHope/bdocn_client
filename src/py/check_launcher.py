# @Time    : 2021/03/12
# @Author  : Naunter
# @Page    : https://github.com/Naunters
# @Page    : https://github.com/BDO-CnHope/bdocn_client

from os.path import expandvars
from re import sub

def change_bdo_font_conf():
    bdo_conf_path = expandvars(R"C:\Users\$USERNAME\Documents\Black Desert\GameOption.txt")
    # open GameOption.txt
    f = open(bdo_conf_path,"r+")
    conf = f.read()
    t = sub(r"(UIFontType =.*)", r"UIFontType = 1", conf)
    f.write(t)
    f.close()