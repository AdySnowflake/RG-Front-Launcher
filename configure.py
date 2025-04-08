import configparser
import os

flag = 1


def modify_config(file_path, section, key, value, create_if_missing=True):
    config = configparser.ConfigParser()

    # 读取 config.ini 文件
    if os.path.exists(file_path):
        config.read(file_path)
    else:
        print(f"文件不存在: {file_path}")
        return

    # 检查 section 是否存在
    if not config.has_section(section):
        if create_if_missing:
            config.add_section(section)
        else:
            print(f"Section 不存在: {section}")
            return

    # 设置键值
    config.set(section, key, value)

    # 写回文件
    with open(file_path, 'w') as configfile:
        config.write(configfile)
    print(f"已修改 {file_path} 中 [{section}] 的 {key} = {value}")


# 示例调用
if __name__ == "__main__":
    file_path = "config.ini"
    section = "Config"
    key = "upscaler"
    path = ["./realesrgan-ncnn-vulkan.exe", "./upscayl-bin.exe", "./realcugan-ncnn-vulkan.exe"]
    value = path[flag]

    modify_config(file_path, section, key, value)
