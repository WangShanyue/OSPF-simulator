# -*- coding:utf-8 -*-

import os, time
from multiprocessing import Process
import os
import socket
import Socket.Threads

delay = 1
class MyProcess(Process):
    linklist=[]#链路状态表
    link=[]#自身链路状态
    id=0#
    name=''

    def __init__(self,id,name,link):
        Process.__init__(self)
        self.link=link
        self.id=id
        self.name=name


    def run(self):
        global delay
        for i in range(len(self.link)):
            #print("123123123",self.link[i][0][1])
            self.linklist.append([self.link[i][0][1], self.link[i][1]])  # 获得链路状态表

        s=Socket.Threads.ListenThread('localhost', Socket.Threads.BASE_PORT + self.id,self.linklist)#服务端接收数据
        s.start()
        while True:
            time.sleep(1)
            c=Socket.Threads.SendThread('localhost',Socket.Threads.BASE_PORT+self.id,self.link)
            c.start()




'''
    def test(self):#测试用的函数
        for i in range(len(self.link)):
           self.linklist.append([(self.id, self.link[i][0]), self.link[i][1]])  # 获得链路状态表

        for i in range(4):
            print("id={0},name={1},link={2},linklist={3}".format(self.id,self.name,self.link,self.linklist))
            time.sleep(0.5)
'''



def main():
    print("主进程开始>>> pid={}".format(os.getpid()))
    route=[[[(0,1),100]],[[(1,0),100],[(1,2),100]],[[(2,1),100],[(2,3),100],[(2,4),100]],[[(3,2),100]],[[(4,2),100]]]#[[目标结点1，距离1]，[目标结点2，距离2]...]
    process_list=[]
    for i in range(4):
        process_list.append(MyProcess(i,'Router{num}'.format(num=i),route[i]))
    for i in range(4):
        process_list[i].start()



    print("主进程终止")


if __name__ == '__main__':
    main()
