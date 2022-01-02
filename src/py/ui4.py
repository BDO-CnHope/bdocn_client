# @Time    : 2022/01/01
# @Author  : Naunter
# @Page    : https://github.com/Naunters
# @Page    : https://github.com/BDO-CnHope/bdocn_client

import tkinter as tk
from tkinter.messagebox import showinfo,askyesno
from pathlib import Path
from subprocess import run

from time_template import time_template
from hyperlinks import hyperlinks
from thread_function import thread_it
import save_bdocn_conf
import select_bdo_game_dir
import select_bdo_game_conf
import execute_list
import replace_text
import loc_lang

bdocn_version = 'v3.2022010100'
bdocn_up_date = '2022/01/01'

class Application:
    def __init__(self, master=None):
        self.main_window = tk.Frame(master)
        self.main_window.config(background='#f2f2f2', height='680', width='600')
        self.main_window.pack(side='top')
        self.left_panel_top = tk.LabelFrame(self.main_window)
        self.left_panel_top.config(font='{Microsoft YaHei} 12 {bold}', foreground='#ff0000', height='200', relief='groove', text='注意事项')
        self.left_panel_top.config(width='200')
        self.left_panel_top.place(anchor='nw', height='150', width='290', x='0', y='0')
        self.left_top_panel_text = tk.Text(self.left_panel_top)
        self.left_top_panel_text.config(background='#f2f2f2', font='{Microsoft YaHei} 10 {}', height='10', relief='flat')
        self.left_top_panel_text.config(state='disabled', width='50')
        _text_ = r'''* 本程序是开源和免费的, 默认发布在Github, 如遇收费请勿上当受骗！
* 如有问题, 请去Github提交issue!
* 汉化文本来自黑沙台服,请以黑沙美服官方文本为准！
* 请文明游戏, 保持良好的游戏环境！'''
        self.left_top_panel_text.configure(state='normal')
        self.left_top_panel_text.insert('0.0', _text_)
        self.left_top_panel_text.configure(state='disabled')
        self.left_top_panel_text.place(anchor='nw', height='120', width='280', x='0', y='0')
        self.left_panel_body = tk.LabelFrame(self.main_window)
        self.left_panel_body_text = tk.Text(self.left_panel_body)
        self.left_panel_body_text.config(background='#f2f2f2', font='{Microsoft YaHei} 10 {}', height='10', relief='flat')
        self.left_panel_body.config(background='#f2f2f2', font='{Microsoft YaHei} 12 {bold}', foreground='#ff8000', height='200', text='汉化指南')
        self.left_panel_body.config(width='200')
        self.left_panel_body.place(anchor='nw', height='450', width='290', x='0', y='150')
        self.left_panel_body_text = tk.Text(self.left_panel_body)
        self.left_panel_body_text.config(background='#f2f2f2', font='{Microsoft YaHei} 10 {}', relief='flat')
        self.left_panel_body_text.config(state='disabled', width='50')
        client_notice = r'''* 首先运行黑沙的启动器, 等待启动器完成所有的更新(就是当进度条显示100%)。保持黑沙启动器开启的状态下执行汉化任务。

* 【例子】黑沙的游戏文件目录路径: 
C:\\Program Files (x86)\\Steam\\steamapps\\common\\Black Desert Online\\

* 【例子】黑沙的配置文件路径:
C:\\Users\\你的用户名\\Documents\\Black Desert\\GameOption.txt

** 如没有找到GameOption.txt, 请先运行一遍黑沙后, 退出游戏再重新执行汉化。

* Steam端用户如出现问题, 请重新校验游戏文件后再重新执行汉化。

* 网络波动等因素导致下载会比较慢, 请耐心等待。

** 如卡住请尝试关闭汉化工具后重试。'''
        self.left_panel_body_text.configure(state='normal')
        self.left_panel_body_text.insert('0.0', client_notice)
        self.left_panel_body_text.configure(state='disabled')
        self.left_panel_body_text.place(anchor='nw', height='420', width='280', x='0', y='0')
        self.left_panel_bottom = tk.LabelFrame(self.main_window)
        self.left_panel_bottom.config(background='#f2f2f2', font='{Microsoft YaHei} 10 {bold}', relief='groove')
        self.left_panel_bottom.config(text='作者')
        self.left_panel_bottom.place(anchor='nw', height='80', width='290', x='0', y='600')
        self.left_panel_bottom_text = tk.Text(self.left_panel_bottom)
        self.left_panel_bottom_text.config(background='#f2f2f2', font='{Microsoft YaHei} 8 {}', relief='flat')
        self.left_panel_bottom_text.config(state='disabled', width='50')
        _text_ = '''Created by Naunter@Github
Version:    '''+ bdocn_version +'''
Updated:    '''+ bdocn_up_date +'''
'''
        self.left_panel_bottom_text.configure(state='normal')
        self.left_panel_bottom_text.insert('0.0', _text_)
        self.left_panel_bottom_text.configure(state='disabled')
        self.left_panel_bottom_text.place(anchor='nw', height='50', width='160', x='0', y='0')
        self.left_panel_bottom_button_1 = tk.Button(self.left_panel_bottom)
        self.left_panel_bottom_button_1.config(text='项目主页')
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
        self.save_path_entry_label.configure(text='请选择黑沙的游戏文件目录:')
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
        self.download_method.place(anchor='nw', height='60', width='300', x='300', y='140')
        self.dmVar = tk.StringVar(value='1')
        self.download_method_radiobutton_1 = tk.Radiobutton(self.download_method)
        self.download_method_radiobutton_1.config(font='{Microsoft YaHei} 10 {}', text='从国外服务器下载', value='1', variable=self.dmVar)
        self.download_method_radiobutton_1.place(anchor='nw', x='0', y='0')
        self.download_method_radiobutton_2 = tk.Radiobutton(self.download_method)
        self.download_method_radiobutton_2.config(font='{Microsoft YaHei} 10 {}', text='从国内服务器下载', value='2', variable=self.dmVar)
        self.download_method_radiobutton_2.place(anchor='nw', x='160', y='0')
        self.hanhua_method = tk.LabelFrame(self.main_window)
        self.hanhua_method.config(background='#f2f2f2', font='{Microsoft YaHei} 12 {bold}', foreground='#008080', height='200', text='3. 汉化方式')
        self.hanhua_method.config(width='200')
        self.hanhua_method.place(anchor='nw', height='180', width='300', x='300', y='200')
        self.hmVar=tk.IntVar()
        self.hmVar.set(1)
        self.hanhua_method_radiobutton_1 = tk.Radiobutton(self.hanhua_method)
        self.hanhua_method_radiobutton_1.config(font='{Microsoft YaHei} 12 {}', text='简体汉化(加强版)', variable=self.hmVar, value='1')
        self.hanhua_method_radiobutton_1.place(anchor='nw', x='0', y='0')
        self.hanhua_method_radiobutton_2 = tk.Radiobutton(self.hanhua_method)
        self.hanhua_method_radiobutton_2.config(font='{Microsoft YaHei} 12 {}', text='繁体汉化', variable=self.hmVar, value='2')
        self.hanhua_method_radiobutton_2.place(anchor='nw', x='0', y='30')
        self.hanhua_method_radiobutton_3 = tk.Radiobutton(self.hanhua_method)
        self.hanhua_method_radiobutton_3.config(font='{Microsoft YaHei} 12 {}', text='不汉化，只安装字体', variable=self.hmVar, value='3')
        self.hanhua_method_radiobutton_3.place(anchor='nw', x='0', y='60')
        self.hanhua_method_radiobutton_4 = tk.Radiobutton(self.hanhua_method)
        self.hanhua_method_radiobutton_4.config(font='{Microsoft YaHei} 12 {}', text='清除汉化，恢复成英文', variable=self.hmVar, value='4')
        self.hanhua_method_radiobutton_4.place(anchor='nw', x='0', y='90')
        self.usefontVar = tk.StringVar(value='1')
        self.no_font_change = tk.Checkbutton(self.hanhua_method)
        self.no_font_change.configure(font='{Microsoft YaHei} 9 {}', relief='flat', text='不覆盖现有的汉化字体 (首次使用汉化请取消勾选)', variable=self.usefontVar)
        self.no_font_change.place(anchor='nw', x='0', y='120')
        self.select_server = tk.LabelFrame(self.main_window)
        self.select_server.config(font='{Microsoft YaHei} 12 {bold}', foreground='#800040', height='200', text='4. 选择黑沙原本所用的语言', width='200')
        self.select_server.place(anchor='nw', height='220', width='300', x='300', y='380')
        self.select_server_listbox = tk.Listbox(self.select_server)
        self.select_server_scrollbar = tk.Scrollbar(self.select_server)
        self.select_server_scrollbar.configure(orient='vertical', command=self.select_server_listbox.yview)
        self.select_server_scrollbar.pack(side="right", fill="both")
        self.select_server_listbox.place(anchor='nw', height='190', width='285', x='5', y='0')
        self.select_server_listbox.configure(font='{Microsoft YaHei} 10', justify='left', yscrollcommand=self.select_server_scrollbar.set)
        self.select_server_listbox.insert(1, '欧美服(英语): languagedata_en.loc')
        self.select_server_listbox.insert(2, '俄服(俄语):   languagedata_ru.loc')
        self.select_server_listbox.insert(3, '日服(日语):   languagedata_jp.loc')
        self.select_server_listbox.insert(4, '欧美服(法语): languagedata_fr.loc')
        self.select_server_listbox.insert(5, '台服(繁体中文):   languagedata_tw.loc')
        self.select_server_listbox.insert(6, '大洋服(葡萄牙语): languagedata_pt.loc')

        self.process_panel = tk.LabelFrame(self.main_window)
        self.process_panel.config(font='{Microsoft YaHei} 12 {bold}', foreground='#008000', height='200', text='5. 执行汉化', width='200')
        self.process_panel.place(anchor='nw', height='80', width='300', x='300', y='600')
        self.process_panel_button_1 = tk.Button(self.process_panel)
        self.process_panel_button_1.config(font='{Microsoft YaHei} 12 {bold}', background='#008000', foreground='white', text='点击执行汉化')
        self.process_panel_button_1.configure(command=lambda :thread_it(self.start_button))
        self.process_panel_button_1.place(anchor='nw', height='50', width='285', x='5', y='0')
 
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

        def bdo_game_dir_resource_ini():
            if a is True and self.output_bdo_game_dir() != False:
                bdo_game_dir_resource_ini = (self.output_bdo_game_dir() + r'\\Resource.ini')
                print("bdo_game_dir_resource_ini: "+str(bdo_game_dir_resource_ini))
                return bdo_game_dir_resource_ini
            else: 
                return False

        if (bdo_game_dir() and bdo_conf_path()) != False:
            bdo_game_dir = str(bdo_game_dir())
            bdo_conf_path = str(bdo_conf_path())
            bdo_game_dir_resource_ini = str(bdo_game_dir_resource_ini())
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

            selection = self.select_server_listbox.curselection()

            try:
                if str(selection[0]) == '0' or str(selection) == '':
                    pass
                elif str(selection[0]) == '1':
                    loc_lang.loc_ru(bdo_game_dir)
                elif str(selection[0]) == '2':
                    loc_lang.loc_jp(bdo_game_dir)
                elif str(selection[0]) == '3':
                    loc_lang.loc_fr(bdo_game_dir)
                elif str(selection[0]) == '4':
                    loc_lang.loc_tw(bdo_game_dir)
                elif str(selection[0]) == '5':
                    loc_lang.loc_pt(bdo_game_dir)
            except:
                print("ui4.py >>> def start_button(self) >>> try selection error")
                pass

            try:
                replace_text.change_ui_font(bdo_conf_path)
            except:
                pass

            try:
                if Path(save_bdocn_conf.create_bdocn_conf_dir()).is_dir() is True:
                    print("ui4.py >>> Path(save_bdocn_conf.create_bdocn_conf_dir()).is_dir() is: " + str(save_bdocn_conf.create_bdocn_conf_dir))
                    save_bdocn_conf.save_bdo_gamepath(bdo_game_dir)
                    save_bdocn_conf.save_bdo_confpath(bdo_conf_path)
                    save_bdocn_conf.save_bdo_downloadpath(dm)
                    save_bdocn_conf.save_bdo_hanhuapath(hm)
                    save_bdocn_conf.save_bdo_langpath(str(selection[0]))
            except:
                pass

    def run(self):
        time_template()
        print("ui4.py >>> def run(self)")
        self.mainwindow.mainloop()
