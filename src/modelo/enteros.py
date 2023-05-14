from modelo.decimales import Decimal
from modelo.token import Token
from modelo.categoria import Categoria

# Clase del token de los números enteros
class Entero:
    def __init__(self) -> None:
        pass

    def comprobacion(self, num) -> str:

        # Comprobación si la cadena está vacía
        if len(num) <= 0:
            return ""
        
        # Comprobación si es un digito lo que se encuentra en la posición actual
        if num[0].isdigit():
            return num[0] + self.comprobacion(num[1:])
        
        # Comprobación si es un punto lo que se encuentra en la posición actual
        elif num[0] == '.':
            if len(num) <= 1:
                return ""
            
            # Comprobación si lo que se encuentra en la siguiente posición no es un digito
            if not(num[1].isdigit()):
                return ""
            
            # Llamado de la clase del token de número decimal
            dec = Decimal()
            
            return "." + dec.comprobar(num[1:])

        return ""
    
    def generacionToken(self, num) -> Token:
        var = self.comprobacion(num)

        # Si el símbolo es alfabético
        if len(num) > len(var) and num[len(var)].isalpha() :
            return Token("", Categoria.NO_RECONOCIDO)

        # Si el símbolo es un punto
        if "." in var :
            return Token(var, Categoria.DECIMAL)

        # Si la cadena no está vacia
        elif len(var) != 0 :
            return Token(var, Categoria.ENTERO)