from modelo.token import Token
from modelo.categoria import Categoria

class CadenaCaracteres:
    def __init__(self) -> None:
        pass

    def comprobacion(self,text) -> str:
        if len(text) <= 0 or text[0] == '$':
            return ""
        
        return text[0] + self.comprobacion(text[1:])

    # Metodo para generar el token y comprobar que tipo de token es.
    def generacionToken(self,text) -> Token:
        if len(text) <= 1:
            return Token("", Categoria.COMENTARIO)    
        
        var = self.comprobacion(text[1:])

        return Token("$" + var + "$", Categoria.CADENA_CARACTERES)