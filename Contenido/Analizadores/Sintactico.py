# Asociación de operadores y precedencia
from Contenido.LstInstruccion import ABCInstruccion
from Contenido.LstInstruccion.Instruccion.Etiqueta import Etiqueta
from Contenido.LstInstruccion.Instruccion.Exit import Exit
from Contenido.LstInstruccion.Instruccion.Unset import Unset
from Contenido.LstInstruccion.Registro.Asignar import Asignar
from Contenido.LstInstruccion.Instruccion.goto import Goto
from Contenido.LstInstruccion.Instruccion.If import If
from Contenido.LstInstruccion.Registro.VariableValor import VariableValor
from Contenido.LstInstruccion.Instruccion.Referencia import Referencia
from Contenido.LstInstruccion.ABCInstruccion import Ts
from .Lexico import *
import ply.lex as lex
import ply.yacc as yacc

precedence = (
    ('left', 'MAS', 'MENOS'),
    ('left', 'POR', 'DIVIDIDO'),

)


# Definición de la gramática
def p_inicio(t):
    'inicio    : etiquetas'
    t[0] = t[1]


def p_etiquetas_lista(t):
    'etiquetas : etiquetas etiqueta'
    t[0] = t[1]
    t[0].agregar(t[2])


def p_etiquetas_lista_inicio(t):
    'etiquetas : etiqueta'
    t[0] = ABCInstruccion.ListaEtiqueta([t[1]])


def p_etiqueta_contenido(t):
    'etiqueta : IDENTIFICADOR ideti  instrucciones'
    t[0] = Etiqueta(t[3], t[1])
    global Ts
    Ts.consolidar_etiqueta()


def p_etiqueta_id_error(t):
    'ideti : DOBLEPUNTO'
    global Ts
    Ts.nueva_etiqueta(t[-1])

def p_etiqueta_principal(t):
    'etiqueta : MAIN ideti  instrucciones'
    t[0] = Etiqueta(t[3], t[1])
    global Ts
    Ts.consolidar_etiqueta()


def p_instrucciones_lista(t):
    'instrucciones :  instrucciones instruccion '
    t[0] = t[1]
    t[0].agregar(t[2])
    global Ts
    Ts.nueva_instruaccion(t[2])

def p_instrucciones_lista_inicio(t):
    'instrucciones : instruccion '
    t[0] = ABCInstruccion.ListaInstruccion([t[1]])
    global Ts
    Ts.nueva_instruaccion(t[1])

def p_instrucciones_exit(t):
    'instruccion :  EXIT PUNTOCOMA'
    t[0] = Exit()


def p_instrucciones_imprimir(t):
    'instruccion :  IMPRIMIR  PARA expresion PARC PUNTOCOMA'
    t[0] = ABCInstruccion.Imprimir(t[3])


def p_instrucciones_unset(t):
    'instruccion :  UNSET  PARA DOLAR IDENTIFICADOR PARC PUNTOCOMA'
    t[0] = Unset(t[4])


def p_instrucciones_asignar(t):
    'instruccion :  DOLAR  IDENTIFICADOR arra IGUAL expresion PUNTOCOMA'
    t[0] = Asignar(t[2], t[5])
    t[0].indices(t[3])


def p_arreglo_indice(t):
    'arra : CORA expresion CORC  arra '
    t[0] = t[4]
    t[0].append(t[2])


def p_arreglo_indice_epsilon(t):
    'arra : '
    t[0] = []


def p_instrucciones_goto(t):
    'instruccion :  GOTO  IDENTIFICADOR  PUNTOCOMA'
    t[0] = Goto(t[2])


def p_instrucciones_if(t):
    'instruccion :  IF   expresion  instruccion  '
    t[0] = If(t[2], t[3])


# HASTA AQUI HAY GRAFICA
def p_expresion_binaria(t):
    '''expresion : valor MAS valor
                  | valor MENOS valor
                  | valor POR valor
                  | valor DIVIDIDO valor
                  | valor MOD valor
                  | valor ANDB valor
                  | valor ORB valor
                  | valor XORB valor
                  | valor SHIFTD valor
                  | valor SHIFTI valor




                  | valor AND valor
                  | valor OR valor
                  | valor XOR valor


                  | valor DIFERENTE valor
                  | valor IGUALDOBLE valor
                  | valor MAYOR valor
                  | valor MAYORIGUAL valor
                  | valor MENORIGUAL valor
                  | valor MENOR valor'''

    t[0] = ABCInstruccion.ExpresionDoble(t[1], t[2], t[3])


def p_expresion_sola(t):
    'expresion :  valor'
    t[0] = t[1]


def p_expresion_unaria(t):
    '''expresion : MENOS valor
                | ABS PARA valor PARC
                | NOTB valor
                | NOT valor
                | MAS valor
                | ANDB DOLAR IDENTIFICADOR arra
                | READ PARA  PARC
                | ARRAY PARA  PARC '''

    if t[2] == "(":
        t[0] = ABCInstruccion.ExpresionSimpleOperacion(t[3], t[1])
    elif t[1]== "&":
        t[0] = Referencia(t[3],t[4])

    else:
        t[0] = ABCInstruccion.ExpresionSimpleOperacion(t[2], t[1])


def p_expresion_agrupacion(t):
    '''expresion : PARA INT PARC valor
                | PARA FLOAT PARC valor
                | PARA CHAR PARC valor'''

    t[0] = ABCInstruccion.ExpresionSimpleOperacion(t[4], t[2])


def p_expresion_parentesis(t):
    'expresion : PARA expresion PARC'
    t[0] = t[2]


def p_expresion_entero(t):
    'valor    : ENTERO'
    t[0] = ABCInstruccion.Valor(t[1], 0)
    t[0] = ABCInstruccion.ExpresionSimple(t[0])


def p_expresion_decimal(t):
    'valor    : DECIMAL'
    t[0] = ABCInstruccion.Valor(t[1], 1)
    t[0] = ABCInstruccion.ExpresionSimple(t[0])

def p_expresion_cadena(t):
    'valor    : CADENA'
    t[0] = ABCInstruccion.Valor(t[1], 2)
    t[0] = ABCInstruccion.ExpresionSimple(t[0])

def p_expresion_valor_unico_variable(t):
    'valor    : DOLAR IDENTIFICADOR arra'
    t[0] = VariableValor(t[2])
    t[0].indices(t[3])


def p_error(t):
    global Ts
    Ts.exit_exec=0
    print("Error sintáctico en '%s'" % t)


def analizar_ascendente(input: str):
    # Construyendo el analizador léxico
    lexer = lex.lex()
    parser = yacc.yacc()
    return parser.parse(input)
