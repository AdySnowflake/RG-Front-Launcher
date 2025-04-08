from sw2 import launch_window

from config2 import modify_config

# launch_window()
# flag = 0


def main():
    print("hello world")
    launch_window(choice)


def choice(flag):
    print("hello world")
    print(flag)
    modify_config(flag)


if __name__ == "__main__":
    main()
