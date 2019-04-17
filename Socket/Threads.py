from threading import Thread
import time,random
import socket
delay=1#延迟时间

class ServerThread(Thread):
    ip=''
    port=0
    def __init__(self, ip, port):
        Thread.__init__(self)
        self.ip=ip
        self.port=port

    def run(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.ip, self.port))  # 绑定要监听的端口
        server.listen(5)  # 开始监听 表示可以使用五个链接排队
        while True:  # conn就是客户端链接过来而在服务端为期生成的一个链接实例
            conn, addr = server.accept()  # 等待链接,多个链接的时候就会出现问题,其实返回了两个值
            print("****",conn,"****",addr)
            while True:
                try:
                    data = conn.recv(1024)  # 接收数据
                    if len(data) !=0 :
                        print('recive:', data.decode())  # 打印接收到的数据
                        secdr= "id= {} receive from {}".format(self.port-7890,data[3]-48)
                        conn.send(str(secdr).encode('utf-8'))  # 然后再发送数据
                except ConnectionResetError as e:
                    print('关闭了正在占线的链接！')
                    break
            conn.close()

# class ClintThread(Thread):
#     ip = ''
#     port = 0
#
#     def __init__(self, ip, port):
#         Thread.__init__(self)
#         self.ip = ip
#         self.port = port
#
#     def run(self):
#         client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 声明socket类型，同时生成链接对象
#         client.connect((self.ip, self.port))  # 建立一个链接，连接到本地的6969端口
#
#         # addr = client.accept()
#         # print '连接地址：', addr
#         msg = self.port-7890  # strip默认取出字符串的头尾空格
#         client.send(str(msg).encode('utf-8'))  # 发送一条信息 python3 只接收btye流
#         data = client.recv(1024)  # 接收一个信息，并指定接收的大小 为1024字节
#         print('recv:', data.decode())  # 输出我接收的信息
#         client.close()  # 关闭这个链接

if __name__ == '__main__':
    t=ServerThread('localhost',7890)
    t.start()
   # c = ClintThread('localhost',7890)
    #c.start()
    print('主')
