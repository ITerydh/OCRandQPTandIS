# 导入QPT
from qpt.executor import CreateExecutableModule as CEM
from qpt.modules.python_env import Python38

def main():
    module = CEM(work_dir="F:/OcrYq",
                 launcher_py_path="F:/OcrYq/run.py",
                 save_path="./out",
                 requirements_file="auto",
                 hidden_terminal=False,
                 interpreter_module=Python38(),
                 icon="F:/OcrYq/static/favicon.ico")
    # 开始打包
    module.make()


if __name__ == "__main__":
    main()
