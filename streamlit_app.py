# -*- coding: utf-8 -*-
import subprocess

def main():
    try:
        # 运行 start.sh 脚本
        subprocess.run(["/entrypoint/entrypoint.sh", "-b"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"启动 start.sh 脚本时出错：{e}")

if __name__ == "__main__":
    main()
