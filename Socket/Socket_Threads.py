from threading import *
import time,random
import socket
import queue
from Interaction.GetInfo import  VIEW_PORT
import Structs.TableViewStruct
BASE_PORT=6565
node_num=5
delay = 10
# class SubSendThread(Thread):
#     def __init__(self,conn,id,q,qs):
#         super(SubSendThread, self).__init__()
#         Thread.__init__(self)
#         self.conn=conn
#         self.id=id
#     def run(self):

class SubListenThread(Thread):
    conn = []
    id=0
    str=''
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    q = queue.Queue(maxsize=1)  # 用来存放Linklist
    def __init__(self,conn,id,q,server):
        super(SubListenThread, self).__init__()
        Thread.__init__(self)
        self.conn=conn
        self.id=id
        self.q=q
        self.server=server
    def run(self):
        while True:
            try:
                self.str = self.conn.recv(1024)  # 接收数据

                if len(self.str) != 0:
                    self.q.put(self.str)    #把接收到的数据放到队列中，向上一级传
                    num=self.str[3]-48
                    self.server.send('[{1},\'收到来自路由器{0}的消息\']'.format(str(num),self.id).encode('utf-8'))
                    time.sleep(1)
                    break#发出去之后就结束自己的线程，节省资源

            except ConnectionResetError as e:
                print('关闭了正在占线的链接！')
                break
        self.conn.close()

class ListenThread(Thread):
    ip=''
    port=0
    linklist = []
    q = queue.Queue(maxsize=1)#用来传输到上一层链路消息
    list_queue=queue.Queue(maxsize=100)#用来获取下一层的链路信息
    def __init__(self, ip, port,linklist,q):
        super(ListenThread,self).__init__()
        self.ip=ip
        self.port=port
        self.linklist=linklist
        self.list_queue=q

    def run(self):

        global BASE_PORT
        subserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        subserver.connect(('localhost', VIEW_PORT))

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #print(self.port)
        server.bind((self.ip, self.port))  # 绑定要监听的端口
        server.listen(5)  # 开始监听 表示可以使用五个链接排队
        while True:  # conn就是客户端链接过来而在服务端为期生成的一个链接实例
            conn, addr = server.accept()  # 等待链接,多个链接的时候就会出现问题,其实返回了两个值
            #print("****",conn,"****",addr)
            sub= SubListenThread(conn, self.port - BASE_PORT, self.q,subserver)
            sub.start()
            time.sleep(0.2)#停顿一下，确定能收到数据
            str=''
            if(not self.q.empty()):
                str = self.q.get()#取出子进程的数
                str1=str[1:len(str)-1].decode()#去掉括号
                list_rec=list(eval(str1))#获得list
                for i in range (len(list_rec)):#循环遍历得到linklist数组，从而得到整个图
                    if (type(list_rec[1]) == int):#有种情况是只有一个列表，那样的话获得的list会有问题，所以就用type判断的方法，找到这种情况
                        self.linklist[list_rec[0][0]][list_rec[0][1]] = list_rec[1]
                        break
                    else:
                        self.linklist[list_rec[i][0][0]][list_rec[i][0][1]]=list_rec[i][1]
                if (not self.list_queue.empty()):
                    self.list_queue.get()
                self.list_queue.put(self.linklist)  # 传给上一层







class SendThread(Thread):
    ip = ''
    port = 0
    link=[]
    def __init__(self, ip, port,link):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.link=link
    def run(self):
        global BASE_PORT
        dest=[]
        id=self.port-BASE_PORT
        ViewClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        for i in range(5):
            if(i==id):
                continue
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 声明socket类型，同时生成链接对象
            #print('{}send to {}'.format(id,BASE_PORT+i))
            client.connect((self.ip, BASE_PORT+i))  # 建立一个链接，连接到本地的6969端口
            msg = self.link
            client.send(str(msg).encode('utf-8'))  # 发送一条信息 python3 只接收btye流
            time.sleep(0.1)
            client.close()
        ViewClient.connect(('localhost',VIEW_PORT))
        ViewClient.send('[{0},\'链路状态发送完毕\']'.format(str(self.port-BASE_PORT)).encode('utf-8'))
        # addr = client.accept()
        # print '连接地址：', addr


class SendRouteInfo(Thread):
    def __init__(self, RouteTable):
        Thread.__init__(self)
        self.RouteTable = RouteTable

    def run(self):
        ViewClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ViewClient.connect(('localhost',VIEW_PORT))
        ViewClient.send('RouteTables({0},{1},{2},{3})'.format(self.RouteTable.id,self.RouteTable.StepTable,self.RouteTable.DjTree,self.RouteTable.RouteTable).encode('utf-8'))


if __name__ == '__main__':
   # t=ListenThread('localhost', 7890)
   # t.start()
   # c = ClintThread('localhost',7890)
    #c.start()
    print('主')