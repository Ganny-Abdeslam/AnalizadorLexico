from modelo.palabrasReservadas import PalabrasReservadas
from modelo.enteros import Entero
from modelo.identificadores import Identificardor
from modelo.relacionales import OperadorRelacional
from modelo.asignacion import OperadorAsignacion
from modelo.apertura_cierre import Apertura_Cierre

class GeneracionTokens():
    def __init__(self) -> None:
        self.allTokens = []
        self.allTokensImprimir = []

    def generacionTokens(self, text) -> None:

        if len(text) == 0 :
            return
        
        dato = PalabrasReservadas()
        
        if text[0].isalpha() :
            if self.acumlacionToken(dato, text):
                return

        
        dato = Entero()

        if text[0].isdigit() :
            if self.acumlacionToken(dato, text):
                return
        
        dato = Identificardor()

        if text[0].isalpha() :
            if self.acumlacionToken(dato, text):
                return
            
        
        #Hace el llamado a la clase OperadorRelacional para validar si el operador es correcto.  
        dato = OperadorRelacional()

        if text[0] == '<' or text[0] == '>' or text[0] == '>=' or text[0] == '<=' or text[0] == '=' or text[0] == '!' or text[0] == '~':
            if self.acumlacionToken(dato, text):
                return
            
        #Hace el llamado a la clase OperadorAsignacion para validar si el operador es correcto.   
        dato = OperadorAsignacion()

        if text[0] == ':':
            if self.acumlacionToken(dato, text):
                return
            
        #Hace el llamado a la clase Apertura_Cierre para validar si el operador es correcto.       
        dato = Apertura_Cierre()

        if text[0] == '(' or text[0] == ')' or text[0] == '[' or text[0] == ']' or text[0] == '{' or text[0] == '}':
            if self.acumlacionToken(dato, text):
                return
        
        #Token(var, Categoria.NO_RECONOCIDO)
        self.generacionTokens(text[1:])

    def acumlacionToken(self, dato, text) -> bool:
            token = dato.generacionToken(text)

            if len(token.getPalabra()) == 0 :
                 return False
            
            self.allTokens.append(token)
            self.allTokensImprimir.append(token.imprimir())

            self.generacionTokens(text[len(self.allTokens[len(self.allTokens)-1].getPalabra()):])
            return True

    def imprimir(self) -> list:
        return self.allTokensImprimir