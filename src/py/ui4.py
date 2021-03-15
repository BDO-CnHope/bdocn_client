# @Time    : 2021/03/14
# @Author  : Naunter
# @Page    : https://github.com/Naunters
# @Page    : https://github.com/BDO-CnHope/bdocn_client

import tkinter as tk
from tkinter.messagebox import showinfo,askyesno,showwarning
from tkinter.filedialog import askdirectory,askopenfilename
from tkinter.scrolledtext import ScrolledText
from shutil import copy, rmtree
from pathlib import Path
from tempfile import mkdtemp
from datetime import datetime
import webbrowser
import joinfiles
import download
import thread_func
import check_new
import check_launcher

time_stamp = datetime.now()

class Application:
    def __init__(self, master=None):
        # main frame
        self.main_window = tk.Frame(master)
        self.main_window.config(background='#f2f2f2', height='600', width='600')
        self.main_window.pack(side='top')
        # left panel top
        self.left_panel_top = tk.LabelFrame(self.main_window)
        self.left_panel_top.config(font='{Microsoft YaHei} 12 {bold}', foreground='#ff0000', height='200', relief='groove', text='注意事项')
        self.left_panel_top.config(width='200')
        self.left_panel_top.place(anchor='nw', height='150', width='290', x='0', y='0')
        self.left_top_panel_text = tk.Text(self.left_panel_top)
        self.left_top_panel_text.config(background='#f2f2f2', font='{Microsoft YaHei} 10 {}', height='10', relief='flat')
        self.left_top_panel_text.config(state='disabled', width='50')
        _text_ = r'''1. 汉化文本来自于黑沙台服，准确内容请以美服官方为主！
2. 如有问题，请去Github提交issue。
3. 本程序是开源和免费的，如遇收费请勿上当受骗！
4. 请文明游戏，保持良好的游戏环境！'''
        self.left_top_panel_text.configure(state='normal')
        self.left_top_panel_text.insert('0.0', _text_)
        self.left_top_panel_text.configure(state='disabled')
        self.left_top_panel_text.place(anchor='nw', height='120', width='280', x='0', y='0')
        # left panle center
        self.left_panel_body = tk.LabelFrame(self.main_window)
        self.left_panel_body_text = tk.Text(self.left_panel_body)
        self.left_panel_body_text.config(background='#f2f2f2', font='{Microsoft YaHei} 10 {}', height='10', relief='flat')
        self.left_panel_body.config(background='#f2f2f2', font='{Microsoft YaHei} 12 {bold}', foreground='#ff8000', height='200', text='使用方法')
        self.left_panel_body.config(width='200')
        self.left_panel_body.place(anchor='nw', height='370', width='290', x='0', y='150')
        self.left_panel_body_text = tk.Text(self.left_panel_body)
        self.left_panel_body_text.config(background='#f2f2f2', font='{Microsoft YaHei} 10 {}', relief='flat')
        self.left_panel_body_text.config(state='disabled', width='50')
        client_notice = r'''1. 执行汉化前，请先【运行黑沙的启动器】并等待其更新完毕 (显示100%)！
2. 选择正确的【黑沙的游戏目录】
3. 黑沙配置目录默认会自动选择, 可不手选
3. 根据需求选择你要汉化的方式
4. 点击运行执行汉化

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
        # left panel bottom
        self.left_panel_bottom = tk.LabelFrame(self.main_window)
        self.left_panel_bottom.config(background='#f2f2f2', font='{Microsoft YaHei} 10 {bold}', relief='groove')
        self.left_panel_bottom.config(text='来源', width='200')
        self.left_panel_bottom.place(anchor='nw', height='80', width='290', x='0', y='520')
        self.left_panel_bottom_text = tk.Text(self.left_panel_bottom)
        self.left_panel_bottom_text.config(background='#f2f2f2', font='{Microsoft YaHei} 8 {}', relief='flat')
        self.left_panel_bottom_text.config(state='disabled', width='50')
        _text_ = ''' Create by Naunter
 Version:    2021031400
 Date:   2021/03/14
'''
        self.left_panel_bottom_text.configure(state='normal')
        self.left_panel_bottom_text.insert('0.0', _text_)
        self.left_panel_bottom_text.configure(state='disabled')
        self.left_panel_bottom_text.place(anchor='nw', height='50', width='150', x='0', y='0')
        self.left_panel_bottom_button_1 = tk.Button(self.left_panel_bottom)
        self.left_panel_bottom_button_1.config(text='Github')
        self.left_panel_bottom_button_1.place(anchor='nw', height='26', width='80', x='200', y='0')
        self.left_panel_bottom_button_1.configure(command=lambda :thread_func.thread_it(self.hyperlinks(1)))
        self.left_panel_bottom_button_2 = tk.Button(self.left_panel_bottom)
        self.left_panel_bottom_button_2.config(text='Gitee')
        self.left_panel_bottom_button_2.place(anchor='nw', height='26', width='80', x='200', y='30')
        self.left_panel_bottom_button_2.configure(command=lambda :thread_func.thread_it(self.hyperlinks(2)))
        # right top, area 1
        self.save_path = tk.LabelFrame(self.main_window)
        self.save_path.config(background='#f2f2f2', font='{Microsoft YaHei} 12 {bold}', foreground='#0000ff', height='200', relief='groove')
        self.save_path.config(text='1. 文件保存路径', width='200')
        self.save_path.place(anchor='nw', height='120', width='300', x='300', y='0')
        self.save_path_entry_label = tk.Label(self.save_path)
        self.save_path_entry_label.configure(text='请选择黑沙的游戏根目录 :')
        self.save_path_entry_label.place(anchor='nw', height='15', x='3', y='0')
        self.save_path_entry = tk.Entry(self.save_path)
        self.save_path_entry.config(font='{Microsoft YaHei} 10 {}')
        self.save_path_entry_text = '''请选择黑沙的游戏根目录...'''
        self.save_path_entry.delete('0', 'end')
        self.save_path_entry.insert('0', self.save_path_entry_text)
        self.save_path_entry.place(anchor='nw', height='20', width='210', x='5', y='20')
        self.save_path_button = tk.Button(self.save_path)
        self.save_path_button.config(font='{Microsoft YaHei} 9 {}', text='打开...')
        self.save_path_button.configure(command=lambda :thread_func.thread_it(self.select_path))
        self.save_path_button.place(anchor='nw', height='25', width='70', x='220', y='17')
        self.conf_path_entry_label = tk.Label(self.save_path)
        self.conf_path_entry_label.configure(text='手动选择黑沙的配置文件目录 (默认会自动选择) :')
        self.conf_path_entry_label.place(anchor='nw', height='15', x='3', y='45')
        self.conf_path_entry = tk.Entry(self.save_path)
        self.conf_path_entry.config(font='{Microsoft YaHei} 10 {}')
        self.conf_path_entry_text = ''''''
        self.conf_path_entry.delete('0', 'end')
        self.conf_path_entry.insert('0', self.conf_path_entry_text)
        self.conf_path_entry.place(anchor='nw', height='20', width='210', x='5', y='65')
        self.conf_path_button = tk.Button(self.save_path)
        self.conf_path_button.config(font='{Microsoft YaHei} 9 {}', text='打开...')
        self.conf_path_button.configure(command=lambda :thread_func.thread_it(self.select_conf_path))
        self.conf_path_button.place(anchor='nw', height='25', width='70', x='220', y='63')
        # right area 2, select download method
        self.download_method = tk.LabelFrame(self.main_window)
        self.download_method.config(background='#f2f2f2', font='{Microsoft YaHei} 12 {bold}', foreground='#004080', height='200', relief='groove')
        self.download_method.config(text='2. 汉化包下载线路', width='200')
        self.download_method.place(anchor='nw', height='60', width='300', x='300', y='120')
        self.dmVar = tk.StringVar(value="1")
        self.download_method_radiobutton_1 = tk.Radiobutton(self.download_method)
        self.download_method_radiobutton_1.config(font='{Microsoft YaHei} 12 {}', text='海外下载', value="1", variable=self.dmVar)
        self.download_method_radiobutton_1.place(anchor='nw', x='0', y='0')
        self.download_method_radiobutton_2 = tk.Radiobutton(self.download_method)
        self.download_method_radiobutton_2.config(font='{Microsoft YaHei} 12 {}', text='国内下载', value="2", variable=self.dmVar)
        self.download_method_radiobutton_2.place(anchor='nw', x='180', y='0')
        # right area 3, select hanhua method
        self.hanhua_method = tk.LabelFrame(self.main_window)
        self.hanhua_method.config(background='#f2f2f2', font='{Microsoft YaHei} 12 {bold}', foreground='#008080', height='200', text='3. 汉化方式')
        self.hanhua_method.config(width='200')
        self.hanhua_method.place(anchor='nw', height='220', width='300', x='300', y='180')
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
        self.usefontVar = tk.StringVar(value="1")
        self.no_font_change = tk.Checkbutton(self.hanhua_method)
        self.no_font_change.configure(font='{Microsoft YaHei} 9 {}', relief='flat', text='不更新或覆盖现有的汉化字体(只对简繁汉化有效)', variable=self.usefontVar)
        self.no_font_change.place(anchor='nw', x='0', y='155')
        # right area 4
        self.process_panel = tk.LabelFrame(self.main_window)
        self.process_panel.config(font='{Microsoft YaHei} 12 {bold}', foreground='#008000', height='200', text='4. 操作面板', width='200')
        self.process_panel.place(anchor='nw', height='200', width='300', x='300', y='400')
        self.process_panel_button_1 = tk.Button(self.process_panel)
        self.process_panel_button_1.config(font='{Microsoft YaHei} 12 {bold}', background='#008000', foreground='white', text='开始汉化')
        self.process_panel_button_1.configure(command=lambda :thread_func.thread_it(self.start_button))
        self.process_panel_button_1.place(anchor='nw', height='50', width='285', x='5', y='0')
        self.process_panel_progresstext = ScrolledText(self.process_panel)
        self.process_panel_progresstext.config(font='{Microsoft YaHei} 10 {}', relief='groove', state='disabled')
        self.process_panel_progresstext.insert('0.0', '...\n')
        self.process_panel_progresstext.place(anchor='nw', height='110', width='285', x='5', y='60')

        self.mainwindow = self.main_window

    # 将日志输出到输出面板
    def insert_text(self, content):
        print("[BEGIN] insert_text >>> " + str(time_stamp.strftime('%Y.%m.%d-%H:%M:%S')) + "\n")
        self.process_panel_progresstext.config(state='normal')
        self.process_panel_progresstext.insert(tk.END, str(time_stamp.strftime('%Y.%m.%d-%H:%M:%S')) + '\n')
        self.process_panel_progresstext.insert(tk.END, content)
        self.process_panel_progresstext.config(state='disabled')
        print(str(time_stamp.strftime('%Y.%m.%d-%H:%M:%S')) + ' inserted output: '+ content)

    # 超链接
    def hyperlinks(self, var):
        if var == 1 :
            webbrowser.open_new(r"https://github.com/BDO-CnHope/bdocn_client")
        elif var == 2:
            webbrowser.open_new(r"https://gitee.com/bdo-cnhope/bdocn_client")

    # 选择黑沙游戏目录
    def select_path(self):
        print("[BEGIN] select_path >>> " + str(time_stamp.strftime('%Y.%m.%d-%H:%M:%S')) + "\n")
        open_path = askdirectory()
        self.save_path_entry.delete('0', 'end')
        self.save_path_entry.insert('0', open_path)
        self.insert_text('选择了目录: \n'+open_path+'\n')

    def check_bdo_dir(self):
        print("[BEGIN] check_bdo_dir >>> " + str(time_stamp.strftime('%Y.%m.%d-%H:%M:%S')) + "\n")
        todir = self.save_path_entry.get()
        ads_dir = todir + r'/ads/'
        font_dir = todir + r'/prestringtable' + r'/font/'
        if todir == '' or todir == self.save_path_entry_text:
            showinfo('提示','你没有选择正确的目录! ')
            self.insert_text('你没有选择正确的游戏目录! \n')
            return False
        elif not Path(ads_dir).is_dir():
            showinfo('提示','没有找到语言文件目录，请检查游戏完整性!')
            self.insert_text('没有找到语言文件目录，请检查游戏完整性! \n')
            return False
        elif not Path(font_dir).is_dir():
            Path(font_dir).mkdir(parents=True, exist_ok=True)
            return(font_dir)
        elif Path(font_dir).is_dir():
            return(font_dir)

    # 选择黑沙配置目录
    def select_conf_path(self):
        print("[BEGIN] select_conf_path >>> " + str(time_stamp.strftime('%Y.%m.%d-%H:%M:%S')) + "\n")
        open_path = askopenfilename()
        self.conf_path_entry.delete('0', 'end')
        self.conf_path_entry.insert('0', open_path)
        self.insert_text('选择了目录: \n'+open_path+'\n')

    def check_bdo_conf_path(self):
        print("[BEGIN] select_conf_path >>> " + str(time_stamp.strftime('%Y.%m.%d-%H:%M:%S')) + "\n")
        todir = self.conf_path_entry.get()
        print('select_conf_path: conf_dir: ' + str(todir))
        if Path(todir).is_file() or Path(todir).is_dir():
            return(todir)
        elif not Path(todir).is_file() or not Path(todir).is_dir():
            print("[ERROR] check_bdo_conf_path: not Path(todir).is_file()")
            showwarning('警告', '无法找到黑色沙漠的【配置文件】!!! 可能的原因和解决办法: \n\n1. 请先完整的运行一次游戏，让其生成游戏配置文件后再重新执行汉化 (请退出游戏后再执行汉化) \n\n2. 请检查配置文件是否生成在当前用户的目录下，亦或是生成在了别的用户的目录下，比如管理员的用户目录。\n例子: C:/Users/你的用户名/Documents/Black Desert/GameOption.txt')
            return False
        else:
            print("[ERROR] check_bdo_conf_path: else pass")
            pass

    def check_bdo_conf_empty_path(self):
        # 检查BDO的配置文件(路径为空时)
        if self.conf_path_entry.get() == '':
            if check_launcher.no_bdo_conf_dir() == True:
                print("[ERROR] start_button: check_launcher.no_bdo_conf_dir() == True")
                showwarning('警告', '无法找到黑色沙漠的【配置目录】!!! 可能的原因和解决办法: \n\n1. 请先完整的运行一次游戏，让其生成游戏配置文件后再重新执行汉化 (请退出游戏后再执行汉化) \n\n2. 请检查配置文件是否生成在当前用户的目录下，亦或是生成在了别的用户的目录下，比如管理员的用户目录。\n例子: C:/Users/你的用户名/Documents/Black Desert/GameOption.txt \n\n3. 请确认黑沙的配置文件文件夹里面包含GameOption.txt这个文件')
                return False
            elif check_launcher.no_bdo_conf() == True:
                print("[ERROR] start_button: check_launcher.no_bdo_conf() == True")
                showwarning('警告', '无法找到黑色沙漠的【配置文件】!!! 可能的原因和解决办法: \n\n1. 请先完整的运行一次游戏，让其生成游戏配置文件后再重新执行汉化 (请退出游戏后再执行汉化) \n\n2. 请检查配置文件是否生成在当前用户的目录下，亦或是生成在了别的用户的目录下，比如管理员的用户目录。\n例子: C:/Users/你的用户名/Documents/Black Desert/GameOption.txt')
                return False
            else:
                conf_dir = ''
                print("start_button: Selected a default BDO conf path")
                check_launcher.change_bdo_font_conf(conf_dir)
                return True

    def check_loc_hash(self):
        print("[BEGIN] check_loc_hash >>> " + str(time_stamp.strftime('%Y.%m.%d-%H:%M:%S')) + "\n")
        todir = self.save_path_entry.get()
        print("check_loc_hash: todir: " + todir)
        ads_dir = todir + r'/ads/languagedata_en.loc'
        print("check_loc_hash: ads_dir: " + ads_dir)
        if Path(ads_dir).is_dir() or Path(ads_dir).is_file():
            print("check_loc_hash: Found " + ads_dir)
            return(check_new.get_hash(ads_dir))
        else:
            print("check_loc_hash: Can not find " + ads_dir)
            return None

    def check_font_hash(self):
        print("[BEGIN] check_font_hash >>> " + str(time_stamp.strftime('%Y.%m.%d-%H:%M:%S')) + "\n")
        todir = self.save_path_entry.get()
        print("check_loc_hash: todir: " + todir)
        font_dir = todir + r'/prestringtable/font/pearl.ttf'
        if Path(font_dir).is_dir() or Path(font_dir).is_file():
            print("check_font_hash: Found " + font_dir)
            return(check_new.get_hash(font_dir))
        else:
            print("check_font_hash: Can not find " + font_dir)
            return None


    def hh_method(self, num):
        todir = self.save_path_entry.get()
        font_dir = self.check_bdo_dir()

        ads_dir = todir + r'/ads'
        temp_loc_dir = mkdtemp(prefix='loc_temp_')
        temp_font_dir = mkdtemp(prefix='font_temp_')
        temp_bdocn_dir = mkdtemp(prefix='bdocn_temp_')

        tw_loc = 'http://dn.blackdesert.com.tw/UploadData/ads/languagedata_tw.loc'
        github_loc = 'https://github.com/BDO-CnHope/bdocn/raw/master/ads/languagedata_en.loc'
        github_font = 'https://github.com/BDO-CnHope/bdocn/raw/master/prestringtable/font/pearl.ttf'
        gitee_loc = 'https://gitee.com/bdo-cnhope/bdocn/tree/master/split/'
        gitee_font = 'https://gitee.com/bdo-cnhope/bdocn/tree/master/split_font/'
        en_loc = download.download_en_loc()
        
        if num == 1:
            if check_new.get_loc_hash(1) != self.check_loc_hash():
                self.insert_text('正在使用国外线路下载简体汉化语言包…… \n')
                download.download_file(github_loc, ads_dir, 'languagedata_en.loc')
                self.insert_text('简体汉化包已更新! \n')
            else:
                self.insert_text('简体汉化包已是最新的了! \n')   
            if check_new.get_font_hash(1) != self.check_font_hash() and str(self.usefontVar.get()) != '1':
                self.insert_text( '正在下载字体包…… \n')
                download.download_file(github_font, font_dir, 'pearl.ttf')
                self.insert_text('字体包已更新! \n')
            else:
                self.insert_text('字体包已是最新的了! \n')
            showinfo('提示','汉化已完成！')
        elif num == 2:
            self.insert_text('正在下载繁体汉化语言包…… \n')
            download.download_file(tw_loc, ads_dir, 'languagedata_en.loc')
            self.insert_text('繁体汉化包已更新! \n')
            if check_new.get_font_hash(1) != self.check_font_hash() and str(self.usefontVar.get()) != '1':
                self.insert_text('正在下载字体包…… \n')
                download.download_file(github_font, font_dir, 'pearl.ttf')
                self.insert_text('字体包已更新! \n')
            else:
                self.insert_text('字体包已是最新的了! \n')
            showinfo('提示','汉化已完成！')
        elif num == 3:
            if check_new.get_font_hash(1) != self.check_font_hash():
                self.insert_text('正在下载字体包…… \n')
                download.download_file(github_font, font_dir, 'pearl.ttf')
                self.insert_text('字体包已更新! \n')
            else:
                self.insert_text('字体包已是最新的了! \n')
            showinfo('提示','汉化已完成！')
        elif num == 11:
            if check_new.get_loc_hash(2) != self.check_loc_hash():
                self.insert_text('正在使用国内线路下载简体汉化语言包…… \n')
                download.download_split_files(gitee_loc, temp_loc_dir)
                joinfiles.join_files(temp_loc_dir, ads_dir, 'languagedata_en.loc')
                self.insert_text('简体汉化包已更新! \n')
            else:
                self.insert_text('简体汉化包已是最新的了! \n')
            if check_new.get_font_hash(2) != self.check_font_hash() and str(self.usefontVar.get()) != '1':
                self.insert_text('正在下载字体包…… \n')
                download.download_split_files(gitee_font, temp_font_dir)
                joinfiles.join_files(temp_font_dir, font_dir, 'pearl.ttf')
                self.insert_text('字体包已更新! \n')
            else:
                self.insert_text('字体包已是最新的了! \n')
            showinfo('提示','汉化已完成！')
        elif num == 12:
            self.insert_text('正在下载繁体汉化语言包…… \n')
            download.download_file(tw_loc, ads_dir, 'languagedata_en.loc')
            self.insert_text('繁体汉化包已更新! \n')
            if check_new.get_font_hash(2) != self.check_font_hash() and str(self.usefontVar.get()) != '1':
                self.insert_text('正在下载字体包…… \n')
                download.download_split_files(gitee_font, temp_font_dir)
                joinfiles.join_files(temp_font_dir, font_dir, 'pearl.ttf')
                self.insert_text('字体包已更新! \n')
            else:
                self.insert_text('字体包已是最新的了! \n')
            showinfo('提示','汉化已完成！')
        elif num == 13:
            if check_new.get_font_hash(2) != self.check_font_hash():
                self.insert_text('正在下载字体包…… \n')
                download.download_split_files(gitee_font, temp_font_dir)
                joinfiles.join_files, (temp_font_dir, font_dir, 'pearl.ttf')
                self.insert_text('字体包已更新! \n')
            else:
                self.insert_text('字体包已是最新的了! \n')
            showinfo('提示','汉化已完成！')
        elif num == 4:
            self.insert_text('正在重新安装美服英语包…… \n')
            download.download_file(en_loc, temp_bdocn_dir, 'languagedata_en.loc')
            copy(temp_bdocn_dir  + r'/languagedata_en.loc', ads_dir)
            self.insert_text('已恢复为美服英语! \n')
            showinfo('提示','任务已完成！')

    def start_button(self):
        print("[BEGIN] start_button >>> " + str(time_stamp.strftime('%Y.%m.%d-%H:%M:%S')) + "\n")
        a = askyesno('提示', '要执行此操作吗')

        if a == True and self.conf_path_entry.get() != '':
            # 用户自选配置文件路径
            conf_dir = self.check_bdo_conf_path()
            print("start_button: selected a custom BDO conf path")
            if self.check_bdo_conf_path() != False:
                check_launcher.change_bdo_font_conf(conf_dir)
        elif a == True and self.conf_path_entry.get() == '':
            self.check_bdo_conf_empty_path()

        if self.check_bdo_dir() == False or self.check_bdo_conf_empty_path() == False or self.check_bdo_conf_path() == False:
            pass
        elif a == True and str(self.hmVar.get()) == '4':
            self.process_panel_button_1.config(state='disabled')
            self.hh_method(4)
            self.process_panel_button_1.config(state='normal')
        elif a == True and str(self.dmVar.get()) == '1':
            self.process_panel_button_1.config(state='disabled')
            if str(self.hmVar.get()) == '1':
                self.hh_method(1)
            elif str(self.hmVar.get()) == '2':
                self.hh_method(2)
            elif str(self.hmVar.get()) == '3':
                self.hh_method(3)
            self.process_panel_button_1.config(state='normal')
        elif a == True and str(self.dmVar.get()) == '2':
            self.process_panel_button_1.config(state='disabled')
            if str(self.hmVar.get()) == '1':
                self.hh_method(11)
            elif str(self.hmVar.get()) == '2':
                self.hh_method(12)
            elif str(self.hmVar.get()) == '3':
                self.hh_method(13)
            self.process_panel_button_1.config(state='normal')
        else:
            self.process_panel_button_1.config(state='normal')

    def run(self):
            self.mainwindow.mainloop()
