
'''
界面传输信息用的
'''
from threading import *
INFO_PORT=9863
import socket

class SendRouteInfo(Thread):
    def __init__(self, RouteTable):
        Thread.__init__(self)
        self.RouteTable = RouteTable

    def run(self):
        ViewClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ViewClient.connect(('localhost',INFO_PORT))
        ViewClient.send('RouteTables({0},{1},{2},{3})'.format(self.RouteTable.id,self.RouteTable.StepTable,self.RouteTable.DjTree,self.RouteTable.RouteTable).encode('utf-8'))
