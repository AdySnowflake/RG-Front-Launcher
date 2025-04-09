import subprocess
import time
import psutil
import os


class ExeController:
    def __init__(self):
        self.exe_path = exe_path
        self.process = None
        self.exe_name = os.path.basename(exe_path)

    def start(self):
        if self.process is None or self.process.poll() is not None:
            self.process = subprocess.Popen(self.exe_path)
            print("程序已启动。")
        else:
            print("程序已经在运行中。")

    def stop(self):
        found = False
        for proc in psutil.process_iter(['pid', 'name', 'exe']):
            try:
                if proc.info['name'] == self.exe_name or (proc.info['exe'] and self.exe_name in proc.info['exe']):
                    proc.kill()
                    print(f"已杀死进程：{proc.pid}")
                    found = True
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue

        if not found:
            print("未找到目标进程，可能已退出。")


if __name__ == "__main__":
    exe_path = r"E:\Downloads\IDM\realesrgan-gui-windows-bundled-v0.2.5.0\realesrgan-gui.exe"
    controller = ExeController()
    controller.start()
    time.sleep(5)
    controller.stop()
