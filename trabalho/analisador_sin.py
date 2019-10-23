import ply.yacc as yacc
from analisador_lex import tokens
import interface

regras = []
last_rule = ''
pERRO = None
    
def p_empty(p):
    'empty :'
    global last_rule
    regra = 'empty -> $'
    regras.append(regra)
    
    last_rule = 'empty'
    global pERRO
    pERRO = p
    pass

def p_programa(p):
    '''programa : lista_declaracoes'''
    global last_rule
    regra = 'programa -> lista_declaracoes' 
    regras.append(regra)
    
    last_rule = 'programa'
    #print(pERRO.linespan(0))
    global pERRO
    pERRO = p

def p_lista_declaracoes(p):
    '''lista_declaracoes : lista_declaracoes declaracao
                       | declaracao'''
    global last_rule
    if len(p) == 3:
        regra = 'lista_declaracoes -> lista_declaracoes  declaracao'
        regras.append(regra)
    else:
        regra = 'lista_declaracoes -> declaracao'
        regras.append(regra)
    
    last_rule = 'lista_declaracoes'
    global pERRO
    pERRO = p
    
def p_declaracao(p):
    '''declaracao : declaracao_variaveis
                    | declaracao_funcoes '''
    global last_rule
    regra = 'declaracao -> ' + last_rule
    regras.append(regra)
    
    last_rule = 'declaracao'
    global pERRO
    pERRO = p
    
def p_declaracao_variaveis(p):
    '''declaracao_variaveis : tipo ID ';'
                            | tipo ID '[' NUM ']' ';' '''
    global last_rule
    if len(p) == 4: 
        regra = 'declaracao_variaveis -> tipo  ' + str(p[2]) + '  ' + str(p[3])
        regras.append(regra)
    else:
        regra = 'declaracao_variaveis -> tipo  ' + str(p[2]) + '  '+ str(p[3]) +'  '+ str(p[4]) +'  '+ str(p[5]) +'  '+ str(p[6])
        regras.append(regra)
    
    last_rule = 'declaracao_variaveis'
    global pERRO
    pERRO = p
    
def p_tipo(p):
    '''tipo : INT
             | VOID'''
    global last_rule
    regra = 'tipo -> ' + str(p[1])
    regras.append(regra)
    
    last_rule = 'tipo'
    global pERRO
    pERRO = p
    
def p_declaracao_funcoes(p):
    '''declaracao_funcoes : tipo ID '(' parametros ')' declaracao_composta '''
    global last_rule
    regra = 'declaracao_funcoes -> tipo  ' + str(p[2]) + '  ' + str(p[3]) + '  parametros  ' + str(p[5]) + '  declaracao_composta'
    regras.append(regra)
    
    last_rule = 'declaracao_funcoes'
    global pERRO
    pERRO = p
    
def p_parametros(p):
    '''parametros : lista_parametros
                   | VOID '''
    global last_rule
    if p[1] == 'void':  
        regra = 'parametros -> ' + str(p[1])
    else:
        regra = 'parametros -> lista_parametros'
    
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
    else:
        regra = 'lista_parametros -> param'
        
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
    else:
        regra = 'param -> tipo  ' + str(p[2])
    
    regras.append(regra)
    
    last_rule = 'param'
    global pERRO
    pERRO = p
    
def p_declaracao_composta(p):
    '''declaracao_composta : '{' declaracao_locais lista_comandos '}' '''
    global last_rule
    
    regra = 'declaracao_composta -> ' + str(p[1]) + '  declaracao_locais  lista_comandos  ' + str(p[4])
    
    regras.append(regra)
    
    last_rule = 'declaracao_composta'
    global pERRO
    pERRO = p
    
def p_declaracao_locais(p):
    '''declaracao_locais : declaracao_locais declaracao_variaveis
                          | empty '''
    global last_rule
    if len(p) == 3:
        regra = 'declaracao_locais -> declaracao_locais  declaracao_variaveis'
    else:
        regra = 'declaracao_locais -> empty'
        
    regras.append(regra)
    
    last_rule = 'declaracao_locais'
    global pERRO
    pERRO = p
    
def p_lista_comando(p):
    '''lista_comandos : lista_comandos comando
                      | empty '''
    global last_rule                  
    if len(p) == 3:     
        regra = 'lista_comandos -> lista_comandos  comando'
    else:
        regra = 'lista_comandos -> empty'
        
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
    global last_rule
    regra = 'comando -> ' + last_rule
        
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
    else:
        regra = 'declaracao_expressao -> ' + str(p[1])
    
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
    else:
        regra = 'declaracao_selecao -> ' + str(p[1]) + '  ' + str(p[2]) + '  expressao  ' + str(p[4]) + '  comando  ' + str(p[6]) + '  comando'
    regras.append(regra)
    
    last_rule = 'declaracao_selecao'
    global pERRO
    pERRO = p
    
def p_declaracao_iteracao(p):
    '''declaracao_iteracao : WHILE '(' expressao ')' comando'''
    global last_rule 
    regra = 'declaracao_iteracao -> ' + str(p[1]) + '  ' + str(p[2]) + '  expressao  ' + str(p[4]) + '  comando'
    regras.append(regra)
    
    last_rule = 'declaracao_iteracao'
    global pERRO
    pERRO = p
    
def p_declaracao_retorno(p):
    '''declaracao_retorno : RETURN ';'
                           | RETURN expressao ';' '''
    global last_rule 
    if len(p) == 3:
        regra = 'declaracao_retorno -> ' + str(p[1]) + '  ' + str(p[2])
    else:
        regra = 'declaracao_retorno -> ' + str(p[1]) + '  expressao  ' + str(p[3])
    
    regras.append(regra)
    
    last_rule = 'declaracao_retorno'
    global pERRO
    pERRO = p
    
def p_expressao(p):
    '''expressao : variavel '=' expressao
                  | expressao_simples'''
    global last_rule 
    if len(p) == 4:
        regra = 'expressao -> variavel  ' + str(p[2]) + '  expressao'
    else:
        regra = 'expressao -> expressao_simples'
    regras.append(regra)
    
    last_rule = 'expressao'
    global pERRO
    pERRO = p
    
def p_variavel(p):
    '''variavel : ID
                | ID '[' expressao ']' '''
    global last_rule 
    if len(p) == 2:
        regra = 'variavel -> ' + str(p[1])
    else:
        regra = 'variavel -> ' + str(p[1]) + '  ' + str(p[2]) + '  expressao  ' + str(p[4])
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
    else:
        regra = 'expressao_simples -> soma_expressao'
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
    global last_rule 
    regra = 'op_relacional -> ' + str(p[1])
    regras.append(regra)
    
    last_rule = 'op_relacional'
    global pERRO
    pERRO = p
    
def p_soma_expressao(p):
    '''soma_expressao : soma_expressao soma termo
                       | termo'''
    
    global last_rule 
    if len(p) == 4:
        regra = 'soma_expressao -> soma_expressao  soma  termo'
    else:
        regra = 'soma_expressao -> termo'
    regras.append(regra)
    
    last_rule = 'soma_expressao'
    global pERRO
    pERRO = p
    
def p_soma(p):
    '''soma : '+'
            | '-' '''
    global last_rule        
    regra = 'soma -> ' + str(p[1])
    regras.append(regra)
    
    last_rule = 'soma'
    global pERRO
    pERRO = p
    
def p_termo(p):
    '''termo : termo mult fator
              | fator'''
    global last_rule           
    if len(p) == 4:
        regra = 'termo -> termo  mult  fator'
    else:
        regra = 'termo -> fator'
    regras.append(regra)
    
    last_rule = 'termo'
    global pERRO
    pERRO = p
    
def p_mult(p):
    '''mult : '*'
            | '/' '''
    global last_rule 
    regra = 'mult -> ' + str(p[1])
    regras.append(regra)
    
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
    elif str(p[1]).isdigit():
        regra = 'fator -> ' + str(p[1])
    else:
        regra = 'fator -> ' + last_rule
    regras.append(regra)
    
    last_rule = 'fator'
    global pERRO
    pERRO = p
    
def p_ativacao(p):
    '''ativacao : ID '(' argumentos ')' '''
    global last_rule 
    regra = 'ativacao -> ' + str(p[1]) +'  ' + str(p[2]) + '  argumentos  ' + str(p[4])
    regras.append(regra)
    
    last_rule = 'ativacao'
    global pERRO
    pERRO = p
    
def p_argumentos(p):
    '''argumentos : lista_argumentos
                   | empty'''
    global last_rule 
    regra = 'argumentos -> ' + last_rule
    regras.append(regra)
    
    last_rule = 'argumentos'
    global pERRO
    pERRO = p
    
def p_lista_argumentos(p):
    '''lista_argumentos : lista_argumentos ',' expressao
                         | expressao'''
    global last_rule 
    if len(p) == 4:
        regra = 'lista_argumentos -> lista_argumentos  ' + str(p[2]) + '  expressao'
    else:
        regra = 'lista_argumentos -> expressao'
    regras.append(regra)
    
    last_rule = 'lista_argumentos'
    global pERRO
    pERRO = p
    
def p_error(p):
    start, end = pERRO.linespan(0)
    regra = 'Erro sintatico, entre as linhas: ' + str(start) + ' e ' +  str(int(start)+1)
    regras.append(regra)
    
def Imprimir_Regras():
    for x in range(len(regras)-1, -1, -1):
        print(regras[x])
        #interface.janela.campotexto_sintatico.append(regras[x])
    
    regras.clear()
    
parser = yacc.yacc(start = 'programa')#Construir o parser    
def Construir(): 
    parser = yacc.yacc(start = 'programa')#Construir o parser
    return parser
'''
if __name__ == "__main__":
    parser = yacc.yacc(start = 'programa')#Construir o parser
    
    #Abrir o arquivo do codigo
    arquivo = open('codigo.txt', 'r')
    codigo = arquivo.read()
        
    parser.parse(codigo, tracking=True)
    print()

    Imprimir_Regras()
'''