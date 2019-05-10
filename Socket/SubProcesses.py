import time
from multiprocessing import Process
import os
import Socket.Socket_Threads
import queue
from Structs import RouteTables
import Algorithm.Dijkstra
class RoutePrecess(Process):#一个进程代表一个路由器
    linklist=[]#链路状态表
    link=[]#自身链路状态
    id=0#
    name=''
    window=object()
    q = queue.Queue(maxsize=100)  # 用来存放Linklist
    DelayTime=0
    def __init__(self,id,name,link,delay):
        Process.__init__(self)
        self.link=link
        self.id=id
        self.name=name
        self.DelayTime=delay
      #  self.window=window

    def run(self):
        node_num=Socket.Socket_Threads.node_num
        self.linklist = [[Algorithm.Dijkstra.INF for col in range(node_num)] for row in range(node_num)]
        for i in range(len(self.link)):
            self.linklist[self.id][self.link[i][0][1]] = self.link[i][1]
     #   print("init link list",self.linklist)
        s=Socket.Socket_Threads.ListenThread('localhost', Socket.Socket_Threads.BASE_PORT + self.id, self.linklist, self.q)#服务端接收数据
        s.start()
        while True:
            c=Socket.Socket_Threads.SendThread('localhost', Socket.Socket_Threads.BASE_PORT + self.id, self.link)#发送数据
            c.start()
            time.sleep(2)#等待接收完毕之后进行dj算法
            for i in range(self.DelayTime-2):# 下次发送的延时,如果把等待和接受结合到一起，可以实现一改变就发送
                if(not  self.q.empty()):#接收数据
                    self.linklist = self.q.get()#获得队列中的数据
                    road,Table,Route=Algorithm.Dijkstra.dijkstra(self.linklist, self.id)#进行dj算法
                    RouteTable=RouteTables.RouteTables(self.id, Table,road , Route)#把数据发送到界面
                    ViewSendThread=Socket.Socket_Threads.SendRouteInfo(RouteTable)
                    ViewSendThread.start()
                   # print(self.linklist)
                    for i in range(len(self.link)):#更新自己的连接信息
                        self.link[i][1]=self.linklist[self.id][self.link[i][0][1]]
                   # print("We Can get", self.link)
                time.sleep(1)


    def SetLink(self,link):
        print("id=", self.id, "link=", link)
        self.link=link


def main():
    qs = queue.Queue(maxsize=100)  # 用来存放Linklist
    qr = queue.Queue(maxsize=100)  # 用来存放Linklist
    print("主进程开始>>> pid={}".format(os.getpid()))
    route=[[[(0,1),100]],[[(1,0),100],[(1,2),100]],[[(2,1),100],[(2,3),100],[(2,4),100]],[[(3,2),100]],[[(4,2),100]]]#[[目标结点1，距离1]，[目标结点2，距离2]...]
    process_list=[]
    for i in range(5):
        process_list.append(RoutePrecess(i, 'Router{num}'.format(num=i), route[i]))
    for i in range(5):
        process_list[i].start()
    print("主进程终止")


if __name__ == '__main__':
    main()
