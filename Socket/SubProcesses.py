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
    def __init__(self,id,name,link):
        Process.__init__(self)
        self.link=link
        self.id=id
        self.name=name
      #  self.window=window

    def run(self):
        node_num=Socket.Socket_Threads.node_num
        self.linklist = [[Algorithm.Dijkstra.INF for col in range(node_num)] for row in range(node_num)]
     #   print("init link list",self.linklist)
        s=Socket.Socket_Threads.ListenThread('localhost', Socket.Socket_Threads.BASE_PORT + self.id, self.q)#服务端接收数据
        s.start()
        while True:
            for i in range(len(self.link)):
                self.linklist[self.id][self.link[i][0][1]] = self.link[i][1]
            c=Socket.Socket_Threads.SendThread('localhost', Socket.Socket_Threads.BASE_PORT + self.id, self.link)#发送数据
            c.start()
            time.sleep(2)#等待接收完毕之后进行dj算法
            if(not  self.q.empty()):#接收数据
                self.linklist = self.q.get()#获得队列中的数据
                road,Table,Route=Algorithm.Dijkstra.dijkstra(self.linklist, self.id)#进行dj算法
                print(road)
                RouteTable=RouteTables.RouteTables(self.id, Table,road , Route)
                ViewSendThread=Socket.Socket_Threads.SendRouteInfo(RouteTable)
                ViewSendThread.start()
            time.sleep(Socket.Socket_Threads.delay-2)#下次发送的延时

    def SetLink(self,link):
        self.link=link


'''
    def test(self):#测试用的函数
        for i in range(len(self.link)):
           self.linklist.append([(self.id, self.link[i][0]), self.link[i][1]])  # 获得链路状态表

        for i in range(4):
            print("id={0},name={1},link={2},linklist={3}".format(self.id,self.name,self.link,self.linklist))
            time.sleep(0.5)
'''

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
