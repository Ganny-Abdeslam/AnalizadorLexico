from modelo.token import Token
from modelo.categoria import Categoria

class PalabrasReservadas:
    def __init__(self) -> None:
        pass

    def comprobacion(self, text,  palabras) -> str:
        if len(palabras) <= 0:
            return ""
        
        if palabras[0] in text[:len(palabras[0])]:
            if len(text) < len(palabras[0])+1:
                return palabras[0]
            
            if text[len(palabras[0])] == ' ':
                return palabras[0]

        return self.comprobacion(text, palabras[1:])

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