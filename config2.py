import configparser
import os

flag = 2
file_path = "config.ini"
section = "Config"
key = "upscaler"
path = [
    "./realesrgan-ncnn-vulkan.exe",  # flag = 1 ，预期值
    "./upscayl-bin.exe",             # flag = 2
    "./realcugan-ncnn-vulkan.exe"    # flag = 3
]
# value = path[flag]

def modify_config(flag):
    value = path[flag-1]
    config = configparser.ConfigParser()

    # 读取 config.ini 文件
    if os.path.exists(file_path):
        config.read(file_path)
    else:
        print(f"文件不存在: {file_path}")
        return

    # 设置键值
    config.set(section, key, value)

    # 写回文件
    with open(file_path, 'w') as configfile:
        config.write(configfile)
    print(f"已修改 {file_path} 中 [{section}] 的 {key} = {value}")


if __name__ == "__main__":
    modify_config(flag)
