# @Time    : 2022/01/01
# @Author  : Naunter
# @Page    : https://github.com/Naunters
# @Page    : https://github.com/BDO-CnHope/bdocn_client

import tkinter as tk
from tkinter.messagebox import askyesno,showinfo
from subprocess import run,Popen

from time_template import time_template
from thread_function import thread_it
from hyperlinks import hyperlinks
import check_client_version
import save_bdocn_conf
import select_bdo_game_dir
import select_bdo_game_conf
import ui4
import new_update

bdocn_version = '2022010100'

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

try:
    if save_bdocn_conf.check_save_bdo_confpath() != False:
        selected_dir = save_bdocn_conf.check_save_bdo_confpath()
        print("run.py >>> def select_game_conf(self) >>> if selected_dir: "+str(selected_dir))
        app.insert_conf_path_entry(selected_dir)
    elif select_bdo_game_conf.auto_select_dir() != False:
        selected_dir = select_bdo_game_conf.auto_select_dir()
        print("run.py >>> def select_bdo_game_conf(self) >>> select_bdo_game_conf.auto_select_dir(): "+str(selected_dir))
        app.insert_conf_path_entry(selected_dir)
except:
    pass

if save_bdocn_conf.check_save_bdo_downloadpath() != False:
    selected_dir = save_bdocn_conf.check_save_bdo_downloadpath()
    print("run.py >>> def select_bdo_downloadpath(self) >>> if selected_dir: "+str(selected_dir))
    app.dmVar.set(selected_dir)

if save_bdocn_conf.check_save_bdo_hanhuapath() != False:
    selected_dir = save_bdocn_conf.check_save_bdo_hanhuapath()
    print("run.py >>> def select_bdo_hanhuapath(self) >>> if selected_dir: "+str(selected_dir))
    app.hmVar.set(selected_dir)

try:
    if save_bdocn_conf.check_save_bdo_langpath() != False:
        selected_dir = save_bdocn_conf.check_save_bdo_langpath()
        print("run.py >>> def select_bdo_langpath(self) >>> if selected_dir: "+str(selected_dir))
        app.select_server_listbox.select_set(selected_dir)
    else:
        app.select_server_listbox.select_set(0)
except:
    pass

ask_run_bdo = askyesno('提示', '是否启动Steam的黑色沙漠？')
if ask_run_bdo == True:
    run("cmd /c start steam://run/582660")
    showinfo('提示', '请等待黑沙更新完毕后再执行汉化任务!')
else:
    showinfo('提示', '请先运行黑色沙漠的启动器并等待其更新完毕后, 再执行汉化任务!')

check = check_client_version.get_version()
if check != bdocn_version and check is not False:
    print("run.py >>> check_client_version.get_version() is True")
    new_update.run_gui()
else:
    thread_it(app.run(), '')