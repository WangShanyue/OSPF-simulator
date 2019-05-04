import sys
import View
from View.MainView import *
from View.SubWindow import *
from Interaction import ControlProcess
from PyQt5.QtWidgets import QApplication
from functools import partial
from Structs.RouteTables import *
import Interaction.GetInfo
class MySubWindow(QWidget,Ui_Dialog_Sub):#子窗口的类,通过传参数的方法传入最短路径的表格，在里边计算最短路径树和路由表
    Routes=RouteTables()
    def __init__(self,RouteTable=None,parent=None):
        super(MySubWindow,self).__init__(parent)
        self.setupUi(self)
        self.model_RouteTable=QStandardItemModel(0,2)
        self.model_RouteTable.setHorizontalHeaderLabels(['下一跳','目的结点'])
        self.tableView_3.setModel(self.model_RouteTable)
        self.model_StapTable=QStandardItemModel(0,0)
        self.model_StapTable.setHorizontalHeaderLabels(['相邻结点', '距离','是否完成'])
        self.tableView_0.setModel(self.model_StapTable)
    def SetTable(self,table):
        self.Routes=table
        print(self.Routes.id,"  ",str(self.Routes.StepTable[0][0][0]))

        for i in range(len(self.Routes.StepTable)):
            for j in range(len(self.Routes.StepTable[0])):
                if(self.Routes.StepTable[i][j][2]==False):
                    self.model_StapTable.setItem(i, j, "邻接点:{0},距离={1}".format(self.Routes.StepTable[i][j][0],self.Routes.StepTable[i][j][1]))
        self.tableView_0.setModel(self.model_StapTable)

        # for i in range(len(self.Routes.RouteTable)):
        #     if i == self.Routes.id : continue
        #     for j in range(2):
        #         self.model_RouteTable.setItem(i, j, self.Routes.RouteTable[i][j])



class MyMainWindow(QMainWindow, Ui_Dialog):
    ModelList=[]
    Table_Count=[0, 0, 0, 0, 0]#主窗口中每一个表的
    RouteTableMap={}
    def __init__ (self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        for i in range(5):#绑定好每个消息窗口
            model=QStandardItemModel(0,0)
            model.setHorizontalHeaderLabels(['路由器{0}的消息窗口'.format(i)])
            self.ModelList.append(model)
            self.TableList[i].setModel(model)
            self.TableList[i].setShowGrid(False)

        self.Thread_RInteract = Interaction.GetInfo.ExeInfo()#绑定好线程，用来传路由器之间的交互信息
        self.Thread_RInteract.update_data.connect(self.ManageMessage)
        self.Thread_RInteract.setVal()

        QToolTip.setFont(QFont('SansSerif',10))
        for i in range(5):#气泡与小手
            self.ButtonList[i].clicked.connect(partial(self.OpenSubWind,i))
            self.ButtonList[i].setCursor(QCursor(Qt.PointingHandCursor))
            self.ButtonList[i].setToolTip('点击查看详细信息')

        self.child=MySubWindow()

    def PrintText(self,id,text):
        self.ModelList[id].setItem(self.Table_Count[id], 0, QStandardItem(text))
        self.TableList[id].setModel(self.ModelList[id])
        self.Table_Count[id] = self.Table_Count[id] + 1  # 信息记录表的列数加一

    def ManageMessage(self,str):#
        obj=eval(eval(str))
        print(type(obj))

        if(type(obj)==type([])):#根据不同的类型跳转到不同的函数,如果是列表就代表是路由器交互信息
            self.PrintText(obj[0],obj[1])
        elif(type(obj)==type(RouteTables())):#如果是路由器各个表的对象，就代表已经运算完成dj算法，信息已经传到这里来了
            self.RouteTableMap[obj.id]=obj
            self.PrintText(obj.id, "运算完成")


    def OpenSubWind(self,id):
        if(len(self.RouteTableMap)>=4):
            self.child.SetTable(self.RouteTableMap[id])
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




