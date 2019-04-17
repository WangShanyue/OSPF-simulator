# -*- coding:utf-8 -*-

import os, time
from multiprocessing import Process
import os
import socket
import Socket.Threads
BASE_PORT=7890
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
            self.linklist.append([(self.id, self.link[i][0]), self.link[i][1]])  # 获得链路状态表

        s=Socket.Threads.ServerThread('localhost',7890+self.id)#服务端接收数据
        s.start()


        list = []
        #time.sleep(10)
        for i in range(len(self.link)):
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 声明socket类型，同时生成链接对象
            client.connect(('localhost', BASE_PORT + self.link[i][0]))  # 建立一个链接，连接到本地的6969端口
            list.append(client)
        # addr = client.accept()
        # print '连接地址：', addr
        while True:
            for i in range(len(self.link)):

                msg = str(self.linklist)  # strip默认取出字符串的头尾空格
                list[i].send(str(msg).encode('utf-8'))  # 发送一条信息 python3 只接收btye流
                data = list[i].recv(1024)  # 接收一个信息，并指定接收的大小 为1024字节
                print( data.decode())  # 输出我接收的信息
            time.sleep(10)





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
    route=[[[1,100]],[[0,100],[2,100]],[[2,100],[3,100],[4,100]],[[2,100]],[[2,100]]]#[[目标结点1，距离1]，[目标结点2，距离2]...]
    process_list=[]
    for i in range(4):
        process_list.append(MyProcess(i,'Router{num}'.format(num=i),route[i]))
    for i in range(4):
        process_list[i].start()



    print("主进程终止")


if __name__ == '__main__':
    main()
