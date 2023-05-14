from modelo.token import Token
from modelo.categoria import Categoria

class NoReconocido:
    def __init__(self) -> None:
        pass

    # Metodo para comprobar que el caracter no es reconocido.

    def comprobacion(self,text) -> str:

        # En el primer if valida el tamaño de la cadena, y algunos caracteres que SI se reconocen, y retorna una
        # cadena vacia ya que no es un error como tal.

        if len(text) <= 0 or text[0] in '><=!+-*/%^,()[]{}:&¬ \n':
            return ""
        
        # Retorna la cadena en la posicion cero y una llamada recursiva con el resto de la cadena.
        return text[0] + self.comprobacion(text[1:])

    # Metodo para generar el token y comprobar que tipo de token es.
    def generacionToken(self,text) -> Token:
        var = self.comprobacion(text)

        return Token(var, Categoria.NO_RECONOCIDO)