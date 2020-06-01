reserved = {
    'print': 'IMPRIMIR',
    'main': 'MAIN',
    'unset': 'UNSET',
    'goto': 'GOTO',
    'read': 'READ',
    'exit': 'EXIT'

}
tokens = [
             'PARA',
             'PARC',
             'CORA',
             'CORC',
             'MAS',
             'MENOS',
             'POR',
             'DIVIDIDO',
             'DECIMAL',
             'ENTERO',
             'PUNTOCOMA',
             'IDENTIFICADOR',
             'DOBLEPUNTO',
             'DOLAR',
             'IGUAL'
         ] + list(reserved.values())

# Tokens
t_PARA = r'\('
t_PARC = r'\)'
t_CORA = r'\['
t_CORC = r'\]'
t_MAS = r'\+'
t_MENOS = r'-'
t_POR = r'\*'
t_DIVIDIDO = r'/'
t_PUNTOCOMA = r';'
t_DOBLEPUNTO = r':'
t_DOLAR = r'\$'
t_IGUAL = r'='


# Expresiones Regulares
def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'IDENTIFICADOR')  # Check for reserved words
    return t


def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Floaat value too large %d", t.value)
        t.value = 0
    return t


def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t


# Caracteres ignorados
t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")




def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
