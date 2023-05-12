from modelo.palabrasReservadas import PalabrasReservadas
from modelo.enteros import Entero
from modelo.identificadores import Identificardor
from modelo.finSentencia import FinSentencia
from modelo.aritmeticos import Aritmeticos
from modelo.logicos import Logicos
from modelo.incrementoDecremento import IncrementoDecremento
from modelo.separador import Separador
from modelo.relacionales import OperadorRelacional
from modelo.asignacion import OperadorAsignacion
from modelo.apertura_cierre import Apertura_Cierre

# Clase encargada de la identificación y creación de los tokens del texto ingresado por el susuario
class GeneracionTokens():
    def __init__(self) -> None:
        self.allTokens = []
        self.allTokensImprimir = []

    # Este metodo crea los Tokens revisando caracter a caracter del texto ingresado
    def generacionTokens(self, text) -> None:

        # Texto vacio
        if len(text) == 0 :
            return
        
        
        dato = PalabrasReservadas()
        
        if text[0].isalpha() :
            if self.acumlacionToken(dato, text):
                return

        # Generador de tokens de numeros enteros y reales
        dato = Entero()

        if text[0].isdigit() :
            if self.acumlacionToken(dato, text):
                return
        
        # Generador de tokens de identificadores
        dato = Identificardor()

        if text[0].isalpha() :
            if self.acumlacionToken(dato, text):
                return
        
        # Generador de tokens de fin de sentencia (¬)
        dato = FinSentencia()

        if text[0] == '¬':
            if self.acumlacionToken(dato, text):
                return
        
        # Generador de tokens de operadores aritmeticos (+ - / % ^)
        dato = Aritmeticos()

        if text[0] == '+' or text[0] == '-' or text[0] == '*' or text[0] == '/' or text[0] =='%' or text[0] == '^':
            if self.acumlacionToken(dato, text):
                return
            
        # Generador de tokens de operadores lógicos (& &| !)    
        dato = Logicos()

        if text[0] == '&' or text[0] == '!':
            if self.acumlacionToken(dato, text):
                return
        
        # Generador de tokens de operadores de incremento y decremento (++ --)
        dato = IncrementoDecremento()

        if text[0] == '+' or text[0] == "-":
            if self.acumlacionToken(dato, text):
                return
        
        # Generador de tokens de separador (,)
        dato = Separador()
        
        if text[0] == ',':
            if self.acumlacionToken(dato, text):
                return
            
        dato = OperadorRelacional()
        #< , >, >= , <= , == , !=, ~=

        if text[0] == '<' or text[0] == '>' or text[0] == '>=' or text[0] == '<=' or text[0] == '=' or text[0] == '!' or text[0] == '~':
            if self.acumlacionToken(dato, text):
                return
            
        dato = OperadorAsignacion()

        if text[0] == ':':
            if self.acumlacionToken(dato, text):
                return
            
        dato = Apertura_Cierre()

        if text[0] == '(' or text[0] == ')' or text[0] == '[' or text[0] == ']' or text[0] == '{' or text[0] == '}':
            if self.acumlacionToken(dato, text):
                return
        
        #Token(var, Categoria.NO_RECONOCIDO)
        self.generacionTokens(text[1:])

    # Metodo que llama al metodo de generacion de tokens y los guarda en una lista
    def acumlacionToken(self, dato, text) -> bool:
            token = dato.generacionToken(text)

            if len(token.getPalabra()) == 0 :
                 return False
            
            self.allTokens.append(token)
            self.allTokensImprimir.append(token.imprimir())

            self.generacionTokens(text[len(self.allTokens[len(self.allTokens)-1].getPalabra()):])
            return True

    # Metodo que imprime los tokens acomulados en la lista
    def imprimir(self) -> list:
        return self.allTokensImprimir