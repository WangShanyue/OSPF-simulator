import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt
from PyQt5 import  QtCore


class Drawing(QWidget):
    P_rect=[]
    def __init__(self,text,rect):
        self.setWindowTitle("在窗体中绘画出文字例子")
        self.resize(500, 600)
        self.text = text
        self.P_rect=rect

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.begin(self)
        # 自定义的绘画方法
        self.drawText(event, painter)
        painter.end()

    def drawText(self, event, qp):
        # 设置笔的颜色
        qp.setPen(QColor(168, 34, 3))
        # 设置字体
        qp.setFont(QFont('SimSun', 10))
        # 画出文本
        qp.drawText(QtCore.QRect(100, 50, 151, 121), Qt.AlignCenter, self.text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Drawing("lalala",QtCore.QRect(100, 50, 151, 121))
    demo.show()
    sys.exit(app.exec_())