import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from view.mainView import *
import  Socket.communicate

import os

class myMainWindow(QMainWindow,Ui_Dialog):
    def __init__ (self, parent=None):
        super(myMainWindow,self).__init__(parent)
        self.setupUi(self)





if __name__ == "__main__":



    app = QApplication(sys.argv)
    window = myMainWindow()
    window.show()

    print("主进程开始>>> pid={}".format(os.getpid()))
    route = [[[(0, 1), 100]], [[(1, 0), 100], [(1, 2), 100]], [[(2, 1), 100], [(2, 3), 100], [(2, 4), 100]],
             [[(3, 2), 100]], [[(4, 2), 100]]]  # [[目标结点1，距离1]，[目标结点2，距离2]...]
    process_list = []
    for i in range(5):
        process_list.append(Socket.communicate.MyProcess(i, 'Router{num}'.format(num=i), route[i]))
    for i in range(5):
        process_list[i].start()

    print("主进程终止")


    sys.exit(app.exec_())



