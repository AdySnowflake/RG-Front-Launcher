import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkfont

from esrgan_switcher import choose_esrgan

# 定义模型变量
model1_name = "Real-ESRGAN"
model2_name = "Real-CUGAN"

# 定义颜色
bg_color = "#ffffff"  # 背景色
title_color = "#000000"  # 标题颜色
button_bg = "#000000"  # 按钮背景色
button_fg = "white"  # 按钮文字颜色
button_active_bg = "#2980b9"  # 按钮激活时的背景色

# def button1_clicked():
#     messagebox.showinfo("提示", f"你选择了 {model1_name} 模型")
#     # root.destroy()  # 关闭窗口并结束程序

def button1_clicked():
    print("Hello World")  # 模拟写入配置
    choose_esrgan(
        root=root,
        title_font=title_font,
        button_font=button_font,
        bg_color=bg_color,
        title_color=title_color,
        button_bg=button_bg,
        button_fg=button_fg,
        button_active_bg=button_active_bg
    )
    # root.iconify()
    root.iconify()        # 最小化窗口

def button2_clicked():
    messagebox.showinfo("提示", f"你选择了 {model2_name} 模型")
    # root.destroy()  # 关闭窗口并结束程序

# 创建主窗口
root = tk.Tk()
root.title("超分模型选择")
root.geometry("400x200")  # 窗口大小
root.configure(bg=bg_color)
root.resizable(False, False)  # 固定窗口大小

# 创建自定义字体
title_font = tkfont.Font(family="HarmonyOS Sans SC", size=14, weight="normal")
button_font = tkfont.Font(family="Montserrat Medium", size=10, weight="normal")

# 添加标题框架
title_frame = tk.Frame(root, bg=bg_color)
title_frame.pack(pady=15)

# 创建说明标签
label = tk.Label(title_frame, text="请选择要使用的超分辨率模型：",
                font=title_font, bg=bg_color, fg=title_color, pady=15)
label.pack()

# 创建按钮框架
button_frame = tk.Frame(root, bg=bg_color)
button_frame.pack(pady=20)

# 创建两个按钮，使用变量作为按钮文本
button1 = tk.Button(button_frame, text=model1_name, command=button1_clicked,
                   width=12, font=button_font, bg=button_bg, fg=button_fg,
                   activebackground=button_active_bg, relief=tk.FLAT,
                   borderwidth=2, cursor="hand2")
button1.pack(side=tk.LEFT, padx=20)

button2 = tk.Button(button_frame, text=model2_name, command=button2_clicked,
                   width=12, font=button_font, bg=button_bg, fg=button_fg,
                   activebackground=button_active_bg, relief=tk.FLAT,
                   borderwidth=2, cursor="hand2")
button2.pack(side=tk.LEFT, padx=20)

# 添加底部提示信息
footer = tk.Label(root, text="选择后将自动应用并最小化", font=("Microsoft YaHei", 8),
                 bg=bg_color, fg="#7f8c8d")
footer.pack(pady=10)

# 居中显示窗口
root.eval('tk::PlaceWindow . center')

# 运行主循环
root.mainloop()


