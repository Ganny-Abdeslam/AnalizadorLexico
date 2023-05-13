from modelo.categoria import Categoria

# Clase del token
class Token():
    def __init__(self, palabra, categoria) -> None:
        self.palabra = palabra
        self.categoria = categoria

    def imprimir(self) -> str:
        return self.categoria.getString() + ": " + self.palabra
    
    def getPalabra(self) -> str:
        return self.palabra
