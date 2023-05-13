from modelo.token import Token
from modelo.categoria import Categoria


class OperadorAsignacion:

    def __init__(self) -> None:
        pass

    # Metodo para comprobar que el operador de asignacion sea el correcto 
    # y no contenga caracteres que no pertenezcan al operador. 
    # Simbolo: :=

    def comprobacion(self,text) -> str:

        # En el primer if valida el tamaño de la cadena, si es menor o igual a 1 pues no 
        # sera un operacion de asignacion y retorna la cadena tal cual.

        if len(text) <= 1:
            return text[0]
        
        # En el segundo if valida que el segundo caracter sea uno de los simbolos de asignacion "=" 
        # si entra al if, retorna los dos primeros caracteres del texto. Sino retorna la cadena tal cual.
        
        if text[1] == '=':
            return text[0:2]
            
        return text[0]
    
    # Metodo para generar el token y comprobar que tipo de token es. Adicional si encuentra el caracter ":" solo
    # lo toma como no reconocido.
    
    def generacionToken(self,text) -> Token:
        var = self.comprobacion(text)

        if var == ":":
            return Token("", Categoria.NO_RECONOCIDO)

        return Token(var, Categoria.OPERADOR_ASIGNACION)


