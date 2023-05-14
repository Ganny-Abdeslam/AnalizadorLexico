from modelo.token import Token
from modelo.categoria import Categoria

class PalabrasReservadas:
    def __init__(self) -> None:
        pass

    # Metodo  que comprueba si la palabra reservada esta en el texto.
    # y no contenga caracteres que no pertenezcan.

    def comprobacion(self, text,  palabras) -> str:

        # En el primer if valida el tamaño de la cadena, y retorna una cadena vacia

        if len(palabras) <= 0:
            return ""
        
        # En el segundo if, toma una palabra de la lista de reservadas, y la compara con el tamaño de la palabra recibida
        # Si coinciden, valida cada bloque, si se cumple luego checkea que sigue despues de esa palabra
        # Por si tiene otro caracter que no corresponde, o un espacio.
        
        if palabras[0] in text[:len(palabras[0])]:
            if len(text) < len(palabras[0])+1:
                return palabras[0]
            
            if text[len(palabras[0])].isalpha() or text[len(palabras[0])].isdigit():
                return ""
            
            return palabras[0]
        
        # Retorna un llamado recursivo

        return self.comprobacion(text, palabras[1:])
    
    # Metodo para generar el token y comprobar que tipo de token es ademas contiene las palabras reservadas

    def generacionToken(self, text) -> Token:
        palabras = [
            'Entier',
            'Reel',
            'Pour',
            'Alors',
            'Prive',
            'Publique',
            'Emballer',
            'Importer',
            'Classe',
            'Retour',
            'Casser',
        ]
        var = self.comprobacion(text, palabras)

        if var is None:
            var = ""
        
        return Token(var, Categoria.PALABRA_RESERVADA)