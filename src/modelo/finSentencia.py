
from modelo.token import Token
from modelo.categoria import Categoria

class FinSentencia:
    def __init__(self) -> None:
        pass

    # Metodo para comprobar que el fin de sentencia sea el correcto
    # y no contenga caracteres que no pertenezcan al operador. 
    # Simbolo: ¬

    def comprobacion(self,text) -> str:

        # En el primer if valida que se encuentre el simbolo de fin de sentencia "¬" y lo retorna si se cumple
        if text[0] == '¬':
            return '¬'
        
        # Retorna una cadena vacia si no se cumple la condicion anterior
        return ""


    # Metodo para generar el token y comprobar que tipo de token es.
    def generacionToken(self,text) -> Token:
        var = self.comprobacion(text)

        return Token(var, Categoria.FIN_SENTENCIA)