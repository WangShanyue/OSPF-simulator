import sys
import  copy
from View.MainView import *
from Interaction import ControlProcess
from PyQt5.QtWidgets import QApplication
from functools import partial
from Structs.RouteTables import *
import Interaction.GetInfo
from View.CallSubWindow import *


class MyMainWindow(QMainWindow, Ui_Dialog):
    ModelList=[]
    Table_Count=[0, 0, 0, 0, 0]#主窗口中每一个表的
    RouteTableMap={}
    DistanceList=[]
    DelayTime=0
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
        for i in range(5):#每个路由器加一个监听信号，同时增加气泡与小手
            self.ButtonList[i].clicked.connect(partial(self.OpenSubWind,i))
            self.ButtonList[i].setCursor(QCursor(Qt.PointingHandCursor))
            self.ButtonList[i].setToolTip('点击查看详细信息')
        self.SendButton.clicked.connect(self.StartProject)#绑定开始发送按钮
        self.ModifyDistanceButton.clicked.connect(partial(self.GetDistance,True))#绑定修改距离按钮
        self.ModifyDistanceButton.setEnabled(False)

        self.GetDistance()
        self.StartProcess = ControlProcess.MainProcess(self.DistanceList)#开始进程
        self.child=MySubWindow()

    def ManageMessage(self, Str):#根据传进来的比特流来进行解码，之后根据不同的类型来判断转到不同的函数
        obj=eval(eval(Str))
        if(type(obj)==type([])):#根据不同的类型跳转到不同的函数,如果是列表就代表是路由器交互信息
            self.PrintText(obj[0],obj[1])
            self.ModifyDistanceButton.setEnabled(False)
        elif(type(obj)==type(RouteTables())):#如果是路由器各个表的对象，就代表已经运算完成dj算法，信息已经传到这里来了
            self.RouteTableMap[obj.id]=obj
            self.PrintText(obj.id, "运算完成")
            self.ModifyDistanceButton.setEnabled(True)


    def PrintText(self,id,text):#输出每一个路由器的交互信息
        self.ModelList[id].setItem(self.Table_Count[id], 0, QStandardItem(text))
        self.TableList[id].setModel(self.ModelList[id])
        self.Table_Count[id] = self.Table_Count[id] + 1  # 信息记录表的列数加一



    def OpenSubWind(self,id):# 打开子窗口并设置其信息            ——点击每一个路由器
        if(len(self.RouteTableMap)>=4):
            self.child.SetTable(self.RouteTableMap[id])
            self.child.show()

    def StartProject(self):# 开始项目                ——开始按钮
        self.GetDistance()
        self.SetDelayTime()
        self.StartProcess.SetRoute(self.DistanceList,True)
        self.ModifyDistanceButton.show()
        self.SendButton.setEnabled(False)
        self.spinBox.setEnabled(False)
        self.StartProcess.setVal(self.DelayTime)


    def GetDistance(self,Change=False):#参数Change代表是不是发生了改变，改变就传给每个进程

        Distance=[]
        INF=214748364
        for i in range(len(self.EditList)):
            temp=self.EditList[i].text()
            if temp == 'inf' or temp == 'INF':#空的情况之后再考虑
                temp=INF
            # if temp == None:
            #     print("duihao",self.DistanceList[i])
            #     self.EditList[i].setText(str(self.DistanceList[i]))
            #     temp=self.DistanceList[i]
            else:
                temp=int(temp)
            print(temp)
            Distance.append(temp)
            self.DistanceList=copy.deepcopy(Distance)
        print(Distance)
        if Change :
            self.StartProcess.SetRoute(self.DistanceList,False)

    def SetDelayTime(self):
        Delay=self.spinBox.value()
        self.DelayTime=Delay

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
   # sub=MySubWindow()
   # sub.show()

    sys.exit(app.exec_())




