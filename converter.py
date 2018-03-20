import sys

from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QLabel, QDoubleSpinBox, QPushButton,
    QVBoxLayout
)


class Converter(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUi()
        self.initLayouts()
        self.initSignals()


    def initUi(self):
        self.setWindowTitle('Конвертер валют')

        self.srcLabel = QLabel('Сумма в рублях', self)
        self.resultLabel = QLabel('Сумма в долларах', self)

        self.srcAmount = QDoubleSpinBox(self)
        self.srcAmount.setMaximum(999999999)

        self.resultAmount = QDoubleSpinBox(self)
        self.resultAmount.setMaximum(999999999)
        #self.resultAmount.setReadOnly(True)

        self.convertBtn = QPushButton('Перевести', self)
        # self.convertBtn.setDisabled(True)


    def initSignals(self):
        self.convertBtn.clicked.connect(self.onClickConvertBtn)


    def initLayouts(self):
        w = QWidget(self)

        self.mainLayout = QVBoxLayout(w)
        self.mainLayout.addWidget(self.srcLabel)
        self.mainLayout.addWidget(self.srcAmount)
        self.mainLayout.addWidget(self.resultLabel)
        self.mainLayout.addWidget(self.resultAmount)
        self.mainLayout.addWidget(self.convertBtn)

        self.setCentralWidget(w)


    def onClickConvertBtn(self):
        src_value = self.srcAmount.value()
        result_value = self.resultAmount.value()

        if src_value:
            self.resultAmount.setValue(src_value / 30)
        elif result_value:
            self.srcAmount.setValue(result_value * 30)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    c = Converter()
    c.show()

    sys.exit(app.exec_())
