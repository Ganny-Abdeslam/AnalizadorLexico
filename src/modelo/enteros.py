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
            return num[0] + self.comprobacion(num[1:len(num)])
        
        elif num[0] == '.':
            if len(num) <= 1:
                return ""
            
            if not(num[1].isdigit()):
                return ""
            
            dec = Decimal()
            
            return "." + dec.comprobar(num[1:len(num)])

        return ""
    
    def generacionToken(self, num) -> Token:
        var = self.comprobacion(num)

        if "." in var:
            token = Token(var, Categoria.DECIMAL)

        elif len(var) != 0:
            token = Token(var, Categoria.ENTERO)

        else:
            token = Token(var, Categoria.NO_RECONOCIDO)

        return token