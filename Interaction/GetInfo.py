from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QThread,pyqtSignal
import socket,time,queue
import  Structs.TableViewStruct


class SubInfoListen(QThread):#和之前的子监听线程一样，都是建立连接之后开一个新的线程传输数据
    conn = []
    Str= ''
    update_data=pyqtSignal(int, str)
    q = queue.Queue(maxsize=100)  # 用来传输最短路径树的队列
    def __init__(self,conn,q,update_data,parent=None):
        super(SubInfoListen,self).__init__(parent)
        self.identity=None
        self.conn=conn
        self.q=q
        self.update_data=update_data
    def run(self):
        while True:
            try:
                self.Str = self.conn.recv(1024)  # 接收数据
                if len(self.Str) != 0:
                    print("received" + self.Str.decode('utf-8'))  # 打印接收到的数据
                    TableNode=self.Str.split()
                    id=TableNode[0][0]-48
                    #self.q.put(self.str)    #把接收到的数据放到队列中，向上一级传
                    self.update_data.emit(id, TableNode[1].decode('utf-8'))
            except ConnectionResetError as e:
                print('关闭了正在占线的链接！')
                break
        self.conn.close()



class ExeInfo(QThread):
    update_data=pyqtSignal(int,str)
    q = queue.Queue(maxsize=100)  # 用来传输最短路径树的队列
    def __init__(self,parent=None):
        super(ExeInfo,self).__init__(parent)
        self.identity=None
    def setVal(self):
        self.start()
    def run(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('localhost', 9090))  # 绑定要监听的端口
        server.listen(5)  # 开始监听 表示可以使用五个链接排队
        while True:  # conn就是客户端链接过来而在服务端为期生成的一个链接实例
            conn, addr = server.accept()  # 等待链接,多个链接的时候就会出现问题,其实返回了两个值
            sub = SubInfoListen(conn,self.q,self.update_data)
            sub.start()
            time.sleep(0.1)  # 停顿一下，确定能收到数据

