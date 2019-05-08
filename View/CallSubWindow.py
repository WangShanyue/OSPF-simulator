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

        self.model_RouteTable.setHorizontalHeaderLabels(['目的结点','后继结点'])
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
                    self.model_StapTable.setItem(i, j,QStandardItem( "邻接点:{0},距离={1}".format(self.Routes.StepTable[i][j][0],temp())))

        self.tableView_0.setModel(self.model_StapTable)

        print(self.Routes.RouteTable)
        j=0
        for i in range(len(self.Routes.RouteTable)+1):
            if i == self.Routes.id :
                j=1
                continue
            self.model_RouteTable.setItem(i-j, 0, QStandardItem(str(i)))
            self.model_RouteTable.setItem(i-j, 1,QStandardItem(str(self.Routes.RouteTable[i])))


        self.tableView_3.setModel(self.model_RouteTable)

