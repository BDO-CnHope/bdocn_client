# @Time    : 2021/03/15
# @Author  : Naunter
# @Page    : https://github.com/Naunters
# @Page    : https://github.com/BDO-CnHope/bdocn_client

from tkinter.messagebox import showwarning
from tkinter.filedialog import askopenfilename
from pathlib import Path

from time_template import time_template

def auto_select_dir():
    time_template()
    print("select_bdo_game_conf.py >>> def auto_select_dir()")
    user_home = str(Path.home())
    default_bdo_conf = (user_home + r'\Documents\Black Desert\GameOption.txt')
    print("select_bdo_game_conf.py >>> def auto_select_dir(): default_bdo_conf: "+str(default_bdo_conf))

    if Path(default_bdo_conf).is_file() != False:
        return default_bdo_conf
    else:
        return False

def select_dir():
    time_template()
    print("select_bdo_game_conf.py >>> def select_dir()")
    path = str(Path.home())
    selected_dir = askopenfilename(title="请选择黑沙配置文件(GameOption.txt)", initialdir = path)
    print("select_bdo_game_conf.py >>> def select_dir(): select_dir: " + str(selected_dir))
    return selected_dir

def check_conf_file(path):
    time_template()
    print("select_bdo_game_conf.py >>> def check_conf_file()")

    bdo_conf = path
    print("select_bdo_game_conf.py >>> def check_conf_file(path): bdo_conf: "+str(bdo_conf))

    if bdo_conf == '':
        print("select_bdo_game_conf.py >>> def check_conf_file(path) >>> if bdo_conf ==: " + str(bdo_conf))
        showwarning("警告","目录为空, 没有找到黑沙的游戏配置文件! \n\n1. 请先完整的运行一次游戏，让其生成游戏配置文件后再重新执行汉化. \n\n2. 请检查配置文件是否生成在当前用户的目录下，亦或是生成在了别的用户目录下。\n\n3. 你也可以尝试手动选择黑沙的游戏配置文件. \n\n例子: "+r"C:/Users/用户名/Documents/Black Desert/GameOption.txt")
        return False
    elif Path(path).is_file() is False:
        print("select_bdo_game_conf.py >>> def check_conf_file(path) >>> elif Path(path).is_file() is: " + str(Path(path).is_file()))
        showwarning("警告","找到的黑沙的游戏配置文件异常(is_file() is False)! \n\n1. 请先完整的运行一次游戏，让其生成游戏配置文件后再重新执行汉化. \n\n2. 请检查配置文件是否生成在当前用户的目录下，亦或是生成在了别的用户目录下。\n\n3. 你也可以尝试手动选择黑沙的游戏配置文件. \n\n4. 到Github上发issue, 请把报错的窗口, 包括黑色的终端窗口里的信息都截图或复制成文本到issue里. \n\n例子: "+r"C:/Users/用户名/Documents/Black Desert/GameOption.txt")
        return False
    elif not 'GameOption.txt' in path:
        print("select_bdo_game_conf.py >>> def check_conf_file(path) >>> not 'GameOption.txt' in path")
        showwarning("警告","没有找到黑沙的游戏配置文件(GameOption.txt)! \n\n1. 请先完整的运行一次游戏，让其生成游戏配置文件后再重新执行汉化. \n\n2. 请检查配置文件是否生成在当前用户的目录下，亦或是生成在了别的用户目录下。\n\n3. 你也可以尝试手动选择黑沙的游戏配置文件. \n\n例子: "+r"C:/Users/用户名/Documents/Black Desert/GameOption.txt")
        return False
    else:
        print("select_bdo_game_conf.py >>> def check_conf_file(path) >>> True, bdo_conf: "+str(bdo_conf))
        return bdo_conf
