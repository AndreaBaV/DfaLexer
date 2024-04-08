class LexerDFA:
    def __init__(self, archivo):
        self.archivo = archivo     # Archivo .txt que se analizará 
        self.alfabeto = self.Alfabeto()

    class Alfabeto:
        def __init__(self):
            self.enteros = tuple(str(i) for i in range(10))
            self.flotantes = ('.',) + self.enteros
            self.operadores = ('=', '+', '-', '*', '/', '^' )
            self.variables = ('_',) + \
                             tuple(chr(i) for i in range (ord('a'), ord('z')+1)) + \
                             tuple(chr(i) for i in range(ord('A'), ord('Z')+1))
            self.parentesis = ('(',')')
            self.comentarios = ('#',) + self.flotantes + self.variables + self.operadores
            self.espacio_blanco = (' ',)
            
    def analizar_linea(self, linea):
        tokens = []
        for caracter in linea:
            token = self.obtener_subset(caracter)
            tokens.append((caracter, token))
        return tokens
        
    def obtener_subset(self, caracter):
        if caracter in self.alfabeto.enteros:
            return "Enteros"
        elif caracter in self.alfabeto.flotantes:
            return "Flotantes"
        elif caracter in self.alfabeto.operadores:
            return "Operadores"
        elif caracter in self.alfabeto.variables:
            return "Variables"
        elif caracter in self.alfabeto.parentesis:
            return "Paréntesis"
        elif caracter in self.alfabeto.comentarios:
            return "Comentarios"
        elif caracter in self.alfabeto.espacio_blanco:
            return "Espacio en blanco"
        else:
            return "Carácter desconocido"

# Ejemplo de uso
lexer = LexerDFA("archivo.txt")
with open(lexer.archivo, 'r') as archivo:
    for linea in archivo:
        tokens = lexer.analizar_linea(linea)
        print("Token\t\tTipo")
        print("---------------------------")
        for token, tipo in tokens:
            print(f"{token}\t\t{tipo}")
        print()
