# @Time    : 2021/07/08
# @Author  : Naunter
# @Page    : https://github.com/Naunters
# @Page    : https://github.com/BDO-CnHope/bdocn_client

import tkinter as tk
from hyperlinks import hyperlinks
from thread_function import thread_it
from time_template import time_template

class UpdateUI:
    def __init__(self, master=None):
        print("new_update.py >>> def __init__()")
        self.second_window = tk.Frame(master)
        self.second_window.config(background='#f2f2f2',height='40', width='600')
        self.second_window.pack()

        self.update_panel_button = tk.Button(self.second_window)
        self.update_panel_button.config(font='{Microsoft YaHei} 12 {bold}', background='orange', foreground='gray1', text='有新的客户端更新, 点击查看')
        self.update_panel_button.configure(command=lambda :thread_it(self.hyperlinks(3)))
        self.update_panel_button.place(height='40', width='600')

    def hyperlinks(self, var):
        time_template()
        print("new_update.py >>> def hyperlinks(self, var)")
        hyperlinks(var)

def run_gui():
    print("new_update.py >>> def run_gui()")
    app = UpdateUI()
    app.second_window.mainloop()