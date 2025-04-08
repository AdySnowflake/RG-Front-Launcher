import configparser
import os

def modify_config(file_path, section, key, value):
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
    flag = 1
    file_path = "config.ini"
    section = "Config"
    key = "upscaler"
    path = ["./realesrgan-ncnn-vulkan.exe", "./upscayl-bin.exe", "./realcugan-ncnn-vulkan.exe"]
    value = path[flag]

    modify_config(file_path, section, key, value)
