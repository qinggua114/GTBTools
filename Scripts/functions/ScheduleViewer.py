import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPainter, QPen
import datetime

nowtime = datetime.datetime
weekday = int(nowtime.weekday(nowtime.now()))
weekdays = {0:"星期一" , 1:"星期二" , 2:"星期三" , 3:"星期四" , 4:"星期五" , 5:"星期六" , 6:"星期日"}
schedules = [
    ["", "", "", "", "", "", "", "", "", "", "", ""], 
    ["", "", "", "", "", "", "", "", "", "", "", ""], 
    ["", "", "", "", "", "", "", "", "", "", "", ""], 
    ["", "", "", "", "", "", "", "", "", "", "", ""], 
    ["", "", "", "", "", "", "", "", "", "", "", ""], 
    ["", "", "", "", "", "", "", "", "", "", "", ""], 
    ["", "", "", "", "", "", "", "", "", "", "", ""]
    ]

filepath = '..\data\schedule_data\schedule.txt'
current_dir = os.path.dirname(os.path.abspath(__file__))
absolute_path = os.path.join(current_dir, filepath)
normalized_path = os.path.normpath(absolute_path)
i=0;j=0
try:
    with open(normalized_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.replace('\n', '')
            if line == "NextDay":
                i += 1;j = 0
                continue
            schedules[i][j] = line
            j += 1
except Exception as err:
    print("Something went wrong when reading schedule.txt: ",err)
    print("Using preset schedule to continue.")
print(schedules)

lines = []

class TransparentWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # 设置窗口无边框和透明
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        # 设置窗口大小
        screen = QApplication.primaryScreen()
        scrSize = screen.geometry()
        scrWid = scrSize.width()
        scrHei = scrSize.height()
        widw_width = int(scrWid/16)
        widw_height = int(scrHei*0.75)
        a = int(widw_height/20)
        self.setGeometry(0, 0,scrWid, scrHei)
        
        # 创建中央部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignRight | Qt.AlignTop)
        central_widget.setLayout(layout)

        # 创建布局和标签
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignRight)
        self.label.setStyleSheet("""
            QLabel {
                background-color: rgba(255, 255, 255, 0);"""+f"""
                font-size: {a}px;"""+
            '}'
        )
        self.label.setGeometry(0, 0, widw_width, widw_height)

        #显示星期
        self.weekdayView = QLabel(weekdays[weekday], self)
        self.weekdayView.setStyleSheet("""
            QLabel {
                color: rgba(0, 0, 0, 1);
                background-color: rgba(255, 255, 255, 0.2);
                """+f"""
                font-size: {a}px;"""+
            '}'
        )
        layout.addWidget(self.weekdayView)

        #创建课程列表
        for i,text in enumerate(schedules[weekday],1):
            if text == "":
                continue
            self.line = QLabel(text, self)
            self.line.setObjectName(f"line_{i}")
            
            self.line.setStyleSheet("""
                QLabel {
                    color: rgba(30, 50, 90, 1);
                    border: 4px double yellow;
                    background-color: rgba(240, 245, 255, 0.8);
                    """+f"""
                    font-size: {a}px;"""+
            '}'
            )
            self.line.setMargin(5)
            layout.addWidget(self.line)
            lines.append(self.line)
        
        
        # 添加锁定按钮
        self.lock_btn = QLabel("L", self)
        self.lock_btn.setStyleSheet("""
            QLabel {
                background-color: rgba(255, 255, 255, 0.1);
                color: rgba(50, 50, 50, 1);
                font-size: 16px;
                padding: 4px;
            }
            QLabel:hover {
                background-color: white;
            }
        """)
        self.lock_btn.setGeometry(scrWid-60, 0, 30, 30)
        self.lock_btn.setAlignment(Qt.AlignCenter)
        self.lock_btn.mousePressEvent = lambda e: self.shiftLockstatu()

        # 添加关闭按钮
        self.close_btn = QLabel("×", self)
        self.close_btn.setStyleSheet("""
            QLabel {
                background-color: rgba(200, 50, 50, 10);
                color: white;
                font-size: 20px;
                border-radius: 0px;
                padding: 2px 8px;
            }
            QLabel:hover {
                background-color: rgba(255, 0, 0, 220);
            }
        """)
        self.close_btn.setAlignment(Qt.AlignCenter)
        self.close_btn.setGeometry(scrWid-30, 0, 30, 30)
        self.close_btn.mousePressEvent = lambda e: self.close()

        #创建指示器
        self.point = QLabel()
        self.point.setAlignment(Qt.AlignRight)
        
        # 用于窗口拖动的变量
        self.oldPos = None

    lockStatu:bool = 0
    lockStatuView = {1 : 'U' , 0 : 'L'}
    def shiftLockstatu(self):
        self.lockStatu = self.lockStatu == 0
        self.lock_btn.setText(self.lockStatuView[self.lockStatu])
        return
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        if self.lockStatu:
            if self.oldPos:
                delta = event.globalPos() - self.oldPos
                self.move(self.x() + delta.x(), self.y() + delta.y())
                self.oldPos = event.globalPos()

    def mouseReleaseEvent(self, event):
        self.oldPos = None
    
    def changeText(self,text):
        self.label.setText(text)

def SVStart():
    app = QApplication(sys.argv)
    window = TransparentWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    SVStart()