from threading import Thread
import time,random
import socket
import queue
delay=1#延迟时间
BASE_PORT=7999
q = queue.Queue(maxsize=100)

class subSendThread(Thread):
    conn = []
    id=0
    str=''
    def __init__(self,conn,id,q):
        super(subSendThread, self).__init__()
        Thread.__init__(self)
        self.conn=conn
        self.id=id
        self.q=q

    def run(self):

        while True:
            try:
                self.str = self.conn.recv(1024)  # 接收数据
                self.q.put(self.str)
                if len(self.str) != 0:
                    print('{0}recive:'.format(self.id),self.str.decode())  # 打印接收到的数据
            except ConnectionResetError as e:
                print('关闭了正在占线的链接！')
                break
        self.conn.close()

class ListenThread(Thread):
    ip=''
    port=0
    q = queue.Queue(maxsize=100)
    linklist = []
    def __init__(self, ip, port,linklist):
        super(ListenThread,self).__init__()
        self.ip=ip
        self.port=port
        self.linklist=linklist

    def run(self):

        global BASE_PORT
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(self.port)
        server.bind((self.ip, self.port))  # 绑定要监听的端口
        server.listen(5)  # 开始监听 表示可以使用五个链接排队
        while True:  # conn就是客户端链接过来而在服务端为期生成的一个链接实例
            conn, addr = server.accept()  # 等待链接,多个链接的时候就会出现问题,其实返回了两个值
            #print("****",conn,"****",addr)
            sub= subSendThread(conn,self.port-BASE_PORT,q)
            str=''
            if(not q.empty() ):
                str = q.get()
                print("The received str is",str.decode())
            sub.start()



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

        for i in range(4):
            if(i==id):
                continue
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 声明socket类型，同时生成链接对象
            print('{}send to {}'.format(id,BASE_PORT+i))
            client.connect((self.ip, BASE_PORT+i))  # 建立一个链接，连接到本地的6969端口
            msg = self.link  # strip默认取出字符串的头尾空格
            client.send(str(msg).encode('utf-8'))  # 发送一条信息 python3 只接收btye流

        # addr = client.accept()
        # print '连接地址：', addr





if __name__ == '__main__':
    t=ListenThread('localhost', 7890)
    t.start()
   # c = ClintThread('localhost',7890)
    #c.start()
    print('主')
