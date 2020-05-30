# Asociación de operadores y precedencia
from .Auxiliares.LstInstruccion import ABCInstruccion

precedence = (
    ('left', 'MAS', 'MENOS'),
    ('left', 'POR', 'DIVIDIDO'),
    ('right', 'UMENOS'),
)


# Definición de la gramática
def p_instrucciones_lista(t):
    '''instrucciones    : instruccion instrucciones
                        | instruccion '''


def p_instrucciones_evaluar(t):
    'instruccion :  expresion  PUNTOCOMA'
    print('El valor de la expresión es: ' + str(t[1]))


def p_expresion_binaria(t):
    '''expresion : expresion MAS expresion
                  | expresion MENOS expresion
                  | expresion POR expresion
                  | expresion DIVIDIDO expresion'''
    # if t[2] == '+'  : t[0] = t[1] + t[3]
    # elif t[2] == '-': t[0] = t[1] - t[3]
    # elif t[2] == '*': t[0] = t[1] * t[3]
    # elif t[2] == '/': t[0] = t[1] / t[3]
    t[0] = ABCInstruccion.ExpresionDoble(t[1], t[2], t[3])


def p_expresion_unaria(t):
    'expresion : MENOS expresion %prec UMENOS'
    t[0] = -t[2]


def p_expresion_agrupacion(t):
    'expresion : PARA expresion PARC'
    t[0] = t[2]


def p_expresion_number(t):
    '''expresion    : ENTERO
                    | DECIMAL'''
    t[0] = t[1]


def p_error(t):
    print("Error sintáctico en '%s'" % t.value)
