from modelo.decimales import Decimal
from modelo.token import Token
from modelo.categoria import Categoria

class Entero:
    def __init__(self) -> None:
        pass

    def comprobacion(self, num) -> str:

        if len(num) <= 0:
            return ""
        
        if num[0].isdigit():
            return num[0] + self.comprobacion(num[1:])
        
        elif num[0] == '.':
            if len(num) <= 1:
                return ""
            
            if not(num[1].isdigit()):
                return ""
            
            dec = Decimal()
            
            return "." + dec.comprobar(num[1:])

        return ""
    
    def generacionToken(self, num) -> Token:
        var = self.comprobacion(num)

        if len(num) > len(var) and num[len(var)].isalpha() :
            return Token("", Categoria.NO_RECONOCIDO)

        if "." in var :
            return Token(var, Categoria.DECIMAL)

        elif len(var) != 0 :
            return Token(var, Categoria.ENTERO)