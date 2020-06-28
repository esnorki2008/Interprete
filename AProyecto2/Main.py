from AProyecto2.Contenido.Analizadores.MinorCSintactico import analizar_ascendente
from AProyecto2.Contenido.TablaDeSimbolos import TablaDeSimbolos

#cadena="int x=0; int a=0; do { a=a+x; x=x+1;  } while(x<4)"









cadena1 = '''
        

       

'''


cadena2='''

'''

cadena3='''



'''

cadena4 = '''
struct punto {
    int x,h;
    int y;
}
int main()
{   
    struct punto hola;
    hola.x=50;
}
'''
def analizar_minor_c_optimizar_3D(cadena_entrada):
    tab = TablaDeSimbolos(None)
    lst_repo_grama = []
    rst=analizar_ascendente(cadena_entrada,lst_repo_grama)
    if rst is None :
        print("Error")
    else:
        #print(rst.str_arbol());
        rst.ejecutar_3D(tab)
        tab.terminar_codigo_3d()
        from AProyecto2.Contenido.Optimo import Optimo
        Optm:Optimo = Optimo(tab.codigo_3d)
        lst_sal = Optm.codigo_optimizado()
        #tab.imprimir_temporales()
        return tab.string_codigo_3d(lst_sal)

def analizar_minor_c(cadena_entrada):
    tab = TablaDeSimbolos(None)
    lst_repo_grama = []
    rst = analizar_ascendente(cadena_entrada, lst_repo_grama)
    if rst is None :
        print("Error")
    else:
        #print(rst.str_arbol());
        rst.ejecutar_3D(tab)
        tab.terminar_codigo_3d()
        #from Contenido.Optimo import Optimo
        #Optm:Optimo = Optimo(tab.codigo_3d)
        #lst_sal = Optm.codigo_optimizado()
        return tab.string_codigo_3d(tab.codigo_3d)


    #print(tab.codigo_3d)
    #tab.imprimir_temporales()


