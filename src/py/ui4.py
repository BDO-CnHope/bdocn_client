# @Time    : 2021/03/18
# @Author  : Naunter
# @Page    : https://github.com/Naunters
# @Page    : https://github.com/BDO-CnHope/bdocn_client

import tkinter as tk
from tkinter.messagebox import showinfo,askyesno
from pathlib import Path

from time_template import time_template
from hyperlinks import hyperlinks
from thread_function import thread_it
import save_bdocn_conf
import select_bdo_game_dir
import select_bdo_game_conf
import execute_list
import replace_text

class Application:
    def __init__(self, master=None):
        self.main_window = tk.Frame(master)
        self.main_window.config(background='#f2f2f2', height='600', width='600')
        self.main_window.pack(side='top')
        self.left_panel_top = tk.LabelFrame(self.main_window)
        self.left_panel_top.config(font='{Microsoft YaHei} 12 {bold}', foreground='#ff0000', height='200', relief='groove', text='注意事项')
        self.left_panel_top.config(width='200')
        self.left_panel_top.place(anchor='nw', height='150', width='290', x='0', y='0')
        self.left_top_panel_text = tk.Text(self.left_panel_top)
        self.left_top_panel_text.config(background='#f2f2f2', font='{Microsoft YaHei} 10 {}', height='10', relief='flat')
        self.left_top_panel_text.config(state='disabled', width='50')
        _text_ = r'''1. 汉化文本来自于黑沙台服，准确内容请以官方美服为准！
2. 如有问题，请去Github提交issue。
3. 本程序是开源和免费的，如遇收费请勿上当受骗！
4. 请文明游戏，保持良好的游戏环境！'''
        self.left_top_panel_text.configure(state='normal')
        self.left_top_panel_text.insert('0.0', _text_)
        self.left_top_panel_text.configure(state='disabled')
        self.left_top_panel_text.place(anchor='nw', height='120', width='280', x='0', y='0')
        self.left_panel_body = tk.LabelFrame(self.main_window)
        self.left_panel_body_text = tk.Text(self.left_panel_body)
        self.left_panel_body_text.config(background='#f2f2f2', font='{Microsoft YaHei} 10 {}', height='10', relief='flat')
        self.left_panel_body.config(background='#f2f2f2', font='{Microsoft YaHei} 12 {bold}', foreground='#ff8000', height='200', text='使用方法')
        self.left_panel_body.config(width='200')
        self.left_panel_body.place(anchor='nw', height='370', width='290', x='0', y='150')
        self.left_panel_body_text = tk.Text(self.left_panel_body)
        self.left_panel_body_text.config(background='#f2f2f2', font='{Microsoft YaHei} 10 {}', relief='flat')
        self.left_panel_body_text.config(state='disabled', width='50')
        client_notice = r'''1. 执行汉化前，请先【运行黑沙的启动器】并等待其更新完毕 (进度显示100%)！
2. 选择正确的【黑沙的游戏目录】
3. 汉化工具默认会自动匹配黑纱的配置文件, 如失败请手动选择
4. 根据需求选择你要汉化的方式
5. 点击运行执行汉化

* 举例Steam的黑沙路径: 
C:\Program Files (x86)\Steam\steamapps\common\Black Desert Online\

* 举例Steam的黑沙配置路径(请确认文件夹里面包含GameOption.txt):
C:\Users\你的用户名\Documents\Black Desert\GameOption.txt

* Steam端用户如出现问题，请重新校验游戏文件后再重新运行一次本汉化工具。
* 网络波动等因素导致下载会比较慢，请耐心等待'''
        self.left_panel_body_text.configure(state='normal')
        self.left_panel_body_text.insert('0.0', client_notice)
        self.left_panel_body_text.configure(state='disabled')
        self.left_panel_body_text.place(anchor='nw', height='340', width='280', x='0', y='0')
        self.left_panel_bottom = tk.LabelFrame(self.main_window)
        self.left_panel_bottom.config(background='#f2f2f2', font='{Microsoft YaHei} 10 {bold}', relief='groove')
        self.left_panel_bottom.config(text='来源', width='200')
        self.left_panel_bottom.place(anchor='nw', height='80', width='290', x='0', y='520')
        self.left_panel_bottom_text = tk.Text(self.left_panel_bottom)
        self.left_panel_bottom_text.config(background='#f2f2f2', font='{Microsoft YaHei} 8 {}', relief='flat')
        self.left_panel_bottom_text.config(state='disabled', width='50')
        _text_ = ''' Create by Naunter
 Version:    2021031404
 Date:   2021/03/18
'''
        self.left_panel_bottom_text.configure(state='normal')
        self.left_panel_bottom_text.insert('0.0', _text_)
        self.left_panel_bottom_text.configure(state='disabled')
        self.left_panel_bottom_text.place(anchor='nw', height='50', width='150', x='0', y='0')
        self.left_panel_bottom_button_1 = tk.Button(self.left_panel_bottom)
        self.left_panel_bottom_button_1.config(text='Github项目主页')
        self.left_panel_bottom_button_1.place(anchor='nw', height='26', width='90', x='190', y='0')
        self.left_panel_bottom_button_1.configure(command=lambda :thread_it(self.hyperlinks(1)))
        self.left_panel_bottom_button_2 = tk.Button(self.left_panel_bottom)
        self.left_panel_bottom_button_2.config(text='视频演示')
        self.left_panel_bottom_button_2.place(anchor='nw', height='26', width='90', x='190', y='30')
        self.left_panel_bottom_button_2.configure(command=lambda :thread_it(self.hyperlinks(2)))
        self.save_path = tk.LabelFrame(self.main_window)
        self.save_path.config(background='#f2f2f2', font='{Microsoft YaHei} 12 {bold}', foreground='#0000ff', height='200', relief='groove')
        self.save_path.config(text='1. 文件保存路径', width='200')
        self.save_path.place(anchor='nw', height='140', width='300', x='300', y='0')
        self.save_path_entry_label = tk.Label(self.save_path)
        self.save_path_entry_label.configure(text='请选择黑沙的游戏根目录:')
        self.save_path_entry_label.place(anchor='nw', height='15', x='3', y='3')
        self.save_path_entry = tk.Entry(self.save_path)
        self.save_path_entry.config(font='{Microsoft YaHei} 10 {}')
        self.save_path_entry_text = ''''''
        self.save_path_entry.delete('0', 'end')
        self.save_path_entry.insert('0', self.save_path_entry_text)
        self.save_path_entry.place(anchor='nw', height='25', width='210', x='5', y='23')
        self.save_path_button = tk.Button(self.save_path)
        self.save_path_button.config(font='{Microsoft YaHei} 9 {}', text='打开目录...')
        self.save_path_button.configure(command=lambda :thread_it(self.select_bdo_game_dir))
        self.save_path_button.place(anchor='nw', height='30', width='70', x='220', y='20')
        self.conf_path_entry_label = tk.Label(self.save_path)
        self.conf_path_entry_label.configure(text='如自动匹配失败, 请手动选择黑沙的配置文件:')
        self.conf_path_entry_label.place(anchor='nw', height='15', x='3', y='60')
        self.conf_path_entry = tk.Entry(self.save_path)
        self.conf_path_entry.config(font='{Microsoft YaHei} 10 {}')
        self.conf_path_entry_text = ''''''
        self.conf_path_entry.delete('0', 'end')
        self.conf_path_entry.insert('0', self.conf_path_entry_text)
        self.conf_path_entry.place(anchor='nw', height='25', width='210', x='5', y='80')
        self.conf_path_button = tk.Button(self.save_path)
        self.conf_path_button.config(font='{Microsoft YaHei} 9 {}', text='打开文件...')
        self.conf_path_button.configure(command=lambda :thread_it(self.select_bdo_conf_path))
        self.conf_path_button.place(anchor='nw', height='30', width='70', x='220', y='77')
        self.download_method = tk.LabelFrame(self.main_window)
        self.download_method.config(background='#f2f2f2', font='{Microsoft YaHei} 12 {bold}', foreground='#004080', height='200', relief='groove')
        self.download_method.config(text='2. 汉化包下载线路', width='200')
        self.download_method.place(anchor='nw', height='60', width='300', x='300', y='150')
        self.dmVar = tk.StringVar(value='1')
        self.download_method_radiobutton_1 = tk.Radiobutton(self.download_method)
        self.download_method_radiobutton_1.config(font='{Microsoft YaHei} 12 {}', text='海外下载', value='1', variable=self.dmVar)
        self.download_method_radiobutton_1.place(anchor='nw', x='0', y='0')
        self.download_method_radiobutton_2 = tk.Radiobutton(self.download_method)
        self.download_method_radiobutton_2.config(font='{Microsoft YaHei} 12 {}', text='国内下载', value='2', variable=self.dmVar)
        self.download_method_radiobutton_2.place(anchor='nw', x='180', y='0')
        self.hanhua_method = tk.LabelFrame(self.main_window)
        self.hanhua_method.config(background='#f2f2f2', font='{Microsoft YaHei} 12 {bold}', foreground='#008080', height='200', text='3. 汉化方式')
        self.hanhua_method.config(width='200')
        self.hanhua_method.place(anchor='nw', height='220', width='300', x='300', y='220')
        self.hmVar=tk.IntVar()
        self.hmVar.set(1)
        self.hanhua_method_radiobutton_1 = tk.Radiobutton(self.hanhua_method)
        self.hanhua_method_radiobutton_1.config(font='{Microsoft YaHei} 12 {}', text='简体汉化(加强版)', variable=self.hmVar, value='1')
        self.hanhua_method_radiobutton_1.place(anchor='nw', x='0', y='0')
        self.hanhua_method_radiobutton_2 = tk.Radiobutton(self.hanhua_method)
        self.hanhua_method_radiobutton_2.config(font='{Microsoft YaHei} 12 {}', text='繁体汉化', variable=self.hmVar, value='2')
        self.hanhua_method_radiobutton_2.place(anchor='nw', x='0', y='40')
        self.hanhua_method_radiobutton_3 = tk.Radiobutton(self.hanhua_method)
        self.hanhua_method_radiobutton_3.config(font='{Microsoft YaHei} 12 {}', text='不汉化，只安装字体', variable=self.hmVar, value='3')
        self.hanhua_method_radiobutton_3.place(anchor='nw', x='0', y='80')
        self.hanhua_method_radiobutton_4 = tk.Radiobutton(self.hanhua_method)
        self.hanhua_method_radiobutton_4.config(font='{Microsoft YaHei} 12 {}', text='清除汉化，恢复英文', variable=self.hmVar, value='4')
        self.hanhua_method_radiobutton_4.place(anchor='nw', x='0', y='120')
        self.usefontVar = tk.StringVar(value='1')
        self.no_font_change = tk.Checkbutton(self.hanhua_method)
        self.no_font_change.configure(font='{Microsoft YaHei} 9 {}', relief='flat', text='不覆盖现有的汉化字体 (第一次汉化请取消勾选)', variable=self.usefontVar)
        self.no_font_change.place(anchor='nw', x='0', y='155')
        self.process_panel = tk.LabelFrame(self.main_window)
        self.process_panel.config(font='{Microsoft YaHei} 12 {bold}', foreground='#008000', height='200', text='4. 操作面板', width='200')
        self.process_panel.place(anchor='nw', height='150', width='300', x='300', y='450')
        self.process_panel_button_1 = tk.Button(self.process_panel)
        self.process_panel_button_1.config(font='{Microsoft YaHei} 12 {bold}', background='#008000', foreground='white', text='点击执行汉化')
        self.process_panel_button_1.configure(command=lambda :thread_it(self.start_button))
        self.process_panel_button_1.place(anchor='nw', height='100', width='285', x='5', y='10')
 
        self.mainwindow = self.main_window

    def hyperlinks(self, var):
        time_template()
        print("ui4.py >>> def hyperlinks(self, var)")
        hyperlinks(var)

    def lock_start_button(self):
        self.process_panel_button_1.config(state='disabled')

    def unlock_start_button(self):
        self.process_panel_button_1.config(state='normal')

    def insert_save_path_entry(self, path):
        self.save_path_entry.delete('0', 'end')
        self.save_path_entry.insert('0', path)
    
    def select_bdo_game_dir(self):
        time_template()
        print("ui4.py >>> def user_select_bdo_game_dir(self)")

        selected_dir = select_bdo_game_dir.select_dir()
        print("ui4.py >>> def select_bdo_game_dir(self) >>> selected_dir: "+str(selected_dir))
        self.insert_save_path_entry(selected_dir)

    def output_bdo_game_dir(self):
        time_template()
        print("ui4.py >>> def output_bdo_game_dir(self)")

        inserted_path = str(self.save_path_entry.get())
        print("ui4.py >>> def output_bdo_game_dir(self) >>> inserted_path:"+str(inserted_path))

        if select_bdo_game_dir.output_selected_bdo_game_dir(inserted_path) != False:
            print("ui4.py >>> def output_bdo_game_dir(self) >>> inserted_path != False")
            return inserted_path
        else:
            self.save_path_entry.delete('0', 'end')
            return False

    def insert_conf_path_entry(self, path):
        self.conf_path_entry.delete('0', 'end')
        self.conf_path_entry.insert('0', path)

    def select_bdo_conf_path(self):
        time_template()
        print("ui4.py >>> def select_bdo_conf_path(self)")

        selected_dir = select_bdo_game_conf.select_dir()
        print("ui4.py >>> def select_bdo_conf_path(self) >>> selected_dir: "+str(selected_dir))
        self.insert_conf_path_entry(selected_dir)

    def output_bdo_conf_path(self):
        time_template()
        print("ui4.py >>> def output_bdo_game_dir(self)")

        inserted_path = str(self.conf_path_entry.get())
        print("ui4.py >>> def output_bdo_conf_path(self) >>> inserted_path:"+str(inserted_path))

        if select_bdo_game_conf.check_conf_file(inserted_path) != False:
            print("ui4.py >>> def output_bdo_conf_path(self) >>> inserted_path != False")
            self.insert_conf_path_entry(inserted_path)
            return inserted_path
        else:
            self.conf_path_entry.delete('0', 'end')
            return False

    def start_button(self):
        time_template()
        print("ui4.py >>> def start_button(self)")

        dm = str(self.dmVar.get())
        hm = str(self.hmVar.get())
        fv = str(self.usefontVar.get())
        print("ui4.py >>> def start_button(self):"+" dm: "+ dm + " hm: "+ hm)
        a = askyesno('提示', '要执行此操作吗')

        def bdo_game_dir():
            if a is True and self.output_bdo_game_dir() != False:
                bdo_game_dir = self.output_bdo_game_dir()
                print("bdo_game_dir: "+str(bdo_game_dir))
                return bdo_game_dir
            else: 
                return False

        def bdo_conf_path():
            if a is True and self.output_bdo_conf_path() != False:
                bdo_conf_path = self.output_bdo_conf_path()
                print("bdo_game_dir: "+str(bdo_conf_path))
                return bdo_conf_path
            else: 
                return False

        if (bdo_game_dir() and bdo_conf_path()) != False:
            bdo_game_dir = str(bdo_game_dir())
            bdo_conf_path = str(bdo_conf_path())
            if a is True and dm == '1':
                print("ui4.py >>> if a is True and dm == 1")
                if hm == '1':
                    print("ui4.py >>> def start_button(self):1 :1")
                    self.lock_start_button()
                    execute_list.dm1_hm1(bdo_game_dir,fv)
                    self.unlock_start_button()
                    showinfo('提示','汉化已完成！')
                elif hm == '2':
                    print("ui4.py >>> def start_button(self):1 :2")
                    self.lock_start_button()
                    execute_list.dm1_hm2(bdo_game_dir,fv)
                    self.unlock_start_button()
                    showinfo('提示','汉化已完成！')
                elif hm == '3':
                    print("ui4.py >>> def start_button(self):1 :3")
                    self.lock_start_button()
                    execute_list.dm1_hm3(bdo_game_dir,fv)
                    self.unlock_start_button()
                    showinfo('提示','字体已更新！')
                elif hm == '4':
                    print("ui4.py >>> def start_button(self):1 :4")
                    self.lock_start_button()
                    execute_list.dm1_hm4(bdo_game_dir,fv)
                    self.unlock_start_button()
                    showinfo('提示','已恢复为英语！')
                else:
                    pass

            if a is True and dm == '2':
                print("ui4.py >>> while a is True and dm == 2")
                if hm == '1':
                    print("ui4.py >>> def start_button(self):2 :1")
                    self.lock_start_button()
                    execute_list.dm2_hm1(bdo_game_dir,fv)
                    self.unlock_start_button()
                    showinfo('提示','汉化已完成！')
                elif hm == '2':
                    print("ui4.py >>> def start_button(self):2 :2")
                    self.lock_start_button()
                    execute_list.dm2_hm2(bdo_game_dir,fv)
                    self.unlock_start_button()
                    showinfo('提示','汉化已完成！')
                elif hm == '3':
                    print("ui4.py >>> def start_button(self):2 :3")
                    self.lock_start_button()
                    execute_list.dm2_hm3(bdo_game_dir,fv)
                    self.unlock_start_button()
                    showinfo('提示','字体已更新！')
                elif hm == '4':
                    print("ui4.py >>> def start_button(self):2 :4")
                    self.lock_start_button()
                    execute_list.dm2_hm4(bdo_game_dir,fv)
                    self.unlock_start_button()
                    showinfo('提示','已恢复为英语！')
                else:
                    pass

            replace_text.change_ui_font(bdo_conf_path)

            if Path(save_bdocn_conf.create_bdocn_conf_dir()).is_dir() is True:
                print("ui4.py >>> Path(save_bdocn_conf.create_bdocn_conf_dir()).is_dir() is: " + str(save_bdocn_conf.create_bdocn_conf_dir))
                save_bdocn_conf.save_bdo_gamepath(bdo_game_dir)
                save_bdocn_conf.save_bdo_confpath(bdo_conf_path)
            else:
                pass

    def run(self):
        time_template()
        print("ui4.py >>> def run(self)")
        self.mainwindow.mainloop()