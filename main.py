from switcher import launch_window
from configure import modify_config
from starter import ExeController


def main():
    print("hello world")
    launch_window(choice)


def choice(flag):
    print(f"flag: {flag}")
    modify_config(flag)
    control_exe()


def control_exe():
    global first
    controller = ExeController()
    if first:
        controller.stop()
    controller.start()

    print(f"first: {first}")
    first += 1


if __name__ == "__main__":
    first = 0  # 记录是否第一次运行
    main()
