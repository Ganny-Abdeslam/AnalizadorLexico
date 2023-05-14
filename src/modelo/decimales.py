# Clase de los Numeros decimales (reales)
class Decimal():
    def __init__(self) -> None:
        pass

    def comprobar(self, num) -> str:
        
        # Comprobación si la cadena no está vacia
        if len(num) <= 0:
            return ""
        
        #  Comprobación que todos los decimales sean digitos
        if num[0].isdigit():
            return num[0] + self.comprobar(num[1:])
        
        return ""