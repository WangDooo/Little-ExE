# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Wang\Desktop\计算力学大作业\171030王博臣\Gui\WangBC171030.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1000, 700)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pic/title.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        self.centralWidget = QtWidgets.QWidget(mainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralWidget)
        self.graphicsView.setGeometry(QtCore.QRect(60, 20, 851, 221))
        self.graphicsView.setStyleSheet("border-image: url(:/pic/question.png);")
        self.graphicsView.setObjectName("graphicsView")
        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox.setGeometry(QtCore.QRect(60, 280, 161, 151))
        self.groupBox.setObjectName("groupBox")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 132, 22))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 100, 132, 22))
        self.radioButton_2.setObjectName("radioButton_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_2.setGeometry(QtCore.QRect(240, 280, 191, 151))
        self.groupBox_2.setObjectName("groupBox_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_3.setGeometry(QtCore.QRect(20, 30, 151, 22))
        self.radioButton_3.setChecked(True)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_4.setGeometry(QtCore.QRect(20, 70, 132, 22))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_5.setGeometry(QtCore.QRect(20, 110, 132, 22))
        self.radioButton_5.setObjectName("radioButton_5")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_3.setGeometry(QtCore.QRect(450, 280, 481, 151))
        self.groupBox_3.setObjectName("groupBox_3")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit.setGeometry(QtCore.QRect(10, 70, 113, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setGeometry(QtCore.QRect(10, 30, 471, 31))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton.setGeometry(QtCore.QRect(10, 100, 171, 34))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(130, 70, 301, 18))
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser.setGeometry(QtCore.QRect(60, 460, 651, 211))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(730, 460, 191, 71))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(730, 590, 211, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(730, 630, 241, 18))
        self.label_4.setObjectName("label_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_3.setGeometry(QtCore.QRect(730, 540, 191, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        mainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "计算力学大作业-王博臣171030"))
        self.groupBox.setTitle(_translate("mainWindow", "荷载方式"))
        self.radioButton.setText(_translate("mainWindow", "P=5"))
        self.radioButton_2.setText(_translate("mainWindow", "P=-5 ，q=-1"))
        self.groupBox_2.setTitle(_translate("mainWindow", "单元类型"))
        self.radioButton_3.setText(_translate("mainWindow", "3节点三角形"))
        self.radioButton_4.setText(_translate("mainWindow", "4节点四边形"))
        self.radioButton_5.setText(_translate("mainWindow", "8节点四边形"))
        self.groupBox_3.setTitle(_translate("mainWindow", "单元大小划分"))
        self.label.setText(_translate("mainWindow", "单元数（建议：三角形单元16个左右，四边形单元8个左右）"))
        self.pushButton.setText(_translate("mainWindow", "确定生成节点数据"))
        self.label_2.setText(_translate("mainWindow", "个 ( 请输入大于1的正整数 )"))
        self.pushButton_2.setText(_translate("mainWindow", "计算结果"))
        self.label_3.setText(_translate("mainWindow", "王博臣 171030"))
        self.label_4.setText(_translate("mainWindow", "Email：wangbc1993@163.com"))
        self.pushButton_3.setText(_translate("mainWindow", "清空输出内容"))

import img_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

