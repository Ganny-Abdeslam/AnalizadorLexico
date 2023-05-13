# Analizador Léxico
Proyecto de Analizador Léxico de un lenguaje inventado escrito en Python, que permite reconocer diversos tokes de dicho lenguaje en un texto ingresado por el usuario.
## Lenguaje MyFirst
MyFirst es un lenguaje inventado, el cual sigue utiliza diversos okens que se enumeran a continuación:
1. Números naturales
2. Números Decimales
3. Iddentificadores
    - No superan los 10 caracteres.
4. Palabras Reservadas
    - Entero: `Entier`
    - Real: `Reel`
    - Para: `Pour`
    - Mientras: `Alors`
    - Private: `Prive`
    - Public: `Publique`
    - Paquete: `Emballer`
    - Importar: `Importer`
    - Clase: `Classe`
    - Return: `Retour`
    - Break: `Casser`
5. Operadores Aritméticos
    - `+ - * / % ^`
6. Operadores Relacionales
    - `== <= >= != ~=`
7. Operadores Lógicos
    - `& ! &|`
8. Operador Asignación
    - `:=`
9. Operadores de Incremento y Decremento
    - `++ --`
10. Parentesis, Llaves y Corchetes (Apertura y Cierre)
    - `( { [ ] } )`
11. Fin de sentencia
    - `¬`
12. Seprarador
    - `,`
13. Hexadecimal
14. Cadenas de caracteres
    - `ª ª`
13. Comentarios en una linea.
    - `??`
## Funcionamiento
Los Tokens fueron creados usando como base Automatas Finitos Deterministas (AFD),con los cuales se creó una función que lee caracter a caracter el texto ingresado por el usuario con el fin de ide ntificar léxicamnete la composición del escrito con relación al lenguaje MyFirst.
## Autores
El proyecto fue realizado por estudiantes del programa de Ingenieria de Sistemas y Computación de la Universidad del Quindío en Colombia para la asignatura de Teoría de Lenguajes Formales.
```
    - Gasser Abdeslam Abdelgelil Serna.
    - David Idárraga Lugo.
    - Santiago Marín Dussán.
```
### Licencia
GNU General Public License