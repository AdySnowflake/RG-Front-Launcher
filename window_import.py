import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkfont

# 定义颜色
bg_color = "#ffffff"  # 背景色
title_color = "#000000"  # 标题颜色
button_bg = "#000000"  # 按钮背景色
button_fg = "white"  # 按钮文字颜色
button_active_bg = "#2980b9"  # 按钮激活时的背景色

# 创建自定义字体
def get_fonts():
    title_font = tkfont.Font(family="HarmonyOS Sans SC", size=14)
    button_font = tkfont.Font(family="Montserrat Medium", size=10)
    return title_font, button_font

# 创建按钮
def create_button(parent, text, command, font):
    return tk.Button(
        parent,
        text=text,
        command=command,
        width=12,
        font=font,
        bg=button_bg,
        fg=button_fg,
        activebackground=button_active_bg,
        relief=tk.FLAT,
        borderwidth=2,
        cursor="hand2"
    )

# 创建按钮并添加到父容器
def add_button(parent, text, command, font):
    btn = create_button(parent, text, command,font)
    btn.pack(side=tk.LEFT, padx=20)
    return btn

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

