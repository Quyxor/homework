"""
PyQt5

QObject - базовый класс для всех классов Qt
QWidget - базовый класс для всех элементов GUI

"""

import sys

from PyQt5.QtWidgets import (
    QApplication, QMainWindow,
    QLabel, QPushButton
)


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.__increment = True

        self.initUi()
        self.initSignals()

    def initUi(self):
        """Создаем и настраиваем UI"""
        self.resize(400, 300) # setWidth, setHeight

        self.setMinimumSize(300, 200)
        self.setMaximumSize(600, 400)

        self.btn = QPushButton(u'We will push the button', self)

        self.setCentralWidget(self.btn)

    def initSignals(self):
        self.btn.clicked.connect(self.onClick)

    def onClick(self):
        if self.__increment:
            self.resize(self.width() + 10, self.height() + 10)
        else:
            self.resize(self.width() - 10, self.height() - 10)

        if self.width() <= self.minimumWidth():
            self.__increment = True

        if self.width() >= self.maximumWidth():
            self.__increment = False


if __name__ == '__main__':
    app = QApplication(sys.argv) # приложение с GUI

    w = MainWindow()
    w.show()

    sys.exit(app.exec_()) # запускает Event-Loop
