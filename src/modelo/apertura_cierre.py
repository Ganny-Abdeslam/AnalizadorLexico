from modelo.token import Token
from modelo.categoria import Categoria

class Apertura_Cierre:

    def __init__(self) -> None:
        pass


    # Metodo para comprobar que los caracteres de apertura y cierre sean los correctos y 
    # se encuentren en la cadena de texto.
    # Simbolos: ( , {  , [ , ] , } , )

    def comprobacion(self,text) -> str:

        # Valida cada uno de los simbolos y si encuentra uno de los simbolos de apertura o cierre
        # retorna la cadena de texto. Sino retorna un string vacio.

        if text[0] == '(' or text[0] == '{' or text[0] == '[' or text[0] == ')' or text[0] == '}' or text[0] == ']':
            return text[0]
        
        return ""
    
    # Metodo para generar el token y comprobar que tipo de token es.
    
    def generacionToken(self,text) -> Token:
        var = self.comprobacion(text)

        return Token(var, Categoria.APERTURA_CIERRE)