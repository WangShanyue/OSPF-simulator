from View.SubWindow import *
from View.MainView import *
from Structs.RouteTables import *
INF= 214748364

class MySubWindow(QWidget,Ui_Dialog_Sub):#子窗口的类,通过传参数的方法传入最短路径的表格，在里边计算最短路径树和路由表
    Routes=RouteTables()
    model_StapTable = QStandardItemModel(0, 0)
    model_RouteTable = QStandardItemModel(0, 2)
    def __init__(self,parent=None):
        super(MySubWindow,self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon('../images/SubWindowIcon.png'))
        self.model_RouteTable.setHorizontalHeaderLabels(['目的结点','后继结点'])
        self.tableView_3.setModel(self.model_RouteTable)





    def SetTable(self,table):#根据传进来的结果设置新窗口
        self.__Init()
        self.Routes=table
        self.setWindowTitle("{0}号路由器的详细信息".format(self.Routes.id))
        self.model_StapTable.clear()

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
                else:
                    self.model_StapTable.setItem(i, j,None)

        self.tableView_0.setModel(self.model_StapTable)


        RouteList=list(self.Routes.RouteTable)
        RouteList_2=list(self.Routes.RouteTable.values())
        print(RouteList)
        for i in range(len(RouteList)):
            self.model_RouteTable.setItem(i, 0, QStandardItem(str(RouteList[i])))
            self.model_RouteTable.setItem(i, 1,QStandardItem(str(RouteList_2[i])))


        self.tableView_3.setModel(self.model_RouteTable)
        print(self.Routes.DjTree)
        self.__ShowTree(self.Routes.DjTree,self.Routes.id)




    def __ShowTree(self,DjTree,id):#显示最短路径树
        for i in range(len(DjTree)):
            for j in range(len(DjTree[i])):
                self.__ShowLine(self.LineTree[i][DjTree[i][j]])
                self.__ShowRoute(self.RoutesTree[DjTree[i][j]],self.labelTable[DjTree[i][j]])
        self.RoutesTree[id].setStyleSheet("QPushButton{border-image:url(../images/CurrentRouter.png);}")
        self.RoutesTree[id].show()
        self.labelTable[id].show()

    def __ShowLine(self,Line):
        for i in range(len(Line)):
            Line[i].show()

    def __ShowRoute(self,route,lable):
        route.show()
        lable.show()



    def __Init(self):#所有的线和路由器全部消失
        for i in range(len(self.RoutesTree)):
            self.RoutesTree[i].setStyleSheet("QPushButton{border-image:url(../images/router.png);}")
            self.RoutesTree[i].hide()
            self.labelTable[i].hide()
        self.line_01.hide()
        self.line_12.hide()
        self.line_13_2.hide()
        self.line_13_1.hide()
        self.line_23_1.hide()
        self.line_23_2.hide()
        self.line_24.hide()


















