from modelo.token import Token
from modelo.categoria import Categoria

# Clase de los identificadores
class Identificardor():
    def __init__(self) -> None:
        pass
    
    def comprobacion(self, text, count) -> str:

        # Comprobación si la cadena de texto está vacia o tiene más de diez caracteres
        if len(text) <= 0 or count > 10 :
            return ""
        
        # Comprobación si la posición actual en la cadena es un alfabético, un dígito o un guión bajo
        if text[0].isalpha() or text[0].isdigit() or text[0] == '_' :
            count += 1
            return text[0] + self.comprobacion(text[1:], count)

        return ""
    
    # Metodo para generar el token y comprobar que tipo de token es.
    
    def generacionToken(self, text) -> Token:
        var = self.comprobacion(text, 0)

        return Token(var, Categoria.IDENTIFICADOR)
