class Lexer:
    def tipo_token(self, token):
        if token.isalpha():
            return 'Variable'
        elif token.isdigit():
            return 'Entero'
        elif '.' in token:
            try:
                float(token)
                return 'Flotante'
            except ValueError:
                pass
        elif token in {'=', '+', '-', '*', '/', '^'}:
            return 'Operador'
        elif token in {'(', ')'}:
            return 'Paréntesis'
        elif token.startswith('#'):
            return 'Comentario'
        return None


def lexerAritmetico(archivo):
    lexer = Lexer()
    try:
        with open(archivo, 'r') as file:
            for linea in file:
                tokens = linea.split()
                comentario = False
                comentario_token = ''
                for token in tokens:
                    if comentario or token.startswith('#'):
                        if not comentario:
                            comentario = True
                            if token.startswith('#'):
                                comentario_token = token + ' '
                            else:
                                comentario_token = '#' + token + ' '
                        else:
                            comentario_token += token + ' '
                    else:
                        tipo = lexer.tipo_token(token)
                        if tipo:
                            print(f'{token} | {tipo}')
                if comentario:
                    print(f'{comentario_token} | Comentario')
    except FileNotFoundError:
        print("El archivo no se encontró.")


lexerAritmetico("expresiones.txt")
