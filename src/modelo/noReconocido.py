from modelo.token import Token
from modelo.categoria import Categoria

class NoReconocido:
    def __init__(self) -> None:
        pass

    def comprobacion(self,text) -> str:
        if len(text) <= 0 or text[0] in '><=!~+-*/%^,()[]{}:&¬ \n':
            return ""
        
        return text[0] + self.comprobacion(text[1:])

    # Metodo para generar el token y comprobar que tipo de token es.
    def generacionToken(self,text) -> Token:
        var = self.comprobacion(text)

        return Token(var, Categoria.NO_RECONOCIDO)