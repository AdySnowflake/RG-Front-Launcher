from window_import import *



# 定义变量
name1 = "Official-ESRGAN"#executor
name2 = "Upscayl"

def choose_esrgan(
    root,
    title_font,
    button_font,
    bg_color="#ffffff",
    title_color="#000000",
    button_bg="#000000",
    button_fg="white",
    button_active_bg="#2980b9"
):
    # 创建第二个窗口
    root2 = tk.Toplevel(root)
    root2.title("Real-ESRGAN 模式")
    root2.geometry("400x200")


    root2.configure(bg=bg_color)
    root2.resizable(False, False)

    # 添加标题框架
    title_frame = tk.Frame(root2, bg=bg_color)
    title_frame.pack(pady=15)

    # 创建说明标签
    label = tk.Label(title_frame, text="请选择 Real-ESRGAN 的运行模式：",
                     font=title_font, bg=bg_color, fg=title_color, pady=15)
    label.pack()

    # 创建按钮框架
    button_frame = tk.Frame(root2, bg=bg_color)
    button_frame.pack(pady=20)

    def button1_clicked():
        # messagebox.showinfo("提示", f"你选择了 {button_a_text}")
        root2.destroy()
        # root.deiconify()  # 重新显示主窗口

    def button2_clicked():
        # messagebox.showinfo("提示", f"你选择了 {button_b_text}")
        root2.destroy()
        # root.deiconify()  # 重新显示主窗口

    # 创建两个按钮
    button1 = tk.Button(button_frame, text=name1, command=button1_clicked,
                         width=12, font=button_font, bg=button_bg, fg=button_fg,
                         activebackground=button_active_bg, relief=tk.FLAT,
                         borderwidth=2, cursor="hand2")
    button1.pack(side=tk.LEFT, padx=20)

    button2 = tk.Button(button_frame, text=name2, command=button2_clicked,
                         width=12, font=button_font, bg=button_bg, fg=button_fg,
                         activebackground=button_active_bg, relief=tk.FLAT,
                         borderwidth=2, cursor="hand2")
    button2.pack(side=tk.LEFT, padx=20)

    # 添加底部提示信息
    footer = tk.Label(root2, text="选择后将返回主窗口", font=("Microsoft YaHei", 8),
                      bg=bg_color, fg="#7f8c8d")
    footer.pack(pady=10)

    # 居中显示窗口
    # root.eval('tk::PlaceWindow . center')
    toplevel_with_tcl(root, root2)
    center_window(root)

    # 设置窗口为模态，阻止与其他窗口交互
    root2.transient(root)
    root2.grab_set()

    # 当窗口关闭时恢复主窗口
    # root2.protocol("WM_DELETE_WINDOW", lambda: [root2.destroy(), root.deiconify()])
