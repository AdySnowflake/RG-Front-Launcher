from sw2 import launch_window

from config2 import modify_config

from starter import ExeController

# launch_window()
# flag = 0


def main():
    print("hello world")
    launch_window(choice)


def choice(flag):
    print("hello world")
    print(flag)
    modify_config(flag)
    # controller.stop()
    control_exe()

def control_exe():
    controller = ExeController()
    if (1):
        controller.stop()
    controller.start()
    # time.sleep(5)



if __name__ == "__main__":
    main()
