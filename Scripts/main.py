import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPainter, QPen

schedule = ["语文","数学","English","Physics","化学","生物"]
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

        #创建课程列表
        for i,text in enumerate(schedule,1):
            self.line = QLabel(text, self)
            self.line.setObjectName(f"line_{i}")
            
            self.line.setStyleSheet("""
                QLabel {
                    color: rgb(227, 255, 25);
                    border: 4px double yellow;
                    background-color: rgba(128, 200, 192, 127);
                    """+f"""
                    font-size: {a}px;"""+
            '}'
            )
            self.line.setMargin(5)
            layout.addWidget(self.line)
            lines.append(self.line)
        
        
#        # 添加移动按钮
#        self.move_btn = QLabel("<>", self)
#        self.move_btn.setStyleSheet("""
#            QLabel {
#                background-color: rgba(255, 255, 255, 127);
#                color: rgba(50, 50, 50, 1);
#                font-size: 12px;
#                padding: 4px;
#            }
#            QLabel:hover {
#                background-color: white;
#            }
#        """)
#        self.move_btn.setGeometry(0, 0, 20, 20)
#        self.move_btn.setAlignment(Qt.AlignCenter)

        # 添加关闭按钮
#        self.close_btn = QLabel("×", self)
#        self.close_btn.setStyleSheet("""
#            QLabel {
#                background-color: rgba(200, 50, 50, 10);
#                color: white;
#                font-size: 20px;
#                border-radius: 0px;
#                padding: 2px 8px;
#            }
#            QLabel:hover {
#                background-color: rgba(255, 0, 0, 220);
#            }
#        """)
#        self.close_btn.setAlignment(Qt.AlignCenter)
#        self.close_btn.setGeometry(scrWid-50, scrHei-50, 10, 30)
#        self.close_btn.mousePressEvent = lambda e: self.close()

        #创建指示器
        self.point = QLabel()
        self.point.setAlignment(Qt.AlignRight)
        
        # 用于窗口拖动的变量
        self.oldPos = None


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        if self.oldPos:
            delta = event.globalPos() - self.oldPos
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()

    def mouseReleaseEvent(self, event):
        self.oldPos = None
    
    def changeText(self,text):
        self.label.setText(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TransparentWindow()
    window.show()
    sys.exit(app.exec_())