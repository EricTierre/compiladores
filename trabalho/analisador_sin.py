import ply.yacc as yacc
from analisador_lex import tokens
import analisador_lex
import interface

regras = []
regras_anotadas = []
last_rule = ''
pERRO = None
contador = 0
nomes = []
nomesGlobal = []
nomesGlobal2 = []
nomesFuncao = []
Lista_De_Simbolos = []
   
def p_empty(p):
    'empty :'
    global last_rule
    regra = 'empty -> $'
    regras.append(regra)
    
    regraAnotada = 'empty -> $'
    regras_anotadas.append(regraAnotada)
    
    last_rule = 'empty'
    global pERRO
    pERRO = p
    pass

def p_programa(p):
    '''programa : lista_declaracoes'''
    p[0] = p[1]
    
    global last_rule
    global pERRO
    global contador
    regra = 'programa -> lista_declaracoes'
    regras.append(regra)
    regraAnotada = 'programa -> lista_declaracoes'
    regras_anotadas.append(regraAnotada)
    
    last_rule = 'programa'
    
    pERRO = p
    
    campos = ''
    for x in Lista_De_Simbolos:
        for y in x:
            if campos == '':
                campos = y
            else:
                campos = campos + '          ' + y
        #print(x)
        interface.Tabela.campotexto_tabela.append(campos)
        campos = ''
        
    nomesGlobal.clear()
    nomesGlobal2.clear()
    nomesFuncao.clear()
    contador = 0
    Lista_De_Simbolos.clear()

def p_lista_declaracoes(p):
    '''lista_declaracoes : lista_declaracoes declaracao
                       | declaracao'''
    
    global last_rule
    if len(p) == 3:
        regra = 'lista_declaracoes -> lista_declaracoes  declaracao'
        regras.append(regra)
        p[0] = [p[1], p[2]]
        regraAnotada = 'lista_declaracoes -> lista_declaracoes  declaracao'
        regras_anotadas.append(regraAnotada)
    else:
        regra = 'lista_declaracoes -> declaracao'
        regras.append(regra)
        p[0] = p[1]
        regraAnotada = 'lista_declaracoes -> declaracao'
        regras_anotadas.append(regraAnotada)
    
    last_rule = 'lista_declaracoes'
    global pERRO
    pERRO = p
    
def p_declaracao(p):
    '''declaracao : declaracao_variaveis
                    | declaracao_funcoes '''
    p[0] = p[1]
    global pERRO
    global last_rule
    regra = 'declaracao -> ' + last_rule
    regras.append(regra)
    regraAnotada = 'declaracao -> ' + last_rule
    regras_anotadas.append(regraAnotada)
    if last_rule == 'declaracao_variaveis': 
        if p[0][0] == 'void':
            start = pERRO.linespan(0)[0]
            regra = 'Erro semântico, entre as linhas: ' + str(start) + ' e ' +  str(int(start)+1) + ' variavies devem ser do tipo int'
            interface.janela.campo_terminal.append(regra)
            return
        
        if p[1][1] in nomesGlobal or p[1][1] in nomesGlobal2:
            start = pERRO.linespan(0)[0]
            regra = 'Erro semântico, entre as linhas: ' + str(start) + ' e ' +  str(int(start)+1) + ' variavies com nomes iguais'
            interface.janela.campo_terminal.append(regra)
            return
        nomesGlobal.append(p[1][1])
        tupla = [str(p[0][1]), str(p[0][0]), 'Var', '-', str(id(p[0])), 'Global']
        Lista_De_Simbolos.append(tupla)
    if last_rule == 'declaracao_funcoes':
        if p[0][1] in nomesFuncao:
            start = pERRO.linespan(0)[0]
            regra = 'Erro semântico, entre as linhas: ' + str(start) + ' e ' +  str(int(start)+1) + ' funções com nomes iguais'
            interface.janela.campo_terminal.append(regra)
            return
        nomesFuncao.append(p[0][1])
        tupla = [str(p[0][1]), str(p[0][0]), 'Func', '-', str(id(p[0])), 'Global']
        Lista_De_Simbolos.append(tupla)
    
    last_rule = 'declaracao'   
    pERRO = p
    
def p_declaracao_variaveis(p):
    '''declaracao_variaveis : tipo ID ';'
                            | tipo ID '[' NUM ']' ';' '''
    global last_rule
    if len(p) == 4: 
        regra = 'declaracao_variaveis -> tipo  ' + str(p[2]) + '  ' + str(p[3])
        regras.append(regra)
        p[0] = [p[1], p[2], p[3]]
        regraAnotada = 'declaracao_variaveis.val('+str(p[1])+') -> tipo  ' + str(p[2]) + '  ' + str(p[3])
        regras_anotadas.append(regraAnotada)
        
    else:
        regra = 'declaracao_variaveis -> tipo  ' + str(p[2]) + '  '+ str(p[3]) +'  '+ str(p[4]) +'  '+ str(p[5]) +'  '+ str(p[6])
        regras.append(regra)
        p[0] = [p[1], p[2], p[3], p[4], p[5], p[6]]
        regraAnotada = 'declaracao_variaveis.val('+str(p[1])+') -> tipo  ' + str(p[2]) + '  '+ str(p[3]) +'  '+ str(p[4]) +'  '+ str(p[5]) +'  '+ str(p[6])
        regras_anotadas.append(regraAnotada)
    
    last_rule = 'declaracao_variaveis'
    global pERRO
    pERRO = p
        
def p_tipo(p):
    '''tipo : INT
             | VOID'''
    p[0] = p[1]
    global last_rule
    regra = 'tipo -> ' + str(p[1])
    regras.append(regra)
    regraAnotada = 'tipo.lex('+str(p[1])+') -> ' + str(p[1])
    regras_anotadas.append(regraAnotada)
    
    last_rule = 'tipo'
    global pERRO
    pERRO = p
    
def p_declaracao_funcoes(p):
    '''declaracao_funcoes : tipo ID '(' parametros ')' declaracao_composta '''
    nomes.clear()
    global contador
    contador+=1
    p[0] = [p[1], p[2], p[3], p[4], p[5], p[6]]
    global last_rule
    regra = 'declaracao_funcoes -> tipo  ' + str(p[2]) + '  ' + str(p[3]) + '  parametros  ' + str(p[5]) + '  declaracao_composta'
    regras.append(regra)
    regraAnotada = 'declaracao_funcoes.val('+str(p[1])+') -> tipo  ' + str(p[2]) + '  ' + str(p[3]) + '  parametros  ' + str(p[5]) + '  declaracao_composta'
    regras_anotadas.append(regraAnotada)
    
    last_rule = 'declaracao_funcoes'
    global pERRO
    pERRO = p
        
def p_parametros(p):
    '''parametros : lista_parametros
                   | VOID '''
    p[0] = p[1]
    global last_rule
    if p[1] == 'void':  
        regra = 'parametros -> ' + str(p[1])
        regraAnotada = 'parametros.lex('+str(p[0])+') -> lista_parametros'
        regras_anotadas.append(regraAnotada)
    else:
        regra = 'parametros -> lista_parametros'
        regraAnotada = 'parametros -> lista_parametros'
        regras_anotadas.append(regraAnotada)
    
    regras.append(regra)
    
    last_rule = 'parametros'
    global pERRO
    pERRO = p
    
def p_lista_parametros(p):
    '''lista_parametros : lista_parametros ',' param
                        | param '''
    global last_rule
    if len(p) == 4:
        regra = 'lista_parametros -> lista_parametros  ' + str(p[2]) + '  param'
        p[0] = [p[1], p[2], p[3]]
        regraAnotada = 'lista_parametros -> lista_parametros  ' + str(p[2]) + '  param'
        regras_anotadas.append(regraAnotada)
    else:
        regra = 'lista_parametros -> param'
        p[0] = p[1]
        regraAnotada = 'lista_parametros.val('+p[0][0]+') -> param'
        regras_anotadas.append(regraAnotada)
        
    regras.append(regra)
    
    last_rule = 'lista_parametros'
    global pERRO
    pERRO = p
    
def p_param(p):
    '''param : tipo ID 
              | tipo ID '[' ']' '''
    global last_rule          
    if len(p) == 5:
        regra = 'param -> tipo  ' + str(p[2]) + '  ' + str(p[3]) + '  ' + str(p[4]) 
        p[0] = [p[1], p[2], p[3], p[4]]
        regraAnotada = 'param.val('+str(p[1])+') -> tipo  ' + str(p[2]) + '  ' + str(p[3]) + '  ' + str(p[4]) 
        regras_anotadas.append(regraAnotada)
    else:
        regra = 'param -> tipo  ' + str(p[2])
        p[0] = [p[1], p[2]]
        regraAnotada = 'param.val('+str(p[1])+') -> tipo  ' + str(p[2])
        regras_anotadas.append(regraAnotada)
    
    regras.append(regra)    
    last_rule = 'param'
    global pERRO
    pERRO = p
    
    if p[0][0] == 'void':
        start = pERRO.linespan(0)[0]
        regra = 'Erro semântico, entre as linhas: ' + str(start) + ' e ' +  str(int(start)+1) + ' variavies devem ser do tipo int'
        interface.janela.campo_terminal.append(regra)
        return
        
    if p[0][1] in nomesGlobal or p[0][1] in nomes:
        start = pERRO.linespan(0)[0]
        regra = 'Erro semântico, entre as linhas: ' + str(start) + ' e ' +  str(int(start)+1) + ' variavies com nomes iguais'
        interface.janela.campo_terminal.append(regra)
        return
    nomes.append(p[0][1])
    nomesGlobal2.append(p[0][1])
    tupla = [str(p[0][1]), str(p[0][0]), 'Var', '-', str(id(p[0])), 'função '+str(contador)]
    Lista_De_Simbolos.append(tupla)
    
def p_declaracao_composta(p):
    '''declaracao_composta : '{' declaracao_locais lista_comandos '}' '''
    p[0] = [p[1], p[2], p[3], p[4]]
    global last_rule
    
    regra = 'declaracao_composta -> ' + str(p[1]) + '  declaracao_locais  lista_comandos  ' + str(p[4])
    regraAnotada = 'declaracao_composta -> ' + str(p[1]) + '  declaracao_locais  lista_comandos  ' + str(p[4])
    regras_anotadas.append(regraAnotada)
    regras.append(regra)
    
    last_rule = 'declaracao_composta'
    global pERRO
    pERRO = p
    
def p_declaracao_locais(p):
    '''declaracao_locais : declaracao_locais declaracao_variaveis
                          | empty '''
    global nomes
    global pERRO
    global last_rule
    if len(p) == 3:
        if p[2][0] == 'void':
            start = pERRO.linespan(0)[0]
            regra = 'Erro semântico, entre as linhas: ' + str(start) + ' e ' +  str(int(start)+1) + ' variavies devem ser do tipo int'
            interface.janela.campo_terminal.append(regra)
            return
        
        if p[2][1] in nomes or p[2][1] in nomesGlobal:
            start = pERRO.linespan(0)[0]
            regra = 'Erro semântico, entre as linhas: ' + str(start) + ' e ' +  str(int(start)+1) + ' variaveis com nomes iguais'
            interface.janela.campo_terminal.append(regra)
            return
        nomes.append(p[2][1])
        nomesGlobal2.append(p[2][1])
        regra = 'declaracao_locais -> declaracao_locais  declaracao_variaveis'
        p[0] = [p[1], p[2]]
        regraAnotada = 'declaracao_locais -> declaracao_locais  declaracao_variaveis'
        regras_anotadas.append(regraAnotada)
        tupla = [str(p[2][1]), str(p[2][0]), 'Var', '-', str(id(p[0])), 'função ' + str(contador)]
        Lista_De_Simbolos.append(tupla)
    else:
        regra = 'declaracao_locais -> empty'
        p[0] = p[1]
        regraAnotada = 'declaracao_locais -> empty'
        regras_anotadas.append(regraAnotada)
        
    regras.append(regra)
    
    last_rule = 'declaracao_locais'
    
    pERRO = p
    
def p_lista_comando(p):
    '''lista_comandos : lista_comandos comando
                      | empty '''
    global last_rule                  
    if len(p) == 3:     
        regra = 'lista_comandos -> lista_comandos  comando'
        p[0] = [p[1], p[2]]
        regraAnotada = 'lista_comandos -> lista_comandos  comando'
        regras_anotadas.append(regraAnotada)
    else:
        regra = 'lista_comandos -> empty'
        p[0] = p[1]
        regraAnotada = 'lista_comandos -> empty'
        regras_anotadas.append(regraAnotada)
        
    regras.append(regra)
    
    last_rule = 'lista_comandos'
    global pERRO
    pERRO = p
    
def p_comando(p):
    '''comando : declaracao_expressao
               | declaracao_composta
               | declaracao_selecao
               | declaracao_iteracao
               | declaracao_retorno'''
    p[0] = p[1]
    global last_rule
    regra = 'comando -> ' + last_rule
    regraAnotada = 'comando -> ' + last_rule
    regras_anotadas.append(regraAnotada)    
    regras.append(regra)
    
    last_rule = 'comando'
    global pERRO
    pERRO = p
    
def p_declaracao_expressao(p):
    '''declaracao_expressao : expressao ';'
                            | ';' '''
    global last_rule                        
    if len(p) == 3:
        regra = 'declaracao_expressao -> expressao  ' + str(p[2])
        p[0] = [p[1], p[2]]
        regraAnotada = 'declaracao_expressao -> expressao  ' + str(p[2])
        regras_anotadas.append(regraAnotada)
    else:
        regra = 'declaracao_expressao -> ' + str(p[1])
        p[0] = p[1]
        regraAnotada = 'declaracao_expressao -> ' + str(p[1])
        regras_anotadas.append(regraAnotada)
    
    regras.append(regra)
    
    last_rule = 'declaracao_expressao'
    global pERRO
    pERRO = p
    
def p_declaracao_selecao(p):
    '''declaracao_selecao : IF '(' expressao ')' comando
                           | IF '(' expressao ')' comando ELSE comando'''
    global last_rule
    if len(p) == 6:
        regra = 'declaracao_selecao -> ' + str(p[1]) + '  ' + str(p[2]) + '  expressao  ' + str(p[4]) + '  comando' 
        p[0] = [p[1], p[2], p[3], p[4], p[5]]
        regraAnotada = 'declaracao_selecao -> ' + str(p[1]) + '  ' + str(p[2]) + '  expressao  ' + str(p[4]) + '  comando'
        regras_anotadas.append(regraAnotada)
    else:
        regra = 'declaracao_selecao -> ' + str(p[1]) + '  ' + str(p[2]) + '  expressao  ' + str(p[4]) + '  comando  ' + str(p[6]) + '  comando'
        p[0] = [p[1], p[2], p[3], p[4], p[5], p[6], p[7]]
        regraAnotada = 'declaracao_selecao -> ' + str(p[1]) + '  ' + str(p[2]) + '  expressao  ' + str(p[4]) + '  comando  ' + str(p[6]) + '  comando'
        regras_anotadas.append(regraAnotada)
    regras.append(regra)
    
    last_rule = 'declaracao_selecao'
    global pERRO
    pERRO = p
    
def p_declaracao_iteracao(p):
    '''declaracao_iteracao : WHILE '(' expressao ')' comando'''
    p[0] = [p[1], p[2], p[3], p[4], p[5]]
    global last_rule 
    regra = 'declaracao_iteracao -> ' + str(p[1]) + '  ' + str(p[2]) + '  expressao  ' + str(p[4]) + '  comando'
    regras.append(regra)
    regraAnotada = 'declaracao_iteracao -> ' + str(p[1]) + '  ' + str(p[2]) + '  expressao  ' + str(p[4]) + '  comando'
    regras_anotadas.append(regraAnotada)
    
    last_rule = 'declaracao_iteracao'
    global pERRO
    pERRO = p
    
def p_declaracao_retorno(p):
    '''declaracao_retorno : RETURN ';'
                           | RETURN expressao ';' '''
    global last_rule 
    if len(p) == 3:
        regra = 'declaracao_retorno -> ' + str(p[1]) + '  ' + str(p[2])
        p[0] = [p[1], p[2]]
        regraAnotada = 'declaracao_retorno -> ' + str(p[1]) + '  ' + str(p[2])
        regras_anotadas.append(regraAnotada)
    else:
        regra = 'declaracao_retorno -> ' + str(p[1]) + '  expressao  ' + str(p[3])
        p[0] = [p[1], p[2], p[3]]
        regraAnotada = 'declaracao_retorno -> ' + str(p[1]) + '  expressao  ' + str(p[3])
        regras_anotadas.append(regraAnotada)
    regras.append(regra)
    
    last_rule = 'declaracao_retorno'
    global pERRO
    pERRO = p
    
def p_expressao(p):
    '''expressao : variavel '=' expressao
                  | expressao_simples'''
    global last_rule
    global pERRO    
    if len(p) == 4:
        regra = 'expressao -> variavel  ' + str(p[2]) + '  expressao'
        p[0] = [p[1], p[2], p[3]]
        regraAnotada = 'expressao -> variavel  ' + str(p[2]) + '  expressao'
        regras_anotadas.append(regraAnotada)
        name = p[0][0]
        if type(p[0][0]) == list: #Verificar se for atribuição de vetor
            name = p[0][0][0]
        
        for x in Lista_De_Simbolos:
            if name in x:
                x[3] = str(p[3])
                for y in Lista_De_Simbolos:
                    if str(p[3]) in y:
                        x[3] = str(y[3])
 
        if name in nomes or name in nomesGlobal:
            pass
        else:
            start = pERRO.linespan(0)[0]
            regra = 'Erro semântico, entre as linhas: ' + str(start) + ' e ' +  str(int(start)+1) + ' declarar variável antes de atribuir um valor à ela'
            interface.janela.campo_terminal.append(regra)
            return
    else:
        regra = 'expressao -> expressao_simples'
        p[0] = p[1]
        regraAnotada = 'expressao -> expressao_simples'
        regras_anotadas.append(regraAnotada)
   
    regras.append(regra)
    
    last_rule = 'expressao'
    
    pERRO = p
      
def p_variavel(p):
    '''variavel : ID
                | ID '[' expressao ']' '''
    global last_rule 
    if len(p) == 2:
        regra = 'variavel -> ' + str(p[1])
        p[0] = p[1]
        regraAnotada = 'variavel -> ' + str(p[1])
        regras_anotadas.append(regraAnotada)
    else:
        regra = 'variavel -> ' + str(p[1]) + '  ' + str(p[2]) + '  expressao  ' + str(p[4])
        p[0] = [p[1], p[2], p[3], p[4]]
        regraAnotada = 'variavel -> ' + str(p[1]) + '  ' + str(p[2]) + '  expressao  ' + str(p[4])
        regras_anotadas.append(regraAnotada)
    regras.append(regra)
    
    last_rule = 'variavel'
    global pERRO
    pERRO = p
    
def p_expressao_simples(p):
    '''expressao_simples : soma_expressao op_relacional soma_expressao
                        | soma_expressao'''
    global last_rule 
    if len(p) == 4:
        regra = 'expressao_simples -> soma_expressao  op_relacional  soma_expressao'
        p[0] = [p[1], p[2], p[3]]
        print(type(p[1]), type(p[3]))
        if str(p[1]).isdigit() and str(p[3]).isdigit():
            if p[2] == '<=':
                if p[1] <= p[3]:
                    p[0] = 'True'
                else:
                    p[0] = 'False'
            if p[2] == '>=':
                if p[1] >= p[3]:
                    p[0] = 'True'
                else:
                    p[0] = 'False'
            if p[2] == '<':
                if p[1] < p[3]:
                    p[0] = 'True'
                else:
                    p[0] = 'False'
            if p[2] == '>':
                if p[1] > p[3]:
                    p[0] = 'True'
                else:
                    p[0] = 'False' 
            if p[2] == '==':
                if p[1] == p[3]:
                    p[0] = 'True'
                else:
                    p[0] = 'False' 
            if p[2] == '!=':
                if p[1] != p[3]:
                    p[0] = 'True'
                else:
                    p[0] = 'False' 
        
        regraAnotada = 'expressao_simples.val('+str(p[0])+') -> soma_expressao  op_relacional  soma_expressao'
        regras_anotadas.append(regraAnotada)
    else:
        regra = 'expressao_simples -> soma_expressao'
        p[0] = p[1]
        regraAnotada = 'expressao_simples.val('+str(p[0])+') -> soma_expressao'
        regras_anotadas.append(regraAnotada)
    regras.append(regra)
    
    last_rule = 'expressao_simples'
    global pERRO
    pERRO = p
    
def p_op_relacional(p):
    '''op_relacional : MENORI
                     | '<'
                     | '>'
                     | MAIORI
                     | EQUALS
                     | DIFFERENT'''
    p[0] = p[1]
    global last_rule 
    regra = 'op_relacional -> ' + str(p[1])
    regras.append(regra)
    regraAnotada = 'op_relacional.lex('+str(p[0])+') -> ' + str(p[1])
    regras_anotadas.append(regraAnotada)
    
    last_rule = 'op_relacional'
    global pERRO
    pERRO = p
    
def p_soma_expressao(p):
    '''soma_expressao : soma_expressao soma termo
                       | termo'''
    
    global last_rule 
    antes = ''
    depois = ''
    if len(p) == 4:
        regra = 'soma_expressao -> soma_expressao  soma  termo'
        p[0] = [p[1],p[2],p[3]]
        if not str(p[1]).isdigit() or  not str(p[3]).isdigit():
            p[0] = '-'
        if str(p[1]).isdigit() and str(p[3]).isdigit():
            if p[2] == '+':
                p[0] = p[1] + p[3]
            else:
                p[0] = p[1] - p[3]
        else:
            for x in Lista_De_Simbolos:
                if str(p[1]) in x:
                    antes = x[3]
                    if antes != '-' and antes.isdigit() and str(p[3]).isdigit():
                        if p[2] == '+':
                            p[0] = int(antes) + p[3]
                        else:
                            p[0] = int(antes) - p[3]
                if str(p[3]) in x:
                    depois = x[3]
                    if depois != '-' and depois.isdigit() and str(p[1]).isdigit():
                        if p[2] == '+':
                            p[0] = p[1] + int(depois)
                        else:
                            p[0] = p[1] - int(depois)
                if antes != '-' and depois != '-' and antes.isdigit() and depois.isdigit():
                    if p[2] == '+':
                        p[0] = int(antes) + int(depois)
                    else:
                        p[0] = int(antes) - int(depois)
            
        regraAnotada = 'soma_expressao.val('+str(p[0])+') -> soma_expressao  soma  termo'
        regras_anotadas.append(regraAnotada)
    else:
        regra = 'soma_expressao -> termo'
        p[0] = p[1]
        regraAnotada = 'soma_expressao.val('+str(p[0])+') -> termo'
        regras_anotadas.append(regraAnotada)
    regras.append(regra)
    
    last_rule = 'soma_expressao'
    global pERRO
    pERRO = p
    
def p_soma(p):
    '''soma : '+'
            | '-' '''
    p[0] = p[1]
    global last_rule        
    regra = 'soma -> ' + str(p[1])
    regras.append(regra)
    regraAnotada = 'soma.lex('+str(p[0])+') -> ' + str(p[1])
    regras_anotadas.append(regraAnotada)
    last_rule = 'soma'
    global pERRO
    pERRO = p
    
def p_termo(p):
    '''termo : termo mult fator
              | fator'''
    global last_rule 
    antes = ''
    depois = ''
    if len(p) == 4:
        regra = 'termo -> termo  mult  fator'
        p[0] = [p[1],p[2],p[3]]
        if str(p[1]).isdigit() and str(p[3]).isdigit():
            if p[2] == '*':
                p[0] = p[1] * p[3]
            else:
                p[0] = p[1] / p[3]
        else:
            for x in Lista_De_Simbolos:
                if str(p[1]) in x:
                    antes = x[3]
                    if antes != '-' and antes.isdigit() and str(p[3]).isdigit():
                        if p[2] == '*':
                            p[0] = int(antes) * p[3]
                        else:
                            p[0] = int(antes) / p[3]
                if str(p[3]) in x:
                    depois = x[3]
                    if depois != '-' and depois.isdigit() and str(p[1]).isdigit():
                        if p[2] == '*':
                            p[0] = p[1] * int(depois)
                        else:
                            p[0] = p[1] / int(depois)
                if antes != '-' and depois != '-' and antes.isdigit() and depois.isdigit():
                    if p[2] == '*':
                        p[0] = int(antes) * int(depois)
                    else:
                        p[0] = int(antes) / int(depois)
        
        regraAnotada = 'termo.val('+str(p[0])+') -> termo  mult  fator'
        regras_anotadas.append(regraAnotada)
    else:
        regra = 'termo -> fator'
        p[0] = p[1]
        regraAnotada = 'termo.val('+str(p[0])+') -> fator'
        regras_anotadas.append(regraAnotada)
    regras.append(regra)
    
    last_rule = 'termo'
    global pERRO
    pERRO = p
    
def p_mult(p):
    '''mult : '*'
            | '/' '''
    p[0] = p[1]
    global last_rule 
    regra = 'mult -> ' + str(p[1])
    regras.append(regra)
    regraAnotada = 'mult.lex('+str(p[0])+') -> ' + str(p[1])
    regras_anotadas.append(regraAnotada)
    last_rule = 'mult'
    global pERRO
    pERRO = p
    
def p_fator(p):
    '''fator : '(' expressao ')' 
             | variavel
             | ativacao
             | NUM'''
    global last_rule 
    if len(p) == 4:
        regra = 'fator -> ' + str(p[1]) + '  expressao  ' + str(p[3])
        p[0] = [p[1], p[2], p[3]]
        regraAnotada = 'fator -> ' + str(p[1]) + '  expressao  ' + str(p[3])
        regras_anotadas.append(regraAnotada)
    elif str(p[1]).isdigit():
        regra = 'fator -> ' + str(p[1])
        p[0] = p[1]
        regraAnotada = 'fator.lex('+str(p[0])+') -> ' + str(p[1])
        regras_anotadas.append(regraAnotada)
    else:
        regra = 'fator -> ' + last_rule
        p[0] = p[1]
        regraAnotada = 'fator -> ' + last_rule
        regras_anotadas.append(regraAnotada)
    regras.append(regra)
    
    last_rule = 'fator'
    global pERRO
    pERRO = p
    
def p_ativacao(p):
    '''ativacao : ID '(' argumentos ')' '''
    p[0] = [p[1], p[2], p[3], p[4]]
    global last_rule 
    regra = 'ativacao -> ' + str(p[1]) +'  ' + str(p[2]) + '  argumentos  ' + str(p[4])
    regras.append(regra)
    regraAnotada = 'ativacao -> ' + str(p[1]) +'  ' + str(p[2]) + '  argumentos  ' + str(p[4])
    regras_anotadas.append(regraAnotada)
    
    last_rule = 'ativacao'
    global pERRO
    pERRO = p
    
def p_argumentos(p):
    '''argumentos : lista_argumentos
                   | empty'''
    p[0] = p[1]
    global last_rule 
    regra = 'argumentos -> ' + last_rule
    regras.append(regra)
    regraAnotada = 'argumentos -> ' + last_rule
    regras_anotadas.append(regraAnotada)
    last_rule = 'argumentos'
    global pERRO
    pERRO = p
    
def p_lista_argumentos(p):
    '''lista_argumentos : lista_argumentos ',' expressao
                         | expressao'''
    global last_rule 
    if len(p) == 4:
        regra = 'lista_argumentos -> lista_argumentos  ' + str(p[2]) + '  expressao'
        p[0] = [p[1], p[2], p[3]]
        regraAnotada = 'lista_argumentos -> lista_argumentos  ' + str(p[2]) + '  expressao'
        regras_anotadas.append(regraAnotada)
    else:
        regra = 'lista_argumentos -> expressao'
        p[0] = p[1]
        regraAnotada = 'lista_argumentos -> expressao'
        regras_anotadas.append(regraAnotada)
    regras.append(regra)
    
    last_rule = 'lista_argumentos'
    global pERRO
    pERRO = p
    
def p_error(p):
    if pERRO != None:
        start = pERRO.linespan(0)[0]
        regra = 'Erro sintático, entre as linhas: ' + str(start) + ' e ' +  str(int(start)+1)
        interface.janela.campo_terminal.append(regra)
    
    nomesGlobal.clear()
    nomesFuncao.clear()
    nomes.clear()
    contador = 0
    Lista_De_Simbolos.clear()
    
def Imprimir_Regras():
    for x in range(len(regras)-1, -1, -1):
        #print(regras[x])
        #interface.janela.campotexto_sintatico.append(regras[x])
        interface.Sintatico.campotexto_sintatico.append(regras[x])
    regras.clear()
    
def Imprimir_Regras_Anotadas():
    for x in range(len(regras_anotadas)-1, -1, -1):
        interface.Semantico.campotexto_semantico.append(regras_anotadas[x])
    regras_anotadas.clear()

def Construir():
    parser = yacc.yacc(start = 'programa')
    return parser






'''
if __name__ == "__main__":
    parser = yacc.yacc(start = 'programa', debug=False, write_tables=False)#Construir o parser
    
    #Abrir o arquivo do codigo
    arquivo = open('codigo.txt', 'r')
    codigo = arquivo.read()
        
    parser.parse(codigo, tracking=True)
    print()

    Imprimir_Regras()
'''