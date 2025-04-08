import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkfont

# 窗口居中
def center_window(win):
    win.update_idletasks()
    w = win.winfo_width()
    h = win.winfo_height()
    ws = win.winfo_screenwidth()
    hs = win.winfo_screenheight()
    x = (ws // 2) - (w // 2)
    y = (hs // 2) - (h // 2)
    win.geometry(f'{w}x{h}+{x}+{y}')

# Tcl显示窗口
def toplevel_with_tcl(parent: tk.Tk, win: tk.Toplevel):
    try:
        win.update_idletasks()
        name = str(win)
        parent.eval(f'tk::PlaceWindow {name} center')
    except Exception as e:
        print("显示失败：", e)

