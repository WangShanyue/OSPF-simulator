import sys
import View
from View.MainView import *
from View.SubWindow import *
from Interaction import ControlProcess
from PyQt5.QtWidgets import QApplication

import Interaction.GetInfo
class MySubWindow(QWidget,Ui_Dialog_Sub):#子窗口的类,通过传参数的方法传入最短路径的表格，在里边计算最短路径树和路由表
    DjTable=[]
    def __init__(self,parent=None):
        super(MySubWindow,self).__init__(parent)
        self.setupUi(self)

    def SetTable(self,table):
        self.DjTable=table

class MyMainWindow(QMainWindow, Ui_Dialog):
    ModelList=[]
    Table_Count=[0, 0, 0, 0, 0]#主窗口中每一个表的
    def __init__ (self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        for i in range(5):#绑定好每个消息窗口
            model=QStandardItemModel(0,0)
            model.setHorizontalHeaderLabels(['路由器{0}的消息窗口'.format(i)])
            self.ModelList.append(model)
            self.TableList[i].setModel(model)
        self.Thread_RInteract = Interaction.GetInfo.ExeInfo()#绑定好线程，用来传路由器之间的交互信息
        self.Thread_RInteract.update_data.connect(self.PrintText)
        self.Thread_RInteract.setVal()
        QToolTip.setFont(QFont('SansSerif',10))
        for i in range(5):
            self.ButtonList[i].clicked.connect(self.OpenSubWind)
            self.ButtonList[i].setCursor(QCursor(Qt.PointingHandCursor))
            self.ButtonList[i].setToolTip('点击查看详细信息')
        self.child=MySubWindow()

    def PrintText(self,id,text):
        self.ModelList[id].setItem(self.Table_Count[id], 0, QStandardItem(text))
        self.TableList[id].setModel(self.ModelList[id])
        self.Table_Count[id] = self.Table_Count[id] + 1  # 信息记录表的列数加一

    def OpenSubWind(self):
        self.child.show()





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
   # sub=MySubWindow()
   # sub.show()
    pro=ControlProcess.MainProcess()
    pro.start()
    sys.exit(app.exec_())




