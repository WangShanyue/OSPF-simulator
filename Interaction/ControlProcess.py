import os,time
from multiprocessing import Process
import  Socket.SubProcesses
import  Socket.Socket_Threads
import Interaction.SendInfo

class MainProcess(Process):
    route=[]
    process_list=[]
    def __init__(self,route,parent=None):
        Process.__init__(self)
        self.identity=None
        self.Route=route
    def setVal(self):
        self.start()
    def run(self):
        print("主进程开始>>> pid={}".format(os.getpid()))
        route = [[[(0, 1), self.Route[0]]], [[(1, 0), self.Route[0]], [(1, 2), self.Route[1]],[(1,3),self.Route[3]]], [[(2, 1), self.Route[1]], [(2, 3), self.Route[2]], [(2, 4), self.Route[4]]],
                 [[(3, 2), self.Route[2]],[(3,1),self.Route[3]]], [[(4, 2), self.Route[4]]]]  # [[目标结点1，距离1]，[目标结点2，距离2]...]
        for i in range(5):
            self.process_list.append(Socket.SubProcesses.RoutePrecess(i, 'Router{num}'.format(num=i), route[i]))
        for i in range(5):
            self.process_list[i].start()
        print("长度为",len(self.process_list))
    def SetRoute(self,route,isStart):
        self.Route=route
        route = [[[(0, 1), self.Route[0]]], [[(1, 0), self.Route[0]], [(1, 2), self.Route[1]], [(1, 3), self.Route[3]]],
                 [[(2, 1), self.Route[1]], [(2, 3), self.Route[2]], [(2, 4), self.Route[4]]],
                 [[(3, 2), self.Route[2]], [(3, 1), self.Route[3]]], [[(4, 2), self.Route[4]]]]
        if not isStart:
            for i in range(5):
                c = Socket.Socket_Threads.SendThread('localhost', Socket.Socket_Threads.BASE_PORT + i,route[i])  # 发送数据
                c.start()


        # for i in range(5):
        #     self.process_list[i].close()
        # self.process_list.clear()
        # for i in range(5):
        #     self.process_list.append(Socket.SubProcesses.RoutePrecess(i, 'Router{num}'.format(num=i), route[i]))
        # for i in range(5):
        #     self.process_list[i].start()