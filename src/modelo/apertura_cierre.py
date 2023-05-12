from modelo.token import Token
from modelo.categoria import Categoria

class Apertura_Cierre:

    def __init__(self) -> None:
        pass

    def comprobacion(self,text) -> str:

        if text[0] == '(' or text[0] == '{' or text[0] == '[' or text[0] == ')' or text[0] == '}' or text[0] == ']':
            return text[0]
        
        return ""
    
    def generacionToken(self,text) -> Token:
        var = self.comprobacion(text)

        return Token(var, Categoria.APERTURA_CIERRE)

