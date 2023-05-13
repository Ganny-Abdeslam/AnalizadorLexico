from enum import Enum 

class Categoria(Enum):
    NO_RECONOCIDO = "NO_RECONOCIDO"
    ENTERO = "ENTERO"
    DECIMAL = "DECIMAL"
    HEXADECIMAL = "HEXADECIMAL"
    IDENTIFICADOR = "IDENTIFICADOR"
    PALABRA_RESERVADA = "PALABRA_RESERVADA"
    CADENA_CARACTERES = "CADENA_CARACTERES"
    COMENTARIO_LINEA = "COMENTARIO_LINEA"
    COMENTARIO_BLOQUE = "COMENTARIO_BLOQUE"
    OPERADOR_ARITMETICO = "OPERADOR_ARITMETICO"
    OPERADOR_RELACIONAL = "OPERADOR_RELACIONAL"
    OPERADOR_LOGICO = "OPERADOR_LOGICO"
    OPERADOR_INCREMENTO = "OPERADOR_INCREMENTO"
    OPERADOR_ASIGNACION = "OPERADOR_ASIGNACION"
    APERTURA_CIERRE = "APERTURA_CIERRE"

    def getString(self):
        return self.value