from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(765, 500)
        MainWindow.setWindowIcon(QtGui.QIcon('./static/favicon.ico'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(19, 8, 721, 421))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.img_txt = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.img_txt.setEnabled(True)
        self.img_txt.setStyleSheet("font: 25 12pt \"微软雅黑 Light\";")
        self.img_txt.setObjectName("img_txt")
        self.horizontalLayout.addWidget(self.img_txt)
        self.img_path = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.img_path.setObjectName("img_path")
        self.horizontalLayout.addWidget(self.img_path)
        self.xzbtn1 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.xzbtn1.setObjectName("xzbtn1")
        self.horizontalLayout.addWidget(self.xzbtn1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.csv_txt = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.csv_txt.setStyleSheet("font: 25 12pt \"微软雅黑 Light\";")
        self.csv_txt.setObjectName("csv_txt")
        self.horizontalLayout_2.addWidget(self.csv_txt)
        self.csv_path = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.csv_path.setObjectName("csv_path")
        self.horizontalLayout_2.addWidget(self.csv_path)
        self.xzbtn2 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.xzbtn2.setObjectName("xzbtn")
        self.horizontalLayout_2.addWidget(self.xzbtn2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_4.setStyleSheet("font: 25 12pt \"微软雅黑 Light\";")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.count = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.count.setStyleSheet("font: 25 14pt \"微软雅黑 Light\";\n"
                                       "color: rgb(255, 0, 0);")
        self.count.setText("")
        self.count.setObjectName("count")
        self.horizontalLayout_3.addWidget(self.count)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_6.setStyleSheet("font: 25 12pt \"微软雅黑 Light\";")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.startButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.startButton.setStyleSheet("font: 25 14pt \"微软雅黑 Light\";\n"
"color: rgb(0, 0, 255);")
        self.startButton.setObjectName("startButton")
        self.horizontalLayout_4.addWidget(self.startButton)
        self.resetButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.resetButton.setStyleSheet("font: 25 14pt \"微软雅黑 Light\";\n"
"color: rgb(255, 0, 0);")
        self.resetButton.setObjectName("resetButton")
        self.horizontalLayout_4.addWidget(self.resetButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.wt = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.wt.setStyleSheet("font: 25 13pt \"微软雅黑 Light\";\n"
                              "color: rgb(255, 0, 255);")
        self.wt.setObjectName("wt")
        self.verticalLayout_4.addWidget(self.wt)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.gy3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.gy3.setStyleSheet("font: 25 12pt \"微软雅黑 Light\";")
        self.gy3.setObjectName("gy3")
        self.horizontalLayout_7.addWidget(self.gy3)
        self.count_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.count_2.setStyleSheet("font: 25 12pt \"微软雅黑 Light\";\n"
                                   "color: rgb(255, 0, 0);")
        self.count_2.setObjectName("count_2")
        self.horizontalLayout_7.addWidget(self.count_2)
        self.gy4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.gy4.setStyleSheet("font: 25 12pt \"微软雅黑 Light\";")
        self.gy4.setObjectName("gy4")
        self.horizontalLayout_7.addWidget(self.gy4)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.log = QtWidgets.QTextEdit(self.verticalLayoutWidget_2)
        self.log.setObjectName("log")
        self.log.setMinimumSize(QtCore.QSize(721, 100))
        self.log.setReadOnly(True)
        self.verticalLayout_4.addWidget(self.log)

        self.verticalLayout.addLayout(self.verticalLayout_4)

        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label.setStyleSheet("font: 10pt \"新宋体\";\n"
"text-align: center;")
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setStyleSheet("font: 9pt \"新宋体\";\n"
"text-align: center;")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_5.setStyleSheet("font: 9pt \"新宋体\";\n"
"text-align: center;")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 765, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PPOCR 疫情信息统计小工具"))
        self.img_txt.setText(_translate("MainWindow", "图像文件夹路径："))
        self.xzbtn1.setText(_translate("MainWindow", "选择文件夹"))
        self.csv_txt.setText(_translate("MainWindow", "输出CSV路径设置："))
        self.xzbtn2.setText(_translate("MainWindow", "选择文件夹"))
        self.label_4.setText(_translate("MainWindow", "共有："))
        self.label_6.setText(_translate("MainWindow", "张图片，请耐心等待识别..."))
        self.startButton.setText(_translate("MainWindow", "点击开始识别"))
        self.resetButton.setText(_translate("MainWindow", "重置"))

        self.wt.setText(_translate("MainWindow", "问题人员列表："))
        self.gy3.setText(_translate("MainWindow", "共有："))
        self.count_2.setText(_translate("MainWindow", "0"))
        self.gy4.setText(_translate("MainWindow", "条风险数据，如下："))
        
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">2022  © 版权归iterhui所有</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p>技术支持1：PPOCR提供识别</p><a>链接：https://github.com/PaddlePaddle/PaddleOCR</a></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p>技术支持2：QPT进行打包</p><a>https://github.com/QPT-Family/QPT</a></body></html>"))

