from tkinter import messagebox
from window_import import *
from esrgan_switcher import choose_esrgan

# 定义变量
model1 = "Real-ESRGAN"
model2 = "Real-CUGAN"


def check_notice():
    messagebox.showwarning("RG Front Launcher", "未找到 Real-ESRGAN GUI 主程序！")
    sys.exit(0)


def launch_window(on_choice_callback):
    def button1_clicked():
        choose_esrgan(root, on_choice_callback)

    def button2_clicked():
        messagebox.showinfo("提示", f"你选择了 {model2} 模型")
        on_choice_callback(3)
        root.iconify()  # 最小化窗口

    # 创建主窗口
    root = tk.Tk()
    root.title("超分模型选择")
    root.geometry("400x200")  # 窗口大小
    root.configure(bg=bg_color)
    root.resizable(False, False)  # 固定窗口大小

    # 调用取得自定义字体
    title_font, button_font = get_fonts()

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

    button1 = add_button(button_frame, model1, button1_clicked, button_font)
    button2 = add_button(button_frame, model2, button2_clicked, button_font)

    # 添加底部提示信息
    footer = tk.Label(root, text="选择后将自动应用并最小化", font=("Microsoft YaHei", 8),
                      bg=bg_color, fg="#7f8c8d")
    footer.pack(pady=10)

    # 居中显示窗口
    root.eval('tk::PlaceWindow . center')

    # 运行主循环
    root.mainloop()


if __name__ == "__main__":
    launch_window()
