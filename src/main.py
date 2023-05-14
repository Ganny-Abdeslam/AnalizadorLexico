import sys
from PySide6 import QtWidgets
from interface.interfaz import MyWidget

from modelo.categoria import Categoria

# Se inicializa la aplicación
if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget("Aqui aparecen las weadas")

    widget.resize(600, 400)
    widget.show()

    sys.exit(app.exec())