import sys
import designer.MainGUI as MainGUI
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets
import ppocrDemo
from PyQt5.QtCore import pyqtSignal, QObject, QBasicTimer
import ctypes
from threading import Thread

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")


class MySignals(QObject):
    # 定义信号
    signal_count = pyqtSignal(str)
    signal_ocr = pyqtSignal(str)
    signal_xz1 = pyqtSignal(str)
    signal_xz2 = pyqtSignal(str)

class Signals(QMainWindow, MainGUI.Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.init_ui()

        # 实例化
        self.ms_signals_count = MySignals()
        self.ms_signals_ocr = MySignals()
        self.ms_signals_xz1 = MySignals()
        self.ms_signals_xz2 = MySignals()

        # 连接信号
        self.ms_signals_count.signal_count.connect(self.update_count)
        self.ms_signals_ocr.signal_ocr.connect(self.update_ocr)
        self.ms_signals_xz1.signal_xz1.connect(self.update_xz1)
        self.ms_signals_xz2.signal_xz2.connect(self.update_xz2)

    def update_count(self, count):
        self.count.setText(str(count))

    def update_ocr(self, status):
        self.startButton.setText(status)

    def update_xz1(self, txt):
        self.img_path.setText(txt.replace('/', '\\'))

    def update_xz2(self, txt):
        self.csv_path.setText(txt.replace('/', '\\'))

    def onclick1(self):
        img_path = self.img_path.text()
        csv_path = self.csv_path.text()

        def run_count():
            _, count = ppocrDemo.manyImages(img_path)
            self.ms_signals_count.signal_count.emit(str(count))

        t1 = Thread(target=run_count)
        t1.start()

        def run_ocr():
            self.ms_signals_ocr.signal_ocr.emit("正在进行识别...")
            ppocrDemo.ocr(img_path, csv_path + '/')
            self.ms_signals_ocr.signal_ocr.emit("识别完成!")

        t2 = Thread(target=run_ocr)
        t2.start()

    def onclick2(self):
        self.img_path.setText("")
        self.csv_path.setText("")
        self.count.setText("0")
        self.startButton.setText("点击开始识别")

    def onclick3(self, filepath):
        m = QtWidgets.QFileDialog.getExistingDirectory(None, "选取文件夹", "F:/")  # 起始路径
        self.ms_signals_xz1.signal_xz1.emit(m)

    def onclick4(self, filepath):
        m = QtWidgets.QFileDialog.getExistingDirectory(None, "选取文件夹", "D:/")  # 起始路径
        self.ms_signals_xz2.signal_xz2.emit(m)

    def init_ui(self):
        MainGUI.Ui_MainWindow.setupUi(self, self)
        self.img_path.setPlaceholderText("请输入图片文件夹全路径（例如：F:\\images）")
        self.img_path.setText("F:\\OcrYq\\images")
        self.csv_path.setPlaceholderText("请输入csv文件夹全路径（例如：D:\\desktop\\csv）")
        self.csv_path.setText("D:\\desktop\\csv")
        self.count.setText("0")

        self.startButton.clicked.connect(self.onclick1)
        self.resetButton.clicked.connect(self.onclick2)
        self.xzbtn1.clicked.connect(self.onclick3)
        self.xzbtn2.clicked.connect(self.onclick4)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Signals()
    window.show()
    sys.exit(app.exec_())
