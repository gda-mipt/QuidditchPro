from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel
import sys

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Пример расположения виджета')

        main_layout = QHBoxLayout(self)
        left_layout = QVBoxLayout()
        main_layout.addLayout(left_layout)

        label = QLabel('Текст в центре левой части', self)
        left_layout.addStretch(1)
        left_layout.addWidget(label)
        left_layout.addStretch(1)
        l2 = QLabel('right', self)
        main_layout.addWidget(l2)

        self.setLayout(main_layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.setGeometry(100, 100, 400, 300)
    widget.show()
    sys.exit(app.exec_())