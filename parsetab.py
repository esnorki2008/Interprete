
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftMASMENOSleftPORDIVIDIDOrightUMENOSCORA CORC DECIMAL DIVIDIDO ENTERO IMPRIMIR MAS MENOS PARA PARC POR PUNTOCOMAinicio    : instruccionesinstrucciones : instrucciones instruccioninstrucciones : instruccioninstruccion :  expresion  PUNTOCOMAinstruccion :  IMPRIMIR PARA expresion PARC PUNTOCOMAexpresion : expresion MAS expresion\n                  | expresion MENOS expresion\n                  | expresion POR expresion\n                  | expresion DIVIDIDO expresionexpresion : MENOS expresion %prec UMENOSexpresion : PARA expresion PARCexpresion    : ENTEROexpresion    : DECIMAL'
    
_lr_action_items = {'IMPRIMIR':([0,2,3,10,11,26,],[5,5,-3,-2,-4,-5,]),'MENOS':([0,2,3,4,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,26,],[7,7,-3,13,7,7,-12,-13,-2,-4,7,7,7,7,7,13,-10,-6,-7,-8,-9,13,-11,-5,]),'PARA':([0,2,3,5,6,7,10,11,12,13,14,15,16,26,],[6,6,-3,16,6,6,-2,-4,6,6,6,6,6,-5,]),'ENTERO':([0,2,3,6,7,10,11,12,13,14,15,16,26,],[8,8,-3,8,8,-2,-4,8,8,8,8,8,-5,]),'DECIMAL':([0,2,3,6,7,10,11,12,13,14,15,16,26,],[9,9,-3,9,9,-2,-4,9,9,9,9,9,-5,]),'$end':([1,2,3,10,11,26,],[0,-1,-3,-2,-4,-5,]),'PUNTOCOMA':([4,8,9,18,19,20,21,22,24,25,],[11,-12,-13,-10,-6,-7,-8,-9,-11,26,]),'MAS':([4,8,9,17,18,19,20,21,22,23,24,],[12,-12,-13,12,-10,-6,-7,-8,-9,12,-11,]),'POR':([4,8,9,17,18,19,20,21,22,23,24,],[14,-12,-13,14,-10,14,14,-8,-9,14,-11,]),'DIVIDIDO':([4,8,9,17,18,19,20,21,22,23,24,],[15,-12,-13,15,-10,15,15,-8,-9,15,-11,]),'PARC':([8,9,17,18,19,20,21,22,23,24,],[-12,-13,24,-10,-6,-7,-8,-9,25,-11,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'inicio':([0,],[1,]),'instrucciones':([0,],[2,]),'instruccion':([0,2,],[3,10,]),'expresion':([0,2,6,7,12,13,14,15,16,],[4,4,17,18,19,20,21,22,23,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> inicio","S'",1,None,None,None),
  ('inicio -> instrucciones','inicio',1,'p_inicio','Sintactico.py',13),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones_lista','Sintactico.py',18),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_lista_inicio','Sintactico.py',24),
  ('instruccion -> expresion PUNTOCOMA','instruccion',2,'p_instrucciones_evaluar','Sintactico.py',29),
  ('instruccion -> IMPRIMIR PARA expresion PARC PUNTOCOMA','instruccion',5,'p_instrucciones_imprimir','Sintactico.py',34),
  ('expresion -> expresion MAS expresion','expresion',3,'p_expresion_binaria','Sintactico.py',38),
  ('expresion -> expresion MENOS expresion','expresion',3,'p_expresion_binaria','Sintactico.py',39),
  ('expresion -> expresion POR expresion','expresion',3,'p_expresion_binaria','Sintactico.py',40),
  ('expresion -> expresion DIVIDIDO expresion','expresion',3,'p_expresion_binaria','Sintactico.py',41),
  ('expresion -> MENOS expresion','expresion',2,'p_expresion_unaria','Sintactico.py',53),
  ('expresion -> PARA expresion PARC','expresion',3,'p_expresion_agrupacion','Sintactico.py',58),
  ('expresion -> ENTERO','expresion',1,'p_expresion_entero','Sintactico.py',63),
  ('expresion -> DECIMAL','expresion',1,'p_expresion_decimal','Sintactico.py',69),
]
