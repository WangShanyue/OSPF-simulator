import sys
from View.MainView import *
from Interaction import ControlProcess
from PyQt5.QtWidgets import QApplication

import Interaction.GetInfo
class myMainWindow(QMainWindow,Ui_Dialog):
    ModelList=[]
    count=[0,0,0,0,0]
    def __init__ (self, parent=None):
        super(myMainWindow,self).__init__(parent)
        self.setupUi(self)
        for i in range(5):
            model=QStandardItemModel(0,0)
            model.setHorizontalHeaderLabels(['路由器{0}的消息窗口'.format(i)])
            self.ModelList.append(model)
            self.TableList[i].setModel(model)
        self.thread = Interaction.GetInfo.ExeInfo()
        self.thread.update_data.connect(self.printText)
        self.thread.setVal()
    def printText(self,id,text):
        self.ModelList[id].setItem(self.count[id],0,QStandardItem(text))
        self.TableList[id].setModel(self.ModelList[id])
        self.count[id] = self.count[id] + 1  # 列数加一









if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = myMainWindow()
    window.show()
    pro=ControlProcess.MainProcess()
    pro.start()
    sys.exit(app.exec_())




