# @Time    : 2020/12/24
# @Author  : Naunter
# @Page    : https://github.com/Naunters

import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox
from tkinter.filedialog import askdirectory
from tkinter.scrolledtext import ScrolledText
import re
import os
import shutil
import tempfile
import webbrowser
import urllib.request
import joinfiles
import download
import thread_func
import unzip
import check_new

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
        _text_ = '''1. 汉化文本来自于黑沙台服，准确内容请以美服官方为主！
2. 如有问题，请去Github或Gitee提交issue。
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
        self.left_panel_body.place(anchor='nw', height='350', width='290', x='0', y='150')
        self.left_panel_body_text = tk.Text(self.left_panel_body)
        self.left_panel_body_text.config(background='#f2f2f2', font='{Microsoft YaHei} 10 {}', height='10', relief='flat')
        self.left_panel_body_text.config(state='disabled', width='50')
        client_notice = '''1. 运行本汉化工具前，请先退出并关闭游戏！如运行着其它的汉化工具，也请关闭。

2. 请选择正确的“黑沙的游戏目录”

3. 根据需求选择你要汉化的方式

4. 点击运行执行汉化

* 举例Steam的黑沙路径: 
C:\Program Files (x86)\Steam\steamapps\common\Black Desert Online\ 

* Steam端用户如出现问题，请“重新校验游戏文件”后再重新运行一次本汉化工具。'''
        self.left_panel_body_text.configure(state='normal')
        self.left_panel_body_text.insert('0.0', client_notice)
        self.left_panel_body_text.configure(state='disabled')
        self.left_panel_body_text.place(anchor='nw', height='320', width='280', x='0', y='0')
        self.left_panel_bottom = tk.LabelFrame(self.main_window)
        self.left_panel_bottom.config(background='#f2f2f2', font='{Microsoft YaHei} 12 {bold}', height='200', relief='groove')
        self.left_panel_bottom.config(text='来源', width='200')
        self.left_panel_bottom.place(anchor='nw', height='100', width='290', x='0', y='500')
        self.left_panel_bottom_text = tk.Text(self.left_panel_bottom)
        self.left_panel_bottom_text.config(background='#f2f2f2', font='{Microsoft YaHei} 10 {}', height='10', relief='flat')
        self.left_panel_bottom_text.config(state='disabled', width='50')
        _text_ = '''Create by Naunter
Version: 2020122400
Date: 2020/12/24
'''
        self.left_panel_bottom_text.configure(state='normal')
        self.left_panel_bottom_text.insert('0.0', _text_)
        self.left_panel_bottom_text.configure(state='disabled')
        self.left_panel_bottom_text.place(anchor='nw', height='70', width='150', x='0', y='0')
        self.left_panel_bottom_button_1 = tk.Button(self.left_panel_bottom)
        self.left_panel_bottom_button_1.config(text='Github')
        self.left_panel_bottom_button_1.place(anchor='nw', height='26', width='80', x='200', y='0')
        self.left_panel_bottom_button_1.configure(command=lambda:self.hyperlinks(1))
        self.left_panel_bottom_button_2 = tk.Button(self.left_panel_bottom)
        self.left_panel_bottom_button_2.config(text='Gitee')
        self.left_panel_bottom_button_2.place(anchor='nw', height='26', width='80', x='200', y='40')
        self.left_panel_bottom_button_2.configure(command=lambda:self.hyperlinks(2))
        self.save_path = tk.LabelFrame(self.main_window)
        self.save_path.config(background='#f2f2f2', font='{Microsoft YaHei} 12 {bold}', foreground='#0000ff', height='200', relief='groove')
        self.save_path.config(text='1. 文件保存路径', width='200')
        self.save_path.place(anchor='nw', height='60', width='300', x='300', y='0')
        self.save_path_entry = tk.Entry(self.save_path)
        self.save_path_entry.config(font='{Microsoft YaHei} 10 {}')
        self.save_path_entry_text = '''请选择黑沙的游戏根目录...'''
        self.save_path_entry.delete('0', 'end')
        self.save_path_entry.insert('0', self.save_path_entry_text)
        self.save_path_entry.place(anchor='nw', height='20', width='210', x='5', y='3')
        self.save_path_button = tk.Button(self.save_path)
        self.save_path_button.config(font='{Microsoft YaHei} 9 {}', text='打开...')
        self.save_path_button.configure(command=self.select_path)
        self.save_path_button.place(anchor='nw', height='25', width='70', x='220', y='0')
        self.download_method = tk.LabelFrame(self.main_window)
        self.download_method.config(background='#f2f2f2', font='{Microsoft YaHei} 12 {bold}', foreground='#004080', height='200', relief='groove')
        self.download_method.config(text='2. 汉化包下载线路', width='200')
        self.download_method.place(anchor='nw', height='60', width='300', x='300', y='60')
        self.dmVar = tk.StringVar(value="1")
        self.download_method_radiobutton_1 = tk.Radiobutton(self.download_method)
        self.download_method_radiobutton_1.config(font='{Microsoft YaHei} 12 {}', text='海外下载', value="1", variable=self.dmVar)
        self.download_method_radiobutton_1.place(anchor='nw', x='0', y='0')
        self.download_method_radiobutton_2 = tk.Radiobutton(self.download_method)
        self.download_method_radiobutton_2.config(font='{Microsoft YaHei} 12 {}', text='国内下载', value="2", variable=self.dmVar)
        self.download_method_radiobutton_2.place(anchor='nw', x='180', y='0')
        self.hanhua_method = tk.LabelFrame(self.main_window)
        self.hanhua_method.config(background='#f2f2f2', font='{Microsoft YaHei} 12 {bold}', foreground='#008080', height='200', text='3. 汉化方式')
        self.hanhua_method.config(width='200')
        self.hanhua_method.place(anchor='nw', height='220', width='300', x='300', y='120')
        self.hmVar=tk.IntVar()
        self.hmVar.set(1)
        self.hanhua_method_radiobutton_1 = tk.Radiobutton(self.hanhua_method)
        self.hanhua_method_radiobutton_1.config(font='{Microsoft YaHei} 12 {}', text='简体汉化(加强版)', variable=self.hmVar, value='1')
        self.hanhua_method_radiobutton_1.place(anchor='nw', x='0', y='0')
        self.hanhua_method_radiobutton_2 = tk.Radiobutton(self.hanhua_method)
        self.hanhua_method_radiobutton_2.config(font='{Microsoft YaHei} 12 {}', text='繁体汉化', variable=self.hmVar, value='2')
        self.hanhua_method_radiobutton_2.place(anchor='nw', x='0', y='50')
        self.hanhua_method_radiobutton_3 = tk.Radiobutton(self.hanhua_method)
        self.hanhua_method_radiobutton_3.config(font='{Microsoft YaHei} 12 {}', text='不汉化，只安装字体', variable=self.hmVar, value='3')
        self.hanhua_method_radiobutton_3.place(anchor='nw', x='0', y='100')
        self.hanhua_method_radiobutton_4 = tk.Radiobutton(self.hanhua_method)
        self.hanhua_method_radiobutton_4.config(font='{Microsoft YaHei} 12 {}', text='清除汉化，恢复英文', variable=self.hmVar, value='4')
        self.hanhua_method_radiobutton_4.place(anchor='nw', x='0', y='150')
        self.process_panel = tk.LabelFrame(self.main_window)
        self.process_panel.config(font='{Microsoft YaHei} 12 {bold}', foreground='#008000', height='200', text='4. 操作面板', width='200')
        self.process_panel.place(anchor='nw', height='260', width='300', x='300', y='340')
        self.process_panel_button_1 = tk.Button(self.process_panel)
        self.process_panel_button_1.config(font='{Microsoft YaHei} 12 {}',text='开始运行')
        self.process_panel_button_1.configure(command=self.start_button)
        self.process_panel_button_1.place(anchor='nw', height='50', width='285', x='5', y='0')
        self.process_panel_progresstext = ScrolledText(self.process_panel)
        self.process_panel_progresstext.config(font='{Microsoft YaHei} 10 {}', height='10', width='50', relief='groove')
        self.process_panel_progresstext.configure(state='normal')
        self.process_panel_progresstext.insert('0.0', '...\n')
        self.process_panel_progresstext.place(anchor='nw', height='160', width='285', x='5', y='60')
        self.mainwindow = self.main_window

    def hyperlinks(self, var):
        if var == 1 :
            webbrowser.open_new(r"https://github.com/BDO-CnHope/bdocn_client")
        elif var == 2:
            webbrowser.open_new(r"https://gitee.com/bdo-cnhope/bdocn_client")

    def select_path(self):
        open_path = askdirectory()
        self.save_path_entry.delete('0', 'end')
        self.save_path_entry.insert('0', open_path)
        self.process_panel_progresstext.insert(tk.INSERT, '选择了目录: \n'+open_path+'\n')

    def check_bdo_dir(self):
        todir = self.save_path_entry.get()
        ads_dir = todir + '\\ads\\'
        font_dir = todir + '\\prestringtable' + '\\font'
        if todir == '' or todir == self.save_path_entry_text:
            tk.messagebox.showinfo('提示','你没有选择正确的目录! ')
            self.process_panel_progresstext.insert(tk.INSERT, '你没有选择正确的游戏目录! \n')
            return False
        elif os.path.exists(ads_dir) == False:
            tk.messagebox.showinfo('提示','没有找到语言文件目录，请检查游戏完整性!')
            self.process_panel_progresstext.insert(tk.INSERT, '没有找到语言文件目录，请检查游戏完整性! \n')
            return False
        elif os.path.exists(font_dir) == False:
            os.makedirs(font_dir)
            return(font_dir)
        elif os.path.exists(font_dir) == True:
            return(font_dir)

    def check_loc_hash(self):
        todir = self.save_path_entry.get()
        ads_dir = todir + '\\ads\\languagedata_en.loc'
        return(check_new.get_hash(ads_dir))

    def check_font_hash(self):
        todir = self.save_path_entry.get()
        font_dir = todir + '\\prestringtable\\font\\pearl.ttf'
        return(check_new.get_hash(font_dir))

    def hh_method(self, num):
        todir = self.save_path_entry.get()
        font_dir = self.check_bdo_dir()
        tmpdirname = str(tempfile.gettempdir())

        ads_dir = todir + '\\ads'
        temp_loc_dir = tmpdirname + r'\split_loc'
        temp_font_dir = tmpdirname + r'\split_fonts'
        temp_bdocn_dir = tmpdirname + r'\bdocn_temp'

        tw_loc = 'http://dn.blackdesert.com.tw/UploadData/ads/languagedata_tw.loc'
        github_loc = 'https://github.com/BDO-CnHope/bdocn/raw/master/ads/languagedata_en.loc'
        github_font = 'https://github.com/BDO-CnHope/bdocn/raw/master/prestringtable/font/pearl.ttf'
        gitee_loc = 'https://gitee.com/bdo-cnhope/bdocn/tree/master/split/'
        gitee_font = 'https://gitee.com/bdo-cnhope/bdocn/tree/master/split_font/'
        en_loc_zip = download.download_en_loc()
        
        try:
            if os.path.exists(temp_bdocn_dir) == False or os.path.exists(temp_font_dir) == False or os.path.exists(temp_bdocn_dir) == False:
                os.mkdir(temp_loc_dir)
                os.mkdir(temp_font_dir)
                os.mkdir(temp_bdocn_dir)
        except:
            self.process_panel_progresstext.insert(tk.INSERT, '操作错误，请重试... \n')
            pass
        else:
            if num == 1:
                if check_new.get_loc_hash(1) != self.check_loc_hash():
                    self.process_panel_progresstext.insert(tk.INSERT, '正在使用国外线路下载简体汉化语言包…… \n')
                    thread_func.thread_it(download.download_file, (github_loc, ads_dir, 'languagedata_en.loc'))
                    self.process_panel_progresstext.insert(tk.INSERT, '简体汉化包已更新! \n')
                else:
                    self.process_panel_progresstext.insert(tk.INSERT, '简体汉化包已是最新的了! \n')   
                if check_new.get_font_hash(1) != self.check_font_hash():
                    self.process_panel_progresstext.insert(tk.INSERT, '正在下载字体包…… \n')
                    thread_func.thread_it(download.download_file, (github_font, font_dir, 'pearl.ttf'))
                    self.process_panel_progresstext.insert(tk.INSERT, '字体包已更新! \n')
                else:
                    self.process_panel_progresstext.insert(tk.INSERT, '字体包已是最新的了! \n')
            elif num == 2:
                self.process_panel_progresstext.insert(tk.INSERT, '正在下载繁体汉化语言包…… \n')
                thread_func.thread_it(download.download_file, (tw_loc, ads_dir, 'languagedata_en.loc'))
                self.process_panel_progresstext.insert(tk.INSERT, '繁体汉化包已更新! \n')
                if check_new.get_font_hash(1) != self.check_font_hash():
                    self.process_panel_progresstext.insert(tk.INSERT, '正在下载字体包…… \n')
                    thread_func.thread_it(download.download_file, (github_font, font_dir, 'pearl.ttf'))
                    self.process_panel_progresstext.insert(tk.INSERT, '字体包已更新! \n')
                else:
                    self.process_panel_progresstext.insert(tk.INSERT, '字体包已是最新的了! \n')
            elif num == 3:
                if check_new.get_font_hash(1) != self.check_font_hash():
                    self.process_panel_progresstext.insert(tk.INSERT, '正在下载字体包…… \n')
                    thread_func.thread_it(download.download_file, (github_font, font_dir, 'pearl.ttf'))
                    self.process_panel_progresstext.insert(tk.INSERT, '字体包已更新! \n')
                else:
                    self.process_panel_progresstext.insert(tk.INSERT, '字体包已是最新的了! \n')
            elif num == 11:
                if check_new.get_loc_hash(2) != self.check_loc_hash():
                    self.process_panel_progresstext.insert(tk.INSERT, '正在使用国内线路下载简体汉化语言包…… \n')
                    thread_func.thread_it(download.download_split_files, (gitee_loc, temp_loc_dir))
                    thread_func.thread_it(joinfiles.join_files, (temp_loc_dir, ads_dir, 'languagedata_en.loc'))
                    self.process_panel_progresstext.insert(tk.INSERT, '简体汉化包已更新! \n')
                else:
                    self.process_panel_progresstext.insert(tk.INSERT, '简体汉化包已是最新的了! \n')
                if check_new.get_font_hash(2) != self.check_font_hash():
                    self.process_panel_progresstext.insert(tk.INSERT, '正在下载字体包…… \n')
                    thread_func.thread_it(download.download_split_files, (gitee_font, temp_font_dir))
                    thread_func.thread_it(joinfiles.join_files, (temp_font_dir, font_dir, 'pearl.ttf'))
                    self.process_panel_progresstext.insert(tk.INSERT, '字体包已更新! \n')
                else:
                    self.process_panel_progresstext.insert(tk.INSERT, '字体包已是最新的了! \n')
            elif num == 12:
                self.process_panel_progresstext.insert(tk.INSERT, '正在下载繁体汉化语言包…… \n')
                thread_func.thread_it(download.download_file, (tw_loc, ads_dir, 'languagedata_en.loc'))
                self.process_panel_progresstext.insert(tk.INSERT, '繁体汉化包已更新! \n')
                if check_new.get_font_hash(2) != self.check_font_hash():
                    self.process_panel_progresstext.insert(tk.INSERT, '正在下载字体包…… \n')
                    thread_func.thread_it(download.download_split_files, (gitee_font, temp_font_dir))
                    thread_func.thread_it(joinfiles.join_files, (temp_font_dir, font_dir, 'pearl.ttf'))
                    self.process_panel_progresstext.insert(tk.INSERT, '字体包已更新! \n')
                else:
                    self.process_panel_progresstext.insert(tk.INSERT, '字体包已是最新的了! \n')
            elif num == 13:
                if check_new.get_font_hash(2) != self.check_font_hash():
                    self.process_panel_progresstext.insert(tk.INSERT, '正在下载字体包…… \n')
                    thread_func.thread_it(download.download_split_files, (gitee_font, temp_font_dir))
                    thread_func.thread_it(joinfiles.join_files, (temp_font_dir, font_dir, 'pearl.ttf'))
                    self.process_panel_progresstext.insert(tk.INSERT, '字体包已更新! \n')
                else:
                    self.process_panel_progresstext.insert(tk.INSERT, '字体包已是最新的了! \n')
            elif num == 4:
                self.process_panel_progresstext.insert(tk.INSERT, '正在重新安装美服英语包…… \n')
                unzip_dir = temp_bdocn_dir + '\\loc'
                thread_func.thread_it(download.download_file, (en_loc_zip, temp_bdocn_dir, 'BDOLanguage.zip'))
                thread_func.thread_it(unzip.un_zip, (temp_bdocn_dir, 'BDOLanguage.zip', unzip_dir))
                thread_func.thread_it(shutil.copy, (unzip_dir + '\\' + 'languagedata_en.loc', ads_dir))
                self.process_panel_progresstext.insert(tk.INSERT, '已恢复为美服英语! \n')
        os.removedirs(temp_loc_dir)
        os.removedirs(temp_font_dir)
        os.removedirs(temp_bdocn_dir)

    def start_button(self):
        a = tkinter.messagebox.askyesno('提示', '要执行此操作吗')
        if self.check_bdo_dir() == False:
            pass
        elif a == True and str(self.hmVar.get()) == '4':
            self.hh_method(4)
        elif a == True and str(self.dmVar.get()) == '1':
            if str(self.hmVar.get()) == '1':
                self.hh_method(1)
            elif str(self.hmVar.get()) == '2':
                self.hh_method(2)
            elif str(self.hmVar.get()) == '3':
                self.hh_method(3)
        elif a == True and str(self.dmVar.get()) == '2':
            if str(self.hmVar.get()) == '1':
                self.hh_method(11)
            elif str(self.hmVar.get()) == '2':
                self.hh_method(12)
            elif str(self.hmVar.get()) == '3':
                self.hh_method(13)
        else:
            pass

    def run(self):
            self.mainwindow.mainloop()

if __name__ == '__main__':
    import tkinter as tk
    root = tk.Tk()
    root.title('黑色沙漠汉化工具 by Naunter')
    root.resizable(False, False)
    app = Application(root)
    if check_new.get_client_version() != '2020122400':
        a = tkinter.messagebox.askyesno('提示', '有新版本的客户端，是否查看？')
        if a == True:
            app.hyperlinks(2)
            thread_func.thread_it(app.run(), '')
        else:
            thread_func.thread_it(app.run(), '')
    else:
        thread_func.thread_it(app.run(), '')
