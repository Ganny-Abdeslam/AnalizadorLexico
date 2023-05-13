from PySide6 import QtCore, QtWidgets

from controller.generacionTokens import GeneracionTokens

# Clase de la interfaz gráfica
class MyWidget(QtWidgets.QWidget):
    def __init__(self, text) -> None:
        super().__init__()

        # Cuadro para el ingreso del texto
        self.label = QtWidgets.QLineEdit("Write here")

        # Botón y texto donde se presentarán los tokens
        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel(text,
                                     alignment = QtCore.Qt.AlignCenter)
        # Agregando la disposición de la interfaz
        self.layout = QtWidgets.QVBoxLayout(self)

        # Agregando el cuadro de ingreso de texto, el texto de los tokes y el botón
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        # Se le da funcionalidad al botón
        self.button.clicked.connect(self.magic)

    
    # Funcionalidad del botón: imprimir los tokens
    @QtCore.Slot()
    def magic(self):

        tokensImprimir = GeneracionTokens()
        tokensImprimir.generacionTokens(str(self.label.text()))

        self.text.setText('\n'.join(tokensImprimir.imprimir()))