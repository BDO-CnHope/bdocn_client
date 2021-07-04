# @Time    : 2021/07/04
# @Author  : Naunter
# @Page    : https://github.com/Naunters
# @Page    : https://github.com/BDO-CnHope/bdocn_client

import tkinter as tk
from tkinter.messagebox import askyesno,showinfo
from subprocess import run

from time_template import time_template
from thread_function import thread_it
from hyperlinks import hyperlinks
import check_client_version
import save_bdocn_conf
import select_bdo_game_dir
import select_bdo_game_conf
import ui4

root = tk.Tk()
root.title('黑色沙漠汉化工具 by Naunter@Github')
root.resizable(False, False)
app = ui4.Application(root)

time_template()
print("run.py >>>")

if save_bdocn_conf.check_save_bdo_gamepath() != False:
    selected_dir = save_bdocn_conf.check_save_bdo_gamepath()
    print("run.py >>> def select_game_path(self) >>> if selected_dir: "+str(selected_dir))
    app.insert_save_path_entry(selected_dir)

if save_bdocn_conf.check_save_bdo_confpath() != False:
    selected_dir = save_bdocn_conf.check_save_bdo_confpath()
    print("run.py >>> def select_game_conf(self) >>> if selected_dir: "+str(selected_dir))
    app.insert_conf_path_entry(selected_dir)
elif select_bdo_game_conf.auto_select_dir() != False:
    selected_dir = select_bdo_game_conf.auto_select_dir()
    print("run.py >>> def select_bdo_game_conf(self) >>> select_bdo_game_conf.auto_select_dir(): "+str(selected_dir))
    app.insert_conf_path_entry(selected_dir)

ask_run_bdo = askyesno('提示', '是否启动Steam 黑色沙漠？')
if ask_run_bdo == True:
    run("cmd /c start steam://run/582660")
    showinfo('提示', '请等待黑沙更新完毕后再执行汉化任务!')
else:
    showinfo('提示', '请先运行黑色沙漠的启动器并等待其更新完毕后, 再执行汉化任务!')

check = check_client_version.get_version()
if check != '2021052501' or check is False:
    print("run.py >>> check_client_version.get_version() is True")
    a = askyesno('提示', '有新版本的客户端，是否查看？')
    if a == True:
        hyperlinks(1)
        thread_it(app.run(), '')
    else:
        thread_it(app.run(), '')
else:
    thread_it(app.run(), '')

