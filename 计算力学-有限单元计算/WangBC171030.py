# coding: utf-8
# 计算力学编程作业
# 王博臣 171030
###################

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

from Ui_WangBC171030 import Ui_mainWindow

from PreProcess import *
from AfterProcess import *
from Triangle import *
from Quadrangle_4 import *
from Quadrangle_8 import *




class MainWindow(QMainWindow, Ui_mainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
    
    # @pyqtSlot()
    # def on_radioButton_clicked(self):
    #     """
    #     Slot documentation goes here.
    #     """
    #     load_style = 'P' # P=-5 集中力
    
    # @pyqtSlot()
    # def on_radioButton_2_clicked(self):
    #     """
    #     Slot documentation goes here.
    #     """
    #     load_style = 'q' # q=-1 均布力
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # 判断输入值是否合法 
        num_try = self.lineEdit.text()
        if num_try.isdigit() == False or int(num_try)<=1:
            my_button = QMessageBox.critical(self, '错误', '请输入大于1的正整数')
            return
        # 主程序
        num = int(self.lineEdit.text())
        self.textBrowser.append('生成节点数据:')
        # 3节点三角形
        if self.radioButton_3.isChecked():    
            num_node = str(get_num_node_33(num))
            self.textBrowser.append('节点总数为:'+ num_node+'个')
            node_info = str(get_Node_33(num)+1) # 不能append numpy.ndarray数据 转化为str 之前为了循环-1了 为了显示加回来
            csys_info = str(get_Global_csys_33(num))
            self.textBrowser.append('节点编号数据:')
            self.textBrowser.append(node_info) 
            self.textBrowser.append('整体坐标:')
            self.textBrowser.append(csys_info)
            self.textBrowser.append('---------------------------------------------')

        # 4节点四边形
        elif self.radioButton_4.isChecked():  
            num_node = str(get_num_node_44(num))
            self.textBrowser.append('节点总数为:'+ num_node +'个')
            node_info = str(get_Node_44(num)+1) # 不能append numpy.ndarray数据 转化为str 之前为了循环-1了 为了显示加回来
            csys_info = str(get_Global_csys_44(num))
            self.textBrowser.append('节点编号数据:')
            self.textBrowser.append(node_info) 
            self.textBrowser.append('整体坐标:')
            self.textBrowser.append(csys_info)
            self.textBrowser.append('---------------------------------------------')
        # 8节点四边形 
        else:                                  
            num_node = str(get_num_node_84(num))
            self.textBrowser.append('节点总数为:'+ num_node +'个')
            node_info = str(get_Node_84(num)+1) # 不能append numpy.ndarray数据 转化为str 之前为了循环-1了 为了显示加回来
            csys_info = str(get_Global_csys_84(num))
            self.textBrowser.append('节点编号数据:')
            self.textBrowser.append(node_info) 
            self.textBrowser.append('整体坐标:')
            self.textBrowser.append(csys_info)
            self.textBrowser.append('---------------------------------------------')
            
    
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        # 判断输入值是否合法
        num_try = self.lineEdit.text()
        if num_try.isdigit() == False or int(num_try)<=1:
            my_button = QMessageBox.critical(self, '错误', '请输入大于1的正整数')
            return
        # 主程序
        num = int(self.lineEdit.text())
        if self.radioButton_3.isChecked():    # 3节点三角形
            K = get_K(num)
            if self.radioButton.isChecked():
                F = get_F_P(num)
            else:
                F = get_F_Pq(num)
            # 计算位移结果u 并画图
            u = get_u(K, F)
            draw_33(num,u)
        elif self.radioButton_4.isChecked():  # 4节点四边形
            K = get_K_44(num)
            if self.radioButton.isChecked():
                F = get_F_P_44(num)
            else:
                F = get_F_Pq_44(num) 
            u = get_u(K, F)
            draw_44(num,u)
        else:                                 # 8节点四边形  
            K = get_K_84(num)
            if self.radioButton.isChecked():
                F = get_F_P_84(num)
            else:
                F = get_F_Pq_84(num)
            u = get_u(K, F)
            draw_84(num,u)
        
        self.textBrowser.append('各节点位移值u:')  
        self.textBrowser.append(str(u))
        self.textBrowser.append('---------------------------------------------')
        self.textBrowser.append('右端节点y方向的节点位移:')
        self.textBrowser.append(str(u[-1]))
        self.textBrowser.append('---------------------------------------------')


    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        """
        Slot documentation goes here.
        """
        # 清空输出框内容
        self.textBrowser.clear()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
