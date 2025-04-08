from window_import import *

# 定义变量
executor1 = "Official-NCNN"
executor2 = "Upscayl-NCNN"

def choose_esrgan(root):
    # 创建第二个窗口
    root2 = tk.Toplevel(root)
    root2.title("Real-ESRGAN 模式")
    root2.geometry("400x200")
    root2.configure(bg=bg_color)
    root2.resizable(False, False)

    # 调用取得自定义字体
    title_font, button_font = get_fonts()

    # 添加标题框架
    title_frame = tk.Frame(root2, bg=bg_color)
    title_frame.pack(pady=15)

    # 创建说明标签
    label = tk.Label(title_frame, text="请选择 Real-ESRGAN 执行器：",
                     font=title_font, bg=bg_color, fg=title_color, pady=15)
    label.pack()

    # 创建按钮框架
    button_frame = tk.Frame(root2, bg=bg_color)
    button_frame.pack(pady=20)

    def button1_clicked():
        messagebox.showinfo("提示", f"你选择了 Real-ESRGAN 模型\n{executor1} 执行器")
        # print("Hello World")
        root2.destroy()
        root.iconify()  # 最小化主窗口

    def button2_clicked():
        messagebox.showinfo("提示", f"你选择了 Real-ESRGAN 模型\n{executor2} 执行器")
        print("Hello World")
        root2.destroy()
        root.iconify()  # 最小化主窗口

    # 创建两个按钮，使用变量作为按钮文本
    button1 = add_button(button_frame, executor1, button1_clicked, button_font)
    button2 = add_button(button_frame, executor2, button2_clicked, button_font)

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

