import os,time
from multiprocessing import Process
import  Socket.Processes


class MainProcess(Process):
    def __init__(self,parent=None):
        Process.__init__(self)
        self.identity=None
    def setVal(self):
        self.start()
    def run(self):
        print("主进程开始>>> pid={}".format(os.getpid()))
        route = [[[(0, 1), 100]], [[(1, 0), 100], [(1, 2), 100]], [[(2, 1), 100], [(2, 3), 100], [(2, 4), 100]],
                 [[(3, 2), 100]], [[(4, 2), 100]]]  # [[目标结点1，距离1]，[目标结点2，距离2]...]
        process_list = []
        for i in range(5):
            process_list.append(Socket.Processes.RoutePrecess(i, 'Router{num}'.format(num=i), route[i]))
        for i in range(5):
            process_list[i].start()

