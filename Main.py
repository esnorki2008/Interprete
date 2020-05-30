from Contenido.Lexico import *
from Contenido.Sintactico import *
import ply.lex as lex
import ply.yacc as yacc




    
# Construyendo el analizador léxico
lexer = lex.lex()
parser = yacc.yacc()


f = open("C:/Users/Esnorki/Desktop/Parser/entrada.txt", "r")
input = f.read()
print(input)
parser.parse(input)