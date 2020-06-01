# Asociación de operadores y precedencia
from Contenido.LstInstruccion import ABCInstruccion

precedence = (
    ('left', 'MAS', 'MENOS'),
    ('left', 'POR', 'DIVIDIDO'),
    ('right', 'UMENOS'),
)


# Definición de la gramática
def p_inicio(t):
    'inicio    : etiquetas'
    t[0] = t[1]

def p_etiquetas_lista(t):
    'etiquetas : etiquetas etiqueta'
    t[0]=t[1]

def p_etiquetas_lista_inicio(t):
    'etiquetas : etiqueta'
    t[0]=t[1]

def p_etiqueta_contenido(t):
    'etiqueta : IDENTIFICADOR DOBLEPUNTO instrucciones'
    t[0]=t[3]

def p_etiqueta_principal(t):
    'etiqueta : MAIN DOBLEPUNTO instrucciones'
    t[0]=t[3]

def p_instrucciones_lista(t):
    'instrucciones :  instrucciones instruccion '
    t[0] = t[1]
    t[0].agregar(t[2])


def p_instrucciones_lista_inicio(t):
    'instrucciones : instruccion '
    t[0] = ABCInstruccion.ListaInstruccion([t[1]])



def p_instrucciones_exit(t):
    'instruccion :  EXIT PUNTOCOMA'
    

def p_instrucciones_imprimir(t):
    'instruccion :  IMPRIMIR  PARA expresion PARC PUNTOCOMA'
    t[0] = ABCInstruccion.Imprimir(t[3])

def p_instrucciones_asignar(t):
    'instruccion :  DOLAR  IDENTIFICADOR IGUAL expresion PUNTOCOMA'
    t[0] = ABCInstruccion.Imprimir(t[3])

def p_instrucciones_goto(t):
    'instruccion :  GOTO  IDENTIFICADOR  PUNTOCOMA'
    t[0] = ABCInstruccion.Imprimir(t[3])

def p_expresion_binaria(t):
    '''expresion : valor MAS valor
                  | valor MENOS valor
                  | valor POR valor
                  | valor DIVIDIDO valor'''
    # if t[2] == '+'  : t[0] = t[1] + t[3]
    # elif t[2] == '-': t[0] = t[1] - t[3]
    # elif t[2] == '*': t[0] = t[1] * t[3]
    # elif t[2] == '/': t[0] = t[1] / t[3]
    t[0] = ABCInstruccion.ExpresionDoble(t[1], t[2], t[3])
    t[0] = ABCInstruccion.ExpresionDoble(t[1], t[2], t[3])
    t[0] = ABCInstruccion.ExpresionDoble(t[1], t[2], t[3])
    t[0] = ABCInstruccion.ExpresionDoble(t[1], t[2], t[3])

def p_expresion_sola(t):
    'expresion :  valor'
    t[0] = t[1]

def p_expresion_unaria(t):
    'expresion : MENOS valor %prec UMENOS'
    t[0] = -t[2]


def p_expresion_agrupacion(t):
    'expresion : PARA valor PARC'
    t[0] = t[2]


def p_expresion_entero(t):
    'valor    : ENTERO'
    t[0] = ABCInstruccion.Valor(t[1], 0)
    t[0] = ABCInstruccion.ExpresionSimple(t[0])


def p_expresion_decimal(t):
    'valor    : DECIMAL'
    t[0] = ABCInstruccion.Valor(t[1], 1)
    t[0] = ABCInstruccion.ExpresionSimple(t[0])

def p_expresion_decimal(t):
    'valor    : DOLAR IDENTIFICADOR'



def p_error(t):
    print("Error sintáctico en '%s'" % t)
