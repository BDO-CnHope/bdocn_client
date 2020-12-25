# https://www.zhihu.com/question/36316470/answer/1466099906
from tkinter import Toplevel, Frame, Label
from time import sleep

class ConvertNotice(Toplevel):
    def __init__(self, file_name):
        super().__init__()
        self.title("提示")
        self.geometry("400x60+700+400")
        self.file_name = file_name

        # 弹窗界面
        self.row1 = Frame(self)
        self.row1.pack(fill="x")
        Label(self.row1, text="正在将 {}.doc 转换为PDF中，请稍等！".format(self.file_name), font=('微软雅黑', 9), width=50).pack()

    def success(self):
        Label(self.row1, text="{}.doc 转换成功！".format(self.file_name), font=('微软雅黑', 9), width=50).pack()
        sleep(2)

    def close(self):
        self.destroy()