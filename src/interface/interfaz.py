from PySide6 import QtCore, QtWidgets

from controller.generacionTokens import GeneracionTokens

class MyWidget(QtWidgets.QWidget):
    def __init__(self, text) -> None:
        super().__init__()
        self.label = QtWidgets.QLineEdit("Write here")

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel(text,
                                     alignment = QtCore.Qt.AlignCenter)
        self.layout = QtWidgets.QVBoxLayout(self)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    

    @QtCore.Slot()
    def magic(self):

        tokensImprimir = GeneracionTokens()
        tokensImprimir.generacionTokens(str(self.label.text()))

        self.text.setText('\n'.join(tokensImprimir.imprimir()))