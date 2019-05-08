from View.SubWindow import *
from View.MainView import *
from Structs.RouteTables import *
INF= 214748364

class MySubWindow(QWidget,Ui_Dialog_Sub):#子窗口的类,通过传参数的方法传入最短路径的表格，在里边计算最短路径树和路由表
    Routes=RouteTables()
    model_StapTable = QStandardItemModel(0, 0)
    model_RouteTable = QStandardItemModel(0, 2)
    def __init__(self,RouteTable=None,parent=None):
        super(MySubWindow,self).__init__(parent)
        self.setupUi(self)

        self.model_RouteTable.setHorizontalHeaderLabels(['后继结点','目的结点'])
        self.tableView_3.setModel(self.model_RouteTable)





    def SetTable(self,table):
        self.Routes=table

        List_Step_Head=[]
        for i in range(len(self.Routes.StepTable[0])):
            List_Step_Head.append('路由器{0}'.format(i))

        self.model_StapTable.setHorizontalHeaderLabels(List_Step_Head)
        self.tableView_0.setModel(self.model_StapTable)

        for i in range(len(self.Routes.StepTable)):
            for j in range(len(self.Routes.StepTable[0])):
                if(self.Routes.StepTable[i][j][2]==False):
                    temp= lambda: '∞' if self.Routes.StepTable[i][j][1] >= INF else self.Routes.StepTable[i][j][1]# lambda表达式，表示一个函数，是不是很高级哈哈哈
                    if (i<len(self.Routes.StepTable)-1 and self.Routes.StepTable[i+1][j][2] == True):
                       pass
                       # self. self.model_StapTable.setItem(i, j,QStandardItem( "邻接点:{0},距离={1}".format(self.Routes.StepTable[i][j][0],temp())).setForeground(QBrush(QColor(255,0,0))))
                    else:
                        self.model_StapTable.setItem(i, j,QTableWidgetItem( "邻接点:{0},距离={1}".format(self.Routes.StepTable[i][j][0],temp())).setForeground(QBrush(QColor(0,0,0,0))))
                    print("daozhelil")
        self.tableView_0.setModel(self.model_StapTable)

        # for i in range(len(self.Routes.RouteTable)):
        #     if i == self.Routes.id : continue
        #     for j in range(2):
        #         self.model_RouteTable.setItem(i, j, self.Routes.RouteTable[i][j])
