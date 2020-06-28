reserved = {
    'print': 'IMPRIMIR',
    'main': 'MAIN',
    'unset': 'UNSET',
    'goto': 'GOTO',
    'read': 'READ',
    'exit': 'EXIT',
    'if': 'IF',
    'abs': 'ABS',
    'xor': 'XOR',
    'int': 'INT',
    'float': 'FLOAT',
    'char': 'CHAR',
    'array': 'ARRAY'

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
             'IGUAL',
             'MOD',
             'NOT',
             'AND',
             'OR',
             'NOTB',
             'ANDB',
             'ORB',
             'XORB',
             'SHIFTI',
             'SHIFTD',
             'IGUALDOBLE',
             'DIFERENTE',
             'MENOR',
             'MENORIGUAL',
             'MAYOR',
             'MAYORIGUAL',
             'CADENA'
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
t_IGUAL = r'\='
t_MOD = r'\%'
t_NOT = r'\!'
t_AND = r'\&\&'
t_OR = r'\|\|'

t_NOTB = r'\~'
t_ANDB = r'\&'
t_ORB = r'\|'
t_XORB = r'\^'
t_SHIFTI = r'<<'
t_SHIFTD = r'>>'

t_IGUALDOBLE = r'\=\='
t_DIFERENTE = r'\!\='
t_MAYOR = r'\>'
t_MENOR = r'\<'
t_MENORIGUAL = r'\<\='
t_MAYORIGUAL = r'\>\='


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


def t_CADENA(t):
    r'("|\')([^"\']*)("|\')'
    try:
        cadena: str = t.value
        t.value = cadena.replace("\"", "")
        t.value = t.value.replace("\'", "")
    except ValueError:
        print("Error Cadena %d", t.value)
        t.value = ""
    return t


# Caracteres ignorados
t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_carro(t):
    r'\r+'
    t.lexer.lineno += t.value.count("\n")

def t_comentario(t):
    r'\#(.*)(\n)?'
    t.lexer.lineno += t.value.count("\n")


def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return ((token.lexpos - line_start) + 1, token.lineno)


def t_error(t):
    from Contenido.LstInstruccion.ABCInstruccion import Ts
    global Ts
    tup = find_column(Ts.texto_analisis, t)
    Ts.cargar_error(
        "El token con lexema \"" + str(t.value[0]) + "\" ocasiono un  error lexico", 30, tup)

    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
