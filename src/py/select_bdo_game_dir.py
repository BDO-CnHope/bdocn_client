# @Time    : 2021/07/10
# @Author  : Naunter
# @Page    : https://github.com/Naunters
# @Page    : https://github.com/BDO-CnHope/bdocn_client

from tkinter.messagebox import showwarning
from tkinter.filedialog import askdirectory
from pathlib import Path

from time_template import time_template
from save_bdocn_conf import check_save_bdo_gamepath

def select_dir():
    time_template()
    print("select_bdo_game_dir.py >>> def select_dir()")

    if check_save_bdo_gamepath() != False:
        path = check_save_bdo_gamepath()
    else:
        path = r'\\'

    selected_dir = askdirectory(title="请选择黑沙的游戏目录", initialdir = path)
    print("select_bdo_game_dir.py >>> def select_dir() >>> select_dir: " + str(selected_dir))

    return selected_dir

def check_bdo_loc_dir(dir):
    time_template()
    print("select_bdo_game_dir.py >>> def check_bdo_loc_dir()")

    bdo_dir = dir
    bdo_dir_ads = bdo_dir + r'\\ads'
    print("select_bdo_game_dir.py >>> def check_bdo_loc_dir() >>> bdo_dir: "+str(bdo_dir))
    print("select_bdo_game_dir.py >>> def check_bdo_loc_dir() >>> bdo_dir_ads: "+str(bdo_dir_ads))

    if bdo_dir == '':
        print("select_bdo_game_dir.py >>> def check_bdo_loc_dir() >>> if bdo_dir == " + str(bdo_dir))
        showwarning("警告","目录为空, 没有找到黑沙的游戏目录! \n\n例子: " + r"C:\\Program Files (x86)\\Steam\\steamapps\\common\\Black Desert Online")
        return False
    elif Path(bdo_dir_ads).is_dir() is False:
        print("select_bdo_game_dir.py >>> def check_bdo_loc_dir() >>> Path(bdo_dir_ads).is_dir() is: " + str(Path(bdo_dir_ads).is_dir()))
        showwarning("警告","没有找到黑沙的语言文件目录" + r"(\\ads)" + "，请检查游戏文件的完整性! \n\n例子: " + r"C:\\Program Files (x86)\\Steam\\steamapps\\common\\Black Desert Online\\ads")
        return False
    else:
        print("select_bdo_game_dir.py >>> def check_bdo_loc_dir() >>> return bdo_dir_ads: "+str(bdo_dir_ads))
        return bdo_dir_ads

def create_bdo_font_dir(dir):
    time_template()
    print("select_bdo_game_dir.py >>> def create_bdo_font_dir()")

    bdo_dir = dir
    bdo_dir_font = bdo_dir + r'\\prestringtable\\font'
    print("select_bdo_game_dir.py >>> def create_bdo_font_dir() >>> bdo_dir_font: "+str(bdo_dir_font))
    if Path(bdo_dir_font).is_dir() is True:
        return bdo_dir_font
    else:
        Path(bdo_dir_font).mkdir(parents=True, exist_ok=True)
        return bdo_dir_font

def output_selected_bdo_game_dir(dir):
    time_template()
    print("select_bdo_game_dir.py >>> def output_selected_bdo_game_dir()")

    if check_bdo_loc_dir(dir) != False:
        create_bdo_font_dir(dir)
        return dir
    else:
        return False
