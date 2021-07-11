import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter.constants import BOTH, END
from jira import JIRA
import MainApp


win_width = 280
win_height = 120
win_color = '#0c76ff'
win_bg_color = '#549eff'
jira_server = 'http://jira.skyoss.com'

class LoginFrame(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.login_success = tk.BooleanVar
        self.pack(pady=10)
        self.config(bg=win_bg_color)
        self.createWidget()

    def createWidget(self):
        #1.user name
        self.user_name_label = ttk.Label(self,text='User Name')
        self.user_name_label.grid(row=0,column=0,columnspan=2,pady=5,stick='ew')
        #StringVar变量绑定到指定的组件
        #StringVar的值发生变化，则组件内容也发生变化；组件内容发生变化时，则StringVar的值也发生变化
        self.user_name = tk.StringVar()
        self.user_name_entry = ttk.Entry(self,name='user_name_entry',textvariable=self.user_name)
        self.user_name_entry.grid(row=0,column=2,columnspan=4,pady=5,stick='ew')
        #self.user_name.set('Please input jira account')
        #self.user_name_entry.bind('<FocusIn>',lambda self,event: self.user_name_entry.delete(0,END))  #lambda 参数列表 ： 表达式
        #self.user_name_entry.bind('<FocusOut>',lambda : self.user_name_entry.insert(END,'Please input jira account'))

        #2.pass word
        self.pass_word_label = ttk.Label(self,text='Pass Word')
        self.pass_word_label.grid(row=1,column=0,columnspan=2,pady=3,sticky='ew')
        self.pass_word = tk.StringVar()
        self.pass_word_entry = ttk.Entry(self,name='pass_word_entry',textvariable=self.pass_word,show='*')
        self.pass_word_entry.grid(row=1,column=2,columnspan=4,pady=3,sticky='ew')
        #self.pass_word_entry.bind('<FocusIn>',self.pwFocusIn)
        #self.pass_word_entry.bind('<FocusOut>',self.pwFocusOut)

        #3.log in
        self.log_in_button = ttk.Button(self,text='Ok',command=self.login_ckeck)
        self.log_in_button.grid(row=2,column=0,columnspan=3,pady=5,sticky='ew')
        #self.log_in_button.bind('<Button-1>',self.login)

        #4.cancel and eixt
        self.exit_button = ttk.Button(self,text='Cancel',command=self.login_cancel)
        self.exit_button.grid(row=2,column=3,columnspan=3,pady=5,sticky='ew')


    def login_ckeck(self):
        global jira_server
        user_name = self.user_name_entry.get()
        pass_word = self.pass_word_entry.get()
        print('user_name:',user_name,'pass_word:',pass_word)
        '''
        if user_name == '':
            messagebox.showwarning('Warning','User Name should not be None')
            return
        elif pass_word == '':
            messagebox.showwarning('Warning','Pass Word should not be None')
            return
        print('go login')
        '''
        '''
        jira = JIRA(jira_server,auth=(user_name,pass_word))
        print('jira:',jira)
        if jira:
            messagebox.showinfo('Message','Login success!')
            self.login_success = True
            self.destroy()
        else:
            messagebox.showerror('Error','Login fail!')
        '''
        self.login_success = True
        if self.login_success:
            self.login_success = False
            self.destroy()
            self.master.destroy()
            print('Login success,go main win')
            MainApp.createMainWin()

    def login_cancel(self):
        print('login canceled and exit')
        self.destroy()
        self.master.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Jira Login')
    #获取屏幕宽高
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    #窗口居中显示
    root.geometry('%dx%d+%d+%d'%(win_width,win_height, \
            (screen_width - win_width)/2,(screen_height - win_height)/2))
    #设置窗口背景色
    root.config(bg=win_bg_color)

    loginFrame = LoginFrame(master=root)
    #loginFrame.pack()
    
    root.mainloop()


