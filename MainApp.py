import tkinter as tk
from tkinter import ttk

def main():
    print('Start')
    root = tk.Tk()
    root.title('Title')
    root.geometry('600x400')
    lb = tk.Label(root,text='hello') 
    lb.pack()
    root.mainloop()
    


if __name__ == '__main__':
    main()
