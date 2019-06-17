
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'programrightassignleftNOTnonassoclessless_equalequalleftplusminusleftstardivrightISVOIDrightcomplementleftdotwhite_space comma semicolon obracket cbracket ocurly ccurly assign plus minus star div printx scanx idx string complement number less less_equal equal case_expr arrobe dot doubledot CLASS LET LOOP INHERITS POOL IF THEN ELSE FI WHILE CASE OF ESAC NEW NOT TRUE FALSE ISVOID INempty :binary_operator : v_expr plus v_expr\n                    | v_expr minus v_expr\n                | v_expr star v_expr\n            | v_expr div v_exprprogram : class_expresion semicolon program_aprogram_a : class_expresion semicolon program_a\n\t\t    | emptyneg : NOT exprcompl : complement exprassign_expresion : idx assign exprdeclare_expresion : idx doubledot idx assign expr\n    \t\t\t\t| idx doubledot idxdeclare_method : idx doubledot idxnew_expresion : NEW idxclass_expresion : CLASS idx ocurly feature\n\t\t  | CLASS idx INHERITS idx ocurly featurefeature : method_decl feature\n                | property_decl feature\n\t\t\t\t| ccurlymethod_decl : idx obracket formal cbracket doubledot idx ocurly expr ccurly semicolon formal : declare_method formal_a\n                | empty formal_a : comma declare_method formal_a\n                | emptyexpr : assign_expresion\n            | while_expresion\n            | v_exprcomparison_expresion : v_expr less v_expr\n                            | v_expr less_equal v_expr\n                            | v_expr equal v_exprv_expr : conditional_expresion\n            | let_expresion\n            | case_expresion\n            | dispatch_expresion\n            | dispatch_instance\n            | block_expresion\n            | binary_operator\n            | neg\n            | compl\n            | is_void\n            | new_expresion\n            | term\n            | comparison_expresionterm : var\n            | num\n            | str\n            | bool\n            | negnum\n            | obracket v_expr cbracketvar : idxnum : numbernegnum : minus termstr : stringbool : TRUE\n            | FALSEblock_expresion : ocurly block_expr ccurlyblock_expr : expr semicolon block_expr_ablock_expr_a : expr semicolon block_expr_a\n                    | emptyproperty_decl : declare_expresion semicolonconditional_expresion : IF v_expr THEN expr ELSE expr FIis_void : ISVOID exprwhile_expresion : WHILE v_expr LOOP expr POOLcase_expresion : CASE expr OF case_list ESACcase_list : declare_method case_expr expr semicolon case_list_acase_list_a : declare_method case_expr expr semicolon case_list_a\n                | emptylet_expresion : LET let_declr_list IN exprlet_declr_list : declare_expresion let_declr_list_alet_declr_list_a : comma declare_expresion let_declr_list_a\n                        | emptydispatch_expresion : idx obracket dispatch_p_list cbracket dispatch_instance : v_expr dot idx obracket dispatch_p_list cbracket\n                        | v_expr arrobe idx dot idx obracket dispatch_p_list cbracket dispatch_p_list : v_expr dispatch_p_list_a\n                    | emptydispatch_p_list_a : comma v_expr dispatch_p_list_a\n                    | empty'
    
_lr_action_items = {'CLASS':([0,4,11,],[3,3,3,]),'$end':([1,4,7,8,11,19,],[0,-1,-6,-8,-1,-7,]),'semicolon':([2,6,13,16,17,22,23,30,31,41,42,43,44,45,47,48,49,50,51,52,53,54,55,56,57,58,59,70,71,72,73,74,75,76,77,78,93,101,102,103,104,105,106,107,109,115,116,117,118,119,120,121,129,130,133,141,145,148,152,155,160,163,166,168,173,],[4,11,-16,-20,24,-18,-19,-13,-17,-51,-12,-26,-27,-28,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-52,-54,-55,-56,-51,131,-53,-51,-9,-10,-63,-15,-11,-2,-3,-4,-5,-29,-30,-31,-50,-57,-73,-69,157,158,-64,-65,-74,167,-62,-75,174,]),'idx':([3,9,10,14,15,20,21,24,25,32,35,37,39,46,60,61,62,63,64,65,66,67,68,69,81,82,83,84,85,86,87,88,89,90,91,108,122,123,124,126,128,131,135,137,138,153,156,157,158,161,167,172,174,],[5,12,18,12,12,26,30,-61,12,38,26,41,79,93,93,97,41,93,41,103,41,41,41,107,41,93,113,114,93,93,93,93,93,93,93,41,41,41,41,97,26,41,93,93,151,41,41,41,-21,93,26,41,26,]),'ocurly':([5,18,37,46,60,62,63,64,66,67,68,79,81,82,85,86,87,88,89,90,91,108,122,123,124,131,135,137,153,156,157,161,172,],[9,25,64,64,64,64,64,64,64,64,64,108,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,]),'INHERITS':([5,],[10,]),'ccurly':([9,14,15,24,25,41,43,44,45,47,48,49,50,51,52,53,54,55,56,57,58,59,70,71,72,73,74,75,76,77,78,93,100,102,103,104,105,106,107,109,115,116,117,118,119,120,121,129,130,131,132,133,141,146,147,152,155,157,158,160,164,166,168,],[16,16,16,-61,16,-51,-26,-27,-28,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-52,-54,-55,-56,-51,130,-53,-51,-9,-10,-63,-15,-11,-2,-3,-4,-5,-29,-30,-31,-50,-57,-1,148,-73,-69,-58,-60,-64,-65,-1,-21,-74,-59,-62,-75,]),'obracket':([12,37,41,46,60,62,63,64,65,66,67,68,81,82,85,86,87,88,89,90,91,93,108,113,122,123,124,131,135,137,151,153,156,157,161,172,],[20,63,82,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,82,63,137,63,63,63,63,63,63,161,63,63,63,63,63,]),'doubledot':([12,26,33,97,],[21,32,39,21,]),'cbracket':([20,27,28,29,34,36,38,40,41,43,44,45,47,48,49,50,51,52,53,54,55,56,57,58,59,70,71,72,73,74,75,76,77,78,80,82,93,99,102,103,104,105,106,107,109,110,111,112,115,116,117,118,119,120,121,129,130,133,134,136,137,141,149,150,152,155,159,160,161,165,166,168,],[-1,33,-1,-23,-22,-25,-14,-1,-51,-26,-27,-28,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-52,-54,-55,-56,-24,-1,-51,129,-53,-51,-9,-10,-63,-15,-11,133,-1,-77,-2,-3,-4,-5,-29,-30,-31,-50,-57,-73,-76,-79,-1,-69,-1,160,-64,-65,-78,-74,-1,168,-62,-75,]),'comma':([28,30,38,40,41,42,43,44,45,47,48,49,50,51,52,53,54,55,56,57,58,59,70,71,72,73,74,75,76,77,78,93,96,102,103,104,105,106,107,109,111,115,116,117,118,119,120,121,129,130,133,141,142,149,152,155,160,166,168,],[35,-13,-14,35,-51,-12,-26,-27,-28,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-52,-54,-55,-56,-51,126,-53,-51,-9,-10,-63,-15,-11,135,-2,-3,-4,-5,-29,-30,-31,-50,-57,-73,-69,126,135,-64,-65,-74,-62,-75,]),'assign':([30,41,],[37,81,]),'IN':([30,41,42,43,44,45,47,48,49,50,51,52,53,54,55,56,57,58,59,70,71,72,73,74,75,76,77,78,93,95,96,102,103,104,105,106,107,109,115,116,117,118,119,120,121,125,127,129,130,133,141,142,152,154,155,160,166,168,],[-13,-51,-12,-26,-27,-28,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-52,-54,-55,-56,-51,124,-1,-53,-51,-9,-10,-63,-15,-11,-2,-3,-4,-5,-29,-30,-31,-70,-72,-50,-57,-73,-69,-1,-64,-71,-65,-74,-62,-75,]),'WHILE':([37,62,64,66,67,68,81,108,122,123,124,131,153,156,157,172,],[46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'IF':([37,46,60,62,63,64,66,67,68,81,82,85,86,87,88,89,90,91,108,122,123,124,131,135,137,153,156,157,161,172,],[60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,]),'LET':([37,46,60,62,63,64,66,67,68,81,82,85,86,87,88,89,90,91,108,122,123,124,131,135,137,153,156,157,161,172,],[61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,]),'CASE':([37,46,60,62,63,64,66,67,68,81,82,85,86,87,88,89,90,91,108,122,123,124,131,135,137,153,156,157,161,172,],[62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,]),'NOT':([37,46,60,62,63,64,66,67,68,81,82,85,86,87,88,89,90,91,108,122,123,124,131,135,137,153,156,157,161,172,],[66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,]),'complement':([37,46,60,62,63,64,66,67,68,81,82,85,86,87,88,89,90,91,108,122,123,124,131,135,137,153,156,157,161,172,],[67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,]),'ISVOID':([37,46,60,62,63,64,66,67,68,81,82,85,86,87,88,89,90,91,108,122,123,124,131,135,137,153,156,157,161,172,],[68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,]),'NEW':([37,46,60,62,63,64,66,67,68,81,82,85,86,87,88,89,90,91,108,122,123,124,131,135,137,153,156,157,161,172,],[69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,]),'number':([37,46,60,62,63,64,65,66,67,68,81,82,85,86,87,88,89,90,91,108,122,123,124,131,135,137,153,156,157,161,172,],[75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,]),'string':([37,46,60,62,63,64,65,66,67,68,81,82,85,86,87,88,89,90,91,108,122,123,124,131,135,137,153,156,157,161,172,],[76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,]),'TRUE':([37,46,60,62,63,64,65,66,67,68,81,82,85,86,87,88,89,90,91,108,122,123,124,131,135,137,153,156,157,161,172,],[77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,]),'FALSE':([37,46,60,62,63,64,65,66,67,68,81,82,85,86,87,88,89,90,91,108,122,123,124,131,135,137,153,156,157,161,172,],[78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,]),'minus':([37,41,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,62,63,64,65,66,67,68,70,71,72,73,74,75,76,77,78,81,82,85,86,87,88,89,90,91,92,93,94,99,102,103,104,105,106,107,108,109,111,115,116,117,118,119,120,121,122,123,124,129,130,131,133,135,137,141,149,152,153,155,156,157,160,161,166,168,172,],[65,-51,-26,-27,86,65,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,65,65,65,65,65,65,65,65,-45,-46,-47,-48,-49,-52,-54,-55,-56,65,65,65,65,65,65,65,65,65,86,-51,86,86,-53,-51,-9,-10,-63,-15,65,-11,86,-2,-3,-4,-5,86,86,86,65,65,65,-50,-57,65,-73,65,65,-69,86,-64,65,-65,65,65,-74,65,-62,-75,65,]),'case_expr':([38,144,169,],[-14,156,172,]),'dot':([41,43,44,45,47,48,49,50,51,52,53,54,55,56,57,58,59,70,71,72,73,74,75,76,77,78,92,93,94,99,102,103,104,105,106,107,109,111,114,115,116,117,118,119,120,121,129,130,133,141,149,152,155,160,166,168,],[-51,-26,-27,83,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-52,-54,-55,-56,83,-51,83,83,-53,-51,-9,-10,-63,-15,-11,83,138,83,83,83,83,83,83,83,-50,-57,-73,-69,83,-64,-65,-74,-62,-75,]),'arrobe':([41,43,44,45,47,48,49,50,51,52,53,54,55,56,57,58,59,70,71,72,73,74,75,76,77,78,92,93,94,99,102,103,104,105,106,107,109,111,115,116,117,118,119,120,121,129,130,133,141,149,152,155,160,166,168,],[-51,-26,-27,84,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-52,-54,-55,-56,84,-51,84,84,-53,-51,-9,-10,-63,-15,-11,84,-2,-3,-4,-5,-29,-30,-31,-50,-57,-73,-69,84,-64,-65,-74,-62,-75,]),'plus':([41,43,44,45,47,48,49,50,51,52,53,54,55,56,57,58,59,70,71,72,73,74,75,76,77,78,92,93,94,99,102,103,104,105,106,107,109,111,115,116,117,118,119,120,121,129,130,133,141,149,152,155,160,166,168,],[-51,-26,-27,85,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-52,-54,-55,-56,85,-51,85,85,-53,-51,-9,-10,-63,-15,-11,85,-2,-3,-4,-5,85,85,85,-50,-57,-73,-69,85,-64,-65,-74,-62,-75,]),'star':([41,43,44,45,47,48,49,50,51,52,53,54,55,56,57,58,59,70,71,72,73,74,75,76,77,78,92,93,94,99,102,103,104,105,106,107,109,111,115,116,117,118,119,120,121,129,130,133,141,149,152,155,160,166,168,],[-51,-26,-27,87,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-52,-54,-55,-56,87,-51,87,87,-53,-51,-9,-10,-63,-15,-11,87,87,87,-4,-5,87,87,87,-50,-57,-73,-69,87,-64,-65,-74,-62,-75,]),'div':([41,43,44,45,47,48,49,50,51,52,53,54,55,56,57,58,59,70,71,72,73,74,75,76,77,78,92,93,94,99,102,103,104,105,106,107,109,111,115,116,117,118,119,120,121,129,130,133,141,149,152,155,160,166,168,],[-51,-26,-27,88,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-52,-54,-55,-56,88,-51,88,88,-53,-51,-9,-10,-63,-15,-11,88,88,88,-4,-5,88,88,88,-50,-57,-73,-69,88,-64,-65,-74,-62,-75,]),'less':([41,43,44,45,47,48,49,50,51,52,53,54,55,56,57,58,59,70,71,72,73,74,75,76,77,78,92,93,94,99,102,103,104,105,106,107,109,111,115,116,117,118,119,120,121,129,130,133,141,149,152,155,160,166,168,],[-51,-26,-27,89,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-52,-54,-55,-56,89,-51,89,89,-53,-51,-9,-10,-63,-15,-11,89,-2,-3,-4,-5,None,None,None,-50,-57,-73,-69,89,-64,-65,-74,-62,-75,]),'less_equal':([41,43,44,45,47,48,49,50,51,52,53,54,55,56,57,58,59,70,71,72,73,74,75,76,77,78,92,93,94,99,102,103,104,105,106,107,109,111,115,116,117,118,119,120,121,129,130,133,141,149,152,155,160,166,168,],[-51,-26,-27,90,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-52,-54,-55,-56,90,-51,90,90,-53,-51,-9,-10,-63,-15,-11,90,-2,-3,-4,-5,None,None,None,-50,-57,-73,-69,90,-64,-65,-74,-62,-75,]),'equal':([41,43,44,45,47,48,49,50,51,52,53,54,55,56,57,58,59,70,71,72,73,74,75,76,77,78,92,93,94,99,102,103,104,105,106,107,109,111,115,116,117,118,119,120,121,129,130,133,141,149,152,155,160,166,168,],[-51,-26,-27,91,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-52,-54,-55,-56,91,-51,91,91,-53,-51,-9,-10,-63,-15,-11,91,-2,-3,-4,-5,None,None,None,-50,-57,-73,-69,91,-64,-65,-74,-62,-75,]),'OF':([41,43,44,45,47,48,49,50,51,52,53,54,55,56,57,58,59,70,71,72,73,74,75,76,77,78,93,98,102,103,104,105,106,107,109,115,116,117,118,119,120,121,129,130,133,141,152,155,160,166,168,],[-51,-26,-27,-28,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-52,-54,-55,-56,-51,128,-53,-51,-9,-10,-63,-15,-11,-2,-3,-4,-5,-29,-30,-31,-50,-57,-73,-69,-64,-65,-74,-62,-75,]),'LOOP':([41,43,44,45,47,48,49,50,51,52,53,54,55,56,57,58,59,70,71,72,73,74,75,76,77,78,92,93,102,103,104,105,106,107,109,115,116,117,118,119,120,121,129,130,133,141,152,155,160,166,168,],[-51,-26,-27,-28,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-52,-54,-55,-56,122,-51,-53,-51,-9,-10,-63,-15,-11,-2,-3,-4,-5,-29,-30,-31,-50,-57,-73,-69,-64,-65,-74,-62,-75,]),'THEN':([41,43,44,45,47,48,49,50,51,52,53,54,55,56,57,58,59,70,71,72,73,74,75,76,77,78,93,94,102,103,104,105,106,107,109,115,116,117,118,119,120,121,129,130,133,141,152,155,160,166,168,],[-51,-26,-27,-28,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-52,-54,-55,-56,-51,123,-53,-51,-9,-10,-63,-15,-11,-2,-3,-4,-5,-29,-30,-31,-50,-57,-73,-69,-64,-65,-74,-62,-75,]),'POOL':([41,43,44,45,47,48,49,50,51,52,53,54,55,56,57,58,59,70,71,72,73,74,75,76,77,78,93,102,103,104,105,106,107,109,115,116,117,118,119,120,121,129,130,133,139,141,152,155,160,166,168,],[-51,-26,-27,-28,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-52,-54,-55,-56,-51,-53,-51,-9,-10,-63,-15,-11,-2,-3,-4,-5,-29,-30,-31,-50,-57,-73,152,-69,-64,-65,-74,-62,-75,]),'ELSE':([41,43,44,45,47,48,49,50,51,52,53,54,55,56,57,58,59,70,71,72,73,74,75,76,77,78,93,102,103,104,105,106,107,109,115,116,117,118,119,120,121,129,130,133,140,141,152,155,160,166,168,],[-51,-26,-27,-28,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-52,-54,-55,-56,-51,-53,-51,-9,-10,-63,-15,-11,-2,-3,-4,-5,-29,-30,-31,-50,-57,-73,153,-69,-64,-65,-74,-62,-75,]),'FI':([41,43,44,45,47,48,49,50,51,52,53,54,55,56,57,58,59,70,71,72,73,74,75,76,77,78,93,102,103,104,105,106,107,109,115,116,117,118,119,120,121,129,130,133,141,152,155,160,162,166,168,],[-51,-26,-27,-28,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-52,-54,-55,-56,-51,-53,-51,-9,-10,-63,-15,-11,-2,-3,-4,-5,-29,-30,-31,-50,-57,-73,-69,-64,-65,-74,166,-62,-75,]),'ESAC':([143,167,170,171,174,175,],[155,-1,-66,-68,-1,-67,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'class_expresion':([0,4,11,],[2,6,6,]),'program_a':([4,11,],[7,19,]),'empty':([4,11,20,28,40,82,96,111,131,137,142,149,157,161,167,174,],[8,8,29,36,36,112,127,136,147,112,127,136,147,112,171,171,]),'feature':([9,14,15,25,],[13,22,23,31,]),'method_decl':([9,14,15,25,],[14,14,14,14,]),'property_decl':([9,14,15,25,],[15,15,15,15,]),'declare_expresion':([9,14,15,25,61,126,],[17,17,17,17,96,142,]),'formal':([20,],[27,]),'declare_method':([20,35,128,167,174,],[28,40,144,169,169,]),'formal_a':([28,40,],[34,80,]),'expr':([37,62,64,66,67,68,81,108,122,123,124,131,153,156,157,172,],[42,98,101,104,105,106,109,132,139,140,141,145,162,163,145,173,]),'assign_expresion':([37,62,64,66,67,68,81,108,122,123,124,131,153,156,157,172,],[43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'while_expresion':([37,62,64,66,67,68,81,108,122,123,124,131,153,156,157,172,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'v_expr':([37,46,60,62,63,64,66,67,68,81,82,85,86,87,88,89,90,91,108,122,123,124,131,135,137,153,156,157,161,172,],[45,92,94,45,99,45,45,45,45,45,111,115,116,117,118,119,120,121,45,45,45,45,45,149,111,45,45,45,111,45,]),'conditional_expresion':([37,46,60,62,63,64,66,67,68,81,82,85,86,87,88,89,90,91,108,122,123,124,131,135,137,153,156,157,161,172,],[47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'let_expresion':([37,46,60,62,63,64,66,67,68,81,82,85,86,87,88,89,90,91,108,122,123,124,131,135,137,153,156,157,161,172,],[48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,]),'case_expresion':([37,46,60,62,63,64,66,67,68,81,82,85,86,87,88,89,90,91,108,122,123,124,131,135,137,153,156,157,161,172,],[49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,]),'dispatch_expresion':([37,46,60,62,63,64,66,67,68,81,82,85,86,87,88,89,90,91,108,122,123,124,131,135,137,153,156,157,161,172,],[50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,]),'dispatch_instance':([37,46,60,62,63,64,66,67,68,81,82,85,86,87,88,89,90,91,108,122,123,124,131,135,137,153,156,157,161,172,],[51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,]),'block_expresion':([37,46,60,62,63,64,66,67,68,81,82,85,86,87,88,89,90,91,108,122,123,124,131,135,137,153,156,157,161,172,],[52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,]),'binary_operator':([37,46,60,62,63,64,66,67,68,81,82,85,86,87,88,89,90,91,108,122,123,124,131,135,137,153,156,157,161,172,],[53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),'neg':([37,46,60,62,63,64,66,67,68,81,82,85,86,87,88,89,90,91,108,122,123,124,131,135,137,153,156,157,161,172,],[54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,]),'compl':([37,46,60,62,63,64,66,67,68,81,82,85,86,87,88,89,90,91,108,122,123,124,131,135,137,153,156,157,161,172,],[55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,]),'is_void':([37,46,60,62,63,64,66,67,68,81,82,85,86,87,88,89,90,91,108,122,123,124,131,135,137,153,156,157,161,172,],[56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,]),'new_expresion':([37,46,60,62,63,64,66,67,68,81,82,85,86,87,88,89,90,91,108,122,123,124,131,135,137,153,156,157,161,172,],[57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,]),'term':([37,46,60,62,63,64,65,66,67,68,81,82,85,86,87,88,89,90,91,108,122,123,124,131,135,137,153,156,157,161,172,],[58,58,58,58,58,58,102,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,]),'comparison_expresion':([37,46,60,62,63,64,66,67,68,81,82,85,86,87,88,89,90,91,108,122,123,124,131,135,137,153,156,157,161,172,],[59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,]),'var':([37,46,60,62,63,64,65,66,67,68,81,82,85,86,87,88,89,90,91,108,122,123,124,131,135,137,153,156,157,161,172,],[70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,]),'num':([37,46,60,62,63,64,65,66,67,68,81,82,85,86,87,88,89,90,91,108,122,123,124,131,135,137,153,156,157,161,172,],[71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,]),'str':([37,46,60,62,63,64,65,66,67,68,81,82,85,86,87,88,89,90,91,108,122,123,124,131,135,137,153,156,157,161,172,],[72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,]),'bool':([37,46,60,62,63,64,65,66,67,68,81,82,85,86,87,88,89,90,91,108,122,123,124,131,135,137,153,156,157,161,172,],[73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,]),'negnum':([37,46,60,62,63,64,65,66,67,68,81,82,85,86,87,88,89,90,91,108,122,123,124,131,135,137,153,156,157,161,172,],[74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,]),'let_declr_list':([61,],[95,]),'block_expr':([64,],[100,]),'dispatch_p_list':([82,137,161,],[110,150,165,]),'let_declr_list_a':([96,142,],[125,154,]),'dispatch_p_list_a':([111,149,],[134,159,]),'case_list':([128,],[143,]),'block_expr_a':([131,157,],[146,164,]),'case_list_a':([167,174,],[170,175,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('empty -> <empty>','empty',0,'p_empty','main.py',98),
  ('binary_operator -> v_expr plus v_expr','binary_operator',3,'p_binary_operator','main.py',103),
  ('binary_operator -> v_expr minus v_expr','binary_operator',3,'p_binary_operator','main.py',104),
  ('binary_operator -> v_expr star v_expr','binary_operator',3,'p_binary_operator','main.py',105),
  ('binary_operator -> v_expr div v_expr','binary_operator',3,'p_binary_operator','main.py',106),
  ('program -> class_expresion semicolon program_a','program',3,'p_program','main.py',118),
  ('program_a -> class_expresion semicolon program_a','program_a',3,'p_program_a','main.py',123),
  ('program_a -> empty','program_a',1,'p_program_a','main.py',124),
  ('neg -> NOT expr','neg',2,'p_neg','main.py',132),
  ('compl -> complement expr','compl',2,'p_compl','main.py',137),
  ('assign_expresion -> idx assign expr','assign_expresion',3,'p_assign_expresion','main.py',142),
  ('declare_expresion -> idx doubledot idx assign expr','declare_expresion',5,'p_declare_expresion','main.py',147),
  ('declare_expresion -> idx doubledot idx','declare_expresion',3,'p_declare_expresion','main.py',148),
  ('declare_method -> idx doubledot idx','declare_method',3,'p_declare_method','main.py',156),
  ('new_expresion -> NEW idx','new_expresion',2,'p_new_expresion','main.py',161),
  ('class_expresion -> CLASS idx ocurly feature','class_expresion',4,'p_class_expresion','main.py',166),
  ('class_expresion -> CLASS idx INHERITS idx ocurly feature','class_expresion',6,'p_class_expresion','main.py',167),
  ('feature -> method_decl feature','feature',2,'p_feature','main.py',175),
  ('feature -> property_decl feature','feature',2,'p_feature','main.py',176),
  ('feature -> ccurly','feature',1,'p_feature','main.py',177),
  ('method_decl -> idx obracket formal cbracket doubledot idx ocurly expr ccurly semicolon','method_decl',10,'p_method_decl','main.py',184),
  ('formal -> declare_method formal_a','formal',2,'p_formal','main.py',189),
  ('formal -> empty','formal',1,'p_formal','main.py',190),
  ('formal_a -> comma declare_method formal_a','formal_a',3,'p_formal_a','main.py',198),
  ('formal_a -> empty','formal_a',1,'p_formal_a','main.py',199),
  ('expr -> assign_expresion','expr',1,'p_expr','main.py',206),
  ('expr -> while_expresion','expr',1,'p_expr','main.py',207),
  ('expr -> v_expr','expr',1,'p_expr','main.py',208),
  ('comparison_expresion -> v_expr less v_expr','comparison_expresion',3,'p_comparison_expresion','main.py',213),
  ('comparison_expresion -> v_expr less_equal v_expr','comparison_expresion',3,'p_comparison_expresion','main.py',214),
  ('comparison_expresion -> v_expr equal v_expr','comparison_expresion',3,'p_comparison_expresion','main.py',215),
  ('v_expr -> conditional_expresion','v_expr',1,'p_v_expr','main.py',225),
  ('v_expr -> let_expresion','v_expr',1,'p_v_expr','main.py',226),
  ('v_expr -> case_expresion','v_expr',1,'p_v_expr','main.py',227),
  ('v_expr -> dispatch_expresion','v_expr',1,'p_v_expr','main.py',228),
  ('v_expr -> dispatch_instance','v_expr',1,'p_v_expr','main.py',229),
  ('v_expr -> block_expresion','v_expr',1,'p_v_expr','main.py',230),
  ('v_expr -> binary_operator','v_expr',1,'p_v_expr','main.py',231),
  ('v_expr -> neg','v_expr',1,'p_v_expr','main.py',232),
  ('v_expr -> compl','v_expr',1,'p_v_expr','main.py',233),
  ('v_expr -> is_void','v_expr',1,'p_v_expr','main.py',234),
  ('v_expr -> new_expresion','v_expr',1,'p_v_expr','main.py',235),
  ('v_expr -> term','v_expr',1,'p_v_expr','main.py',236),
  ('v_expr -> comparison_expresion','v_expr',1,'p_v_expr','main.py',237),
  ('term -> var','term',1,'p_term','main.py',241),
  ('term -> num','term',1,'p_term','main.py',242),
  ('term -> str','term',1,'p_term','main.py',243),
  ('term -> bool','term',1,'p_term','main.py',244),
  ('term -> negnum','term',1,'p_term','main.py',245),
  ('term -> obracket v_expr cbracket','term',3,'p_term','main.py',246),
  ('var -> idx','var',1,'p_var','main.py',254),
  ('num -> number','num',1,'p_num','main.py',259),
  ('negnum -> minus term','negnum',2,'p_negnum','main.py',263),
  ('str -> string','str',1,'p_str','main.py',267),
  ('bool -> TRUE','bool',1,'p_bool','main.py',272),
  ('bool -> FALSE','bool',1,'p_bool','main.py',273),
  ('block_expresion -> ocurly block_expr ccurly','block_expresion',3,'p_block_expresion','main.py',277),
  ('block_expr -> expr semicolon block_expr_a','block_expr',3,'p_block_expr','main.py',282),
  ('block_expr_a -> expr semicolon block_expr_a','block_expr_a',3,'p_block_expr_a','main.py',287),
  ('block_expr_a -> empty','block_expr_a',1,'p_block_expr_a','main.py',288),
  ('property_decl -> declare_expresion semicolon','property_decl',2,'p_property_decl','main.py',296),
  ('conditional_expresion -> IF v_expr THEN expr ELSE expr FI','conditional_expresion',7,'p_conditional_expresion','main.py',301),
  ('is_void -> ISVOID expr','is_void',2,'p_is_void','main.py',306),
  ('while_expresion -> WHILE v_expr LOOP expr POOL','while_expresion',5,'p_while_expresion','main.py',311),
  ('case_expresion -> CASE expr OF case_list ESAC','case_expresion',5,'p_case_expresion','main.py',316),
  ('case_list -> declare_method case_expr expr semicolon case_list_a','case_list',5,'p_case_list','main.py',321),
  ('case_list_a -> declare_method case_expr expr semicolon case_list_a','case_list_a',5,'p_case_list_a','main.py',326),
  ('case_list_a -> empty','case_list_a',1,'p_case_list_a','main.py',327),
  ('let_expresion -> LET let_declr_list IN expr','let_expresion',4,'p_let_expresion','main.py',335),
  ('let_declr_list -> declare_expresion let_declr_list_a','let_declr_list',2,'p_let_declr_list','main.py',340),
  ('let_declr_list_a -> comma declare_expresion let_declr_list_a','let_declr_list_a',3,'p_let_declr_list_a','main.py',345),
  ('let_declr_list_a -> empty','let_declr_list_a',1,'p_let_declr_list_a','main.py',346),
  ('dispatch_expresion -> idx obracket dispatch_p_list cbracket','dispatch_expresion',4,'p_dispatch_expresion','main.py',354),
  ('dispatch_instance -> v_expr dot idx obracket dispatch_p_list cbracket','dispatch_instance',6,'p_dispatch_instance','main.py',359),
  ('dispatch_instance -> v_expr arrobe idx dot idx obracket dispatch_p_list cbracket','dispatch_instance',8,'p_dispatch_instance','main.py',360),
  ('dispatch_p_list -> v_expr dispatch_p_list_a','dispatch_p_list',2,'p_dispatch_p_list','main.py',368),
  ('dispatch_p_list -> empty','dispatch_p_list',1,'p_dispatch_p_list','main.py',369),
  ('dispatch_p_list_a -> comma v_expr dispatch_p_list_a','dispatch_p_list_a',3,'p_dispatch_p_list_a','main.py',376),
  ('dispatch_p_list_a -> empty','dispatch_p_list_a',1,'p_dispatch_p_list_a','main.py',377),
]
