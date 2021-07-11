import tkinter as tk
from tkinter import ttk
import LoginApp 


main_width = 600
main_height =400

class MainFrame(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.config(bg=LoginApp.win_bg_color)
        self.createWidget()
    def createWidget(self):
        self.label = ttk.Label(self,text='mainframe')
        self.label.pack()


def createMainWin():
    root = tk.Tk()
    root.title('Issues Statistic Tool')
    #获取屏幕大小
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    #窗口居中显示
    root.geometry('%dx%d+%d+%d'%(main_width,main_height, \
            (screen_width - main_width)/2,(screen_height - main_height)/2))
    #设置窗口背景色
    root.config(bg=LoginApp.win_bg_color)

    mainFrame = MainFrame(master=root)

    root.mainloop()        



