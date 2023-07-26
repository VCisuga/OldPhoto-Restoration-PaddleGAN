import sys
import Repair
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *
 
class picture(QWidget):
    def __init__(self):
        super(picture, self).__init__()
 
        self.resize(1000, 600)
        self.setWindowTitle("显示图像")
 
        self.label = QLabel(self)
        self.label.setText("显示图像")
        self.label.setFixedSize(250, 400) # 设置大小
        self.label.move(230, 150) # 设置位置
 
        self.label.setStyleSheet("QLabel{background:white;}"
                                 "QLabel{color:rgb(300,300,300,120);font-size:10px;font-weight:bold;font-family:宋体;}"
                                 )
        
        self.setWindowTitle("显示图像")
 
        self.label2 = QLabel(self)
        self.label2.setText("显示图像")
        self.label2.setFixedSize(250, 400)
        self.label2.move(530, 150)
 
        self.label2.setStyleSheet("QLabel{background:white;}"
                                 "QLabel{color:rgb(300,300,300,120);font-size:10px;font-weight:bold;font-family:宋体;}"
                                 )
 
        btn = QPushButton(self)
        btn.setText("打开图片")
        btn.move(10, 30)
        btn.clicked.connect(self.openimage)
 
    def openimage(self):
        imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;*.png;;All Files(*)")
        jpg = QtGui.QPixmap(imgName).scaled(self.label.width(), self.label.height())
        self.label.setPixmap(jpg)
        Repair.Reimg(imgName)
        jpg = QtGui.QPixmap('./Repair1.jpg').scaled(self.label2.width(), self.label.height())
        self.label2.setPixmap(jpg)

 
 
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    my = picture()
    my.show()
    sys.exit(app.exec_())