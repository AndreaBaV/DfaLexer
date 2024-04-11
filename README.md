# DfaLexer
 DFA de un Lexer en Python 

## Requisitos de ejecución
1. Instalación de Python
2. Crear un archivo llamado "expresiones.txt"

## Detalles
Se cuenta con dos autómatas, uno que funciona para el caso práctico dado (pruebas.py), y otro incompleto que planea utilizarse para cualquier tipo de caso. 

Pruebas.py simplemente identifica el tipo de caracter como valores de un conjunto (tipo de token), y al cambiar el tipo de caracter, y que no sea encontrado dentro del conjunto "tipo de tolen", finaliza la formación del token.

Por otro lado, el autómata incompleto (automata1.py), planea funcionar como un grafo, que identifica todos los posibles takens a los que puede pertenecer un mismo caracter, y lo redirecciona dependiendo del caracter que sea encontrado después de este. 
