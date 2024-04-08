# DFA de un Lexer
# Andrea Bahena

class LexerDFA:
    def __init__(self, archivo):
        self.archivo = archivo
        self.alfabeto = self.Alfabeto()
      #  self.estados = self.Estados()
         
    
    def leerLinea(self):
        with open(self.archivo, 'r') as archivo:
            for linea in archivo:
                token = ""
                for i in range(len(linea)-1):
                    caracter= linea[i]
                    sigCaracter = linea[i+1]
                    tipoToken = self.alfabeto.tipoToken(caracter)
                    sigTipoToken = self.alfabeto.tipoToken(sigCaracter)
                    if tipoToken == sigTipoToken:
                        token += caracter
                    else:
                        if tipoToken == "Espacio":
                            continue
                        token += caracter
                        print(f"Token: {token}   |   Tipo: {tipoToken}")
                        token = ""
                
                finCaracter = linea[-1]
                finTipoToken = self.alfabeto.tipoToken(finCaracter)
                token += finCaracter
                print(f"Token: {token}  |   Tipo: {finTipoToken}")
                
    def tipoCadena(self, cadena):
        tipos = ["Espacio", "Entero", "Flotante", "Operador", "Variable", "Parentesis", "Comentario"]
        tipoToken = None
        for caracter in cadena:
            tipoCaracter = self.alfabeto.tipoToken(caracter)
            if tipoToken is None:
                tipoToken = tipoCaracter
            else:
                if tipos.index(tipoCaracter) < tipos.index(tipoToken):
                    tipoToken = tipoCaracter
        return tipoToken
                    
    # Crear una subclase que contenga tuplas con los subsets del alfabeto
    class Alfabeto:
        def __init__(self):
            
            self.enteros = tuple(str(i) for i in range(10))
            self.flotantes = ('.', 'e', 'E','-') + self.enteros
            self.operadores = ('=', '+', '-', '*', '/', '^' )
            # chr y ord son funciones para acceder al código ASCII y hacer conversiones 
            self.variables= ('_',) + \
                            tuple(chr(i) for i in range (ord('a'), ord('z')+1)) + \
                            tuple(chr(i) for i in range(ord('A'), ord('Z')+1)) + self.enteros
            self.parentesis= ('(',')')
            self.espacio_blanco = (' ',)
            self.comentarios= ('#',)+ self.flotantes + self.variables + self.operadores + self.espacio_blanco
            
        def tipoToken(self, caracter):
            posToken= [] 
     
            if caracter in self.enteros:
                posToken.append(1)          # Representa al estado de enteros
                posToken.append(2)          # Representa a los flotantes
                posToken.append(3)          # Representa a las variables
            elif caracter in self.flotantes:
                posToken.append(2)
            elif caracter in self.operadores:
                posToken.append(4)          # Representa a los operadores
            elif caracter in self.variables:
                posToken.append(3)          
            elif caracter in self.parentesis:
                posToken.append(5)          # Representa a los paréntesis
            elif caracter in self.espacio_blanco:
                posToken.append(6)          # Representa a los espacios en blanco
            elif caracter in self.comentarios:
                posToken.append(7)          # Representa a los comentarios
            else:
                LexerDFA.errores(1)
            return posToken
        
    @staticmethod
    def errores(num_error):
        if num_error == 1:
            return "Error 1: se encontro un caracter fuera del alfabeto"
            
            
    
    # Crear una subclase para los estados y sus funciones de transición    
    class Estados:
       estados = {
        "Enteros": 1,
        "Flotantes": 2,
        "Variables": 3,
        "Operadores": 4,
        "Paréntesis": 5,
        "Espacios en blanco": 6,
        "Comentarios": 7
    }
       
       

lex= LexerDFA("expresiones.txt")
lex.leerLinea()