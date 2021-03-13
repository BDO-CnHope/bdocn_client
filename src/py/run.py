# @Time    : 2021/03/12
# @Author  : Naunter
# @Page    : https://github.com/Naunters
# @Page    : https://github.com/BDO-CnHope/bdocn_client

import tkinter as tk
from tkinter.messagebox import askyesno,showinfo
import ui4
import check_new
import thread_func


root = tk.Tk()
root.title('黑色沙漠汉化工具 by Naunter')
root.resizable(False, False)
app = ui4.Application(root)

showinfo('提示', '请先运行黑沙的启动器并等待其更新完毕后再执行汉化任务')

if check_new.get_client_version() != '2021031200':
    a = askyesno('提示', '有新版本的客户端，是否查看？')
    if a == True:
        app.hyperlinks(2)
        thread_func.thread_it(app.run(), '')
    else:
        thread_func.thread_it(app.run(), '')
else:
    thread_func.thread_it(app.run(), '')

