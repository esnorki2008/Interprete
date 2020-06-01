
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftMASMENOSleftPORDIVIDIDOrightUMENOSCORA CORC DECIMAL DIVIDIDO DOBLEPUNTO DOLAR ENTERO EXIT GOTO IDENTIFICADOR IGUAL IMPRIMIR MAIN MAS MENOS PARA PARC POR PUNTOCOMA READ UNSETinicio    : etiquetasetiquetas : etiquetas etiquetaetiquetas : etiquetaetiqueta : IDENTIFICADOR DOBLEPUNTO instruccionesetiqueta : MAIN DOBLEPUNTO instruccionesinstrucciones :  instrucciones instruccion instrucciones : instruccion instruccion :  EXIT PUNTOCOMAinstruccion :  IMPRIMIR  PARA expresion PARC PUNTOCOMAinstruccion :  DOLAR  IDENTIFICADOR IGUAL expresion PUNTOCOMAinstruccion :  GOTO  IDENTIFICADOR  PUNTOCOMAexpresion : valor MAS valor\n                  | valor MENOS valor\n                  | valor POR valor\n                  | valor DIVIDIDO valorexpresion :  valorexpresion : MENOS valor %prec UMENOSexpresion : PARA valor PARCvalor    : ENTEROvalor    : DOLAR IDENTIFICADOR'
    
_lr_action_items = {'IDENTIFICADOR':([0,2,3,6,9,10,13,14,15,16,17,26,28,39,44,],[4,4,-3,-2,-4,-7,19,20,-5,-6,-8,36,-11,-9,-10,]),'MAIN':([0,2,3,6,9,10,15,16,17,28,39,44,],[5,5,-3,-2,-4,-7,-5,-6,-8,-11,-9,-10,]),'$end':([1,2,3,6,9,10,15,16,17,28,39,44,],[0,-1,-3,-2,-4,-7,-5,-6,-8,-11,-9,-10,]),'DOBLEPUNTO':([4,5,],[7,8,]),'EXIT':([7,8,9,10,15,16,17,28,39,44,],[11,11,11,-7,11,-6,-8,-11,-9,-10,]),'IMPRIMIR':([7,8,9,10,15,16,17,28,39,44,],[12,12,12,-7,12,-6,-8,-11,-9,-10,]),'DOLAR':([7,8,9,10,15,16,17,18,21,24,27,28,31,32,33,34,39,44,],[13,13,13,-7,13,-6,-8,26,26,26,26,-11,26,26,26,26,-9,-10,]),'GOTO':([7,8,9,10,15,16,17,28,39,44,],[14,14,14,-7,14,-6,-8,-11,-9,-10,]),'PUNTOCOMA':([11,20,23,25,30,35,36,37,38,40,41,42,43,],[17,28,-16,-19,39,-17,-20,44,-18,-12,-13,-14,-15,]),'PARA':([12,18,27,],[18,21,21,]),'MENOS':([18,23,25,27,36,],[24,32,-19,24,-20,]),'ENTERO':([18,21,24,27,31,32,33,34,],[25,25,25,25,25,25,25,25,]),'IGUAL':([19,],[27,]),'PARC':([22,23,25,29,35,36,38,40,41,42,43,],[30,-16,-19,38,-17,-20,-18,-12,-13,-14,-15,]),'MAS':([23,25,36,],[31,-19,-20,]),'POR':([23,25,36,],[33,-19,-20,]),'DIVIDIDO':([23,25,36,],[34,-19,-20,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'inicio':([0,],[1,]),'etiquetas':([0,],[2,]),'etiqueta':([0,2,],[3,6,]),'instrucciones':([7,8,],[9,15,]),'instruccion':([7,8,9,15,],[10,10,16,16,]),'expresion':([18,27,],[22,37,]),'valor':([18,21,24,27,31,32,33,34,],[23,29,35,23,40,41,42,43,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> inicio","S'",1,None,None,None),
  ('inicio -> etiquetas','inicio',1,'p_inicio','Sintactico.py',13),
  ('etiquetas -> etiquetas etiqueta','etiquetas',2,'p_etiquetas_lista','Sintactico.py',17),
  ('etiquetas -> etiqueta','etiquetas',1,'p_etiquetas_lista_inicio','Sintactico.py',21),
  ('etiqueta -> IDENTIFICADOR DOBLEPUNTO instrucciones','etiqueta',3,'p_etiqueta_contenido','Sintactico.py',25),
  ('etiqueta -> MAIN DOBLEPUNTO instrucciones','etiqueta',3,'p_etiqueta_principal','Sintactico.py',29),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones_lista','Sintactico.py',33),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_lista_inicio','Sintactico.py',39),
  ('instruccion -> EXIT PUNTOCOMA','instruccion',2,'p_instrucciones_exit','Sintactico.py',45),
  ('instruccion -> IMPRIMIR PARA expresion PARC PUNTOCOMA','instruccion',5,'p_instrucciones_imprimir','Sintactico.py',49),
  ('instruccion -> DOLAR IDENTIFICADOR IGUAL expresion PUNTOCOMA','instruccion',5,'p_instrucciones_asignar','Sintactico.py',53),
  ('instruccion -> GOTO IDENTIFICADOR PUNTOCOMA','instruccion',3,'p_instrucciones_goto','Sintactico.py',57),
  ('expresion -> valor MAS valor','expresion',3,'p_expresion_binaria','Sintactico.py',61),
  ('expresion -> valor MENOS valor','expresion',3,'p_expresion_binaria','Sintactico.py',62),
  ('expresion -> valor POR valor','expresion',3,'p_expresion_binaria','Sintactico.py',63),
  ('expresion -> valor DIVIDIDO valor','expresion',3,'p_expresion_binaria','Sintactico.py',64),
  ('expresion -> valor','expresion',1,'p_expresion_sola','Sintactico.py',75),
  ('expresion -> MENOS valor','expresion',2,'p_expresion_unaria','Sintactico.py',79),
  ('expresion -> PARA valor PARC','expresion',3,'p_expresion_agrupacion','Sintactico.py',84),
  ('valor -> ENTERO','valor',1,'p_expresion_entero','Sintactico.py',89),
  ('valor -> DOLAR IDENTIFICADOR','valor',2,'p_expresion_decimal','Sintactico.py',100),
]
