from Contenido.Lexico import *
from Contenido.Sintactico import *
import ply.lex as lex
import ply.yacc as yacc




    
# Construyendo el analizador léxico
lexer = lex.lex()
parser = yacc.yacc()


#f = open("C:/Users/norki/Desktop/interprete/entrada.txt", "r")
f = open("C:/Users/Esnorki/Desktop/interprete/entrada.txt", "r")
input: str = f.read()
#print(input)
raiz_produccion = parser.parse(input)
for Prod in raiz_produccion:
    print(Prod.ejecutar().dar_valor())
