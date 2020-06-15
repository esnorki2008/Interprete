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

    global Ts
    Ts.rp_nuevo_nodo('inicio    : etiquetas', "t[0] = t[1]")


def p_etiquetas_lista(t):
    'etiquetas : etiqueta etiquetasp'
    t[0] = t[2]

    global Ts
    Ts.rp_nuevo_nodo('etiquetas : etiquetas etiqueta', "t[0] = t[2] ")

def p_etiqeutas_sin_recursividad(t):
    'etiquetasp : etiqueta  etiquetasp'
    t[0]=t[2]
    t[0].lst.insert(0, t[-1])

    global Ts
    Ts.rp_nuevo_nodo('etiquetasp : etiqueta  etiquetasp', "t[0] = t[2] \n t[0].lst.insert(0, t[-1])")

def p_etiqeutas_sin_recursividad_epsilon(t):
    'etiquetasp : '
    t[0] = ABCInstruccion.ListaEtiqueta([t[-1]])

    global Ts
    Ts.rp_nuevo_nodo('etiquetasp : ', "t[0] = ABCInstruccion.ListaEtiqueta([t[-1]])")

def p_etiqueta_contenido(t):
    'etiqueta : IDENTIFICADOR ideti  instrucciones'
    t[0] = Etiqueta(t[3], t[1])
    global Ts
    Ts.consolidar_etiqueta()
    t[0].n_t(find_column(Ts.texto_analisis, t.slice[1]))

    Ts.rp_nuevo_nodo('etiqueta : IDENTIFICADOR ideti  instrucciones', "t[0] = Etiqueta(t[3], t[1])")


def p_etiqueta_id_error(t):
    'ideti : DOBLEPUNTO'
    global Ts
    Ts.nueva_etiqueta(t[-1])

    Ts.rp_nuevo_nodo('ideti : DOBLEPUNTO', "Ts.nueva_etiqueta(t[-1])")

def p_etiqueta_principal(t):
    'etiqueta : MAIN ideti  instrucciones'
    t[0] = Etiqueta(t[3], t[1])
    global Ts
    Ts.consolidar_etiqueta()
    t[0].n_t(find_column(Ts.texto_analisis, t.slice[1]))

    Ts.rp_nuevo_nodo('etiqueta : MAIN ideti  instrucciones', "t[0] = Etiqueta(t[3], t[1])")

def p_instrucciones_lista(t):
    'instrucciones :   instruccionesp '
    t[0] = t[1]

    global Ts
    Ts.rp_nuevo_nodo('instrucciones :   instruccionesp ', "t[0] = t[1]")

def p_instrucciones_lista_sin_recursividad(t):
    'instruccionesp : instruccion instruccionesp'
    t[0] = t[2]
    t[0].lst.insert(0, t[1])
    global Ts
    Ts.nueva_instruaccion(t[1])

    Ts.rp_nuevo_nodo('instruccionesp : instruccion instruccionesp', "t[0] = t[2] \n t[0].lst.insert(0, t[1])")

def p_instrucciones_lista_sin_recursividad_epsilon(t):
    'instruccionesp : '
    t[0] = ABCInstruccion.ListaInstruccion([])

    global Ts
    Ts.rp_nuevo_nodo('instruccionesp : ', "t[0] = ABCInstruccion.ListaInstruccion([])")


def p_instrucciones_exit(t):
    'instruccion :  EXIT PUNTOCOMA'
    t[0] = Exit()

    global Ts
    t[0].n_t(find_column(Ts.texto_analisis, t.slice[1]))

    Ts.rp_nuevo_nodo('instruccion :  EXIT PUNTOCOMA', "t[0] = Exit()")

def p_instrucciones_imprimir(t):
    'instruccion :  IMPRIMIR  PARA expresion PARC PUNTOCOMA'
    t[0] = ABCInstruccion.Imprimir(t[3])

    global Ts
    t[0].n_t(find_column(Ts.texto_analisis, t.slice[1]))

    Ts.rp_nuevo_nodo('instruccion :  IMPRIMIR  PARA expresion PARC PUNTOCOMA', "t[0] = ABCInstruccion.Imprimir(t[3])")


def p_instrucciones_unset(t):
    'instruccion :  UNSET  PARA DOLAR IDENTIFICADOR arra PARC PUNTOCOMA'
    t[0] = Unset(t[4])
    t[0].indices(t[5])

    global Ts
    t[0].n_t(find_column(Ts.texto_analisis, t.slice[1]))
    Ts.rp_nuevo_nodo('instruccion :  UNSET  PARA DOLAR IDENTIFICADOR arra PARC PUNTOCOMA', "t[0] = Unset(t[4])")


def p_instrucciones_asignar(t):
    'instruccion :  DOLAR  IDENTIFICADOR arra IGUAL expresion PUNTOCOMA'
    t[0] = Asignar(t[2], t[5])
    t[0].indices(t[3])

    global Ts
    t[0].n_t(find_column(Ts.texto_analisis, t.slice[1]))

    Ts.rp_nuevo_nodo('instruccion :  DOLAR  IDENTIFICADOR arra IGUAL expresion PUNTOCOMA', "t[0] = Asignar(t[2], t[5])")


def p_arreglo_indice(t):
    'arra : CORA expresion CORC  arra '
    t[0] = t[4]
    t[0].append(t[2])

    global Ts
    Ts.rp_nuevo_nodo('arra : CORA expresion CORC  arra ', "t[0] = t[4]")


def p_arreglo_indice_epsilon(t):
    'arra : '
    t[0] = []

    global Ts
    Ts.rp_nuevo_nodo('arra : ', "t[0] = []")


def p_instrucciones_goto(t):
    'instruccion :  GOTO  IDENTIFICADOR  PUNTOCOMA'
    t[0] = Goto(t[2])

    global Ts
    t[0].n_t(find_column(Ts.texto_analisis, t.slice[1]))

    Ts.rp_nuevo_nodo('instruccion :  GOTO  IDENTIFICADOR  PUNTOCOMA', "t[0] = Goto(t[2])")

def p_instrucciones_if(t):
    'instruccion :  IF   expresion  instruccion  '
    t[0] = If(t[2], t[3])

    global Ts
    t[0].n_t(find_column(Ts.texto_analisis, t.slice[1]))

    Ts.rp_nuevo_nodo('instruccion :  IF   expresion  instruccion  ', "t[0] = If(t[2], t[3])")


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

    global Ts
    t[0].n_t(find_column(Ts.texto_analisis, t.slice[2]))
    Ts.rp_nuevo_nodo('expresion : valor ' + str(t[2]) + ' valor',
                     "t[0] = ABCInstruccion.ExpresionDoble(t[1], t[2], t[3])")


def p_expresion_sola(t):
    'expresion :  valor'
    t[0] = t[1]

    global Ts
    Ts.rp_nuevo_nodo('expresion :  valor', "t[0] = t[1]")


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
    elif t[1] == "&":
        t[0] = Referencia(t[3], t[4])

    else:
        t[0] = ABCInstruccion.ExpresionSimpleOperacion(t[2], t[1])

    global Ts
    t[0].n_t(find_column(Ts.texto_analisis, t.slice[1]))
    Ts.rp_nuevo_nodo('expresion : ' + str(t[1]) + 'valor', "t[0] = ABCInstruccion.ExpresionSimpleOperacion(t[3], t[1])")


def p_expresion_agrupacion(t):
    '''expresion : PARA INT PARC valor
                | PARA FLOAT PARC valor
                | PARA CHAR PARC valor'''

    t[0] = ABCInstruccion.ExpresionSimpleOperacion(t[4], t[2])

    global Ts
    t[0].n_t(find_column(Ts.texto_analisis, t.slice[1]))
    Ts.rp_nuevo_nodo('expresion : PARA' + str(t[2]) + 'PARC valor',
                     "t[0] = ABCInstruccion.ExpresionSimpleOperacion(t[4], t[2])")


def p_expresion_parentesis(t):
    'expresion : PARA expresion PARC'
    t[0] = t[2]

    global Ts
    Ts.rp_nuevo_nodo('expresion : PARA expresion PARC', "t[0] = t[2]")


def p_expresion_entero(t):
    'valor    : ENTERO'
    t[0] = ABCInstruccion.Valor(t[1], 0)
    t[0] = ABCInstruccion.ExpresionSimple(t[0])

    global Ts
    t[0].n_t(find_column(Ts.texto_analisis, t.slice[1]))
    Ts.rp_nuevo_nodo('valor    : ENTERO', "t[0] = ABCInstruccion.Valor(t[1], 0)")


def p_expresion_decimal(t):
    'valor    : DECIMAL'
    t[0] = ABCInstruccion.Valor(t[1], 1)
    t[0] = ABCInstruccion.ExpresionSimple(t[0])

    global Ts
    t[0].n_t(find_column(Ts.texto_analisis, t.slice[1]))
    Ts.rp_nuevo_nodo('valor    : DECIMAL', "t[0] = ABCInstruccion.Valor(t[1], 1)")


def p_expresion_cadena(t):
    'valor    : CADENA'
    t[0] = ABCInstruccion.Valor(t[1], 2)
    t[0] = ABCInstruccion.ExpresionSimple(t[0])

    global Ts
    t[0].n_t(find_column(Ts.texto_analisis, t.slice[1]))
    Ts.rp_nuevo_nodo('valor    : CADENA', "t[0] = ABCInstruccion.Valor(t[1], 2)")


def p_expresion_valor_unico_variable(t):
    'valor    : DOLAR IDENTIFICADOR arra'
    t[0] = VariableValor(t[2])
    t[0].indices(t[3])

    global Ts
    t[0].n_t(find_column(Ts.texto_analisis, t.slice[1]))
    Ts.rp_nuevo_nodo('valor    : DOLAR IDENTIFICADOR arra', "t[0] = VariableValor(t[2])")


def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return ((token.lexpos - line_start) + 1, token.lineno)


def p_error(t):
    global Ts
    if t is None:
        Ts.cargar_error("Se Alcanzo El Fin Del Archivo", 20, (0, 0))
        return
    Ts.exit_exec = 0
    tup = find_column(Ts.texto_analisis, t)
    Ts.cargar_error(
        "El token con lexema \"" + str(t.value) + "\" de tipo \"" + str(t.type) + " \" ocasiono un  error sintactico",
        20, tup)
    print("Error sintáctico en '%s'" % t)

    global parsitode

    while True:
        tok = parsitode.token()  # Get the next token
        if not tok or tok.type == 'PUNTOCOMA':
            break

    tok = parsitode.token()
    parsitode.errok()

parsitode=None

def analizar_descendente(input: str):
    # Construyendo el analizador léxico
    lexer = lex.lex()
    global parsitode
    parsitode = yacc.yacc()
    return parsitode.parse(input)
