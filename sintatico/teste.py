import ply.yacc as yacc
from trabLexico import tokens

regras = []

def p_empty(p):
    'empty :'
    regra = 'empty -> $'
    regras.append(regra)
    print('empty', ' ')
    pass

def p_programa(p):
    '''programa : lista_declaracoes'''
    regra = 'programa -> lista_declaracoes'
    regras.append(regra)
    print('programa', 'lista_declaracoes')

def p_lista_declaracoes(p):
    '''lista_declaracoes : lista_declaracoes declaracao
                       | declaracao'''
    if len(p) == 3:
        regra = 'lista_declaracoes -> lista_declaracoes declaracao'
        regras.append(regra)
        print('lista_declaracoes', 'lista_declaracoes', 'declaracao')
    else:
        regra = 'lista_declaracoes -> declaracao'
        regras.append(regra)
        print('lista_declaracoes', 'declaracao')
        
def p_declaracao(p):
    '''declaracao : declaracao_variaveis
                    | declaracao_funcoes '''
    regra = 'declaracao -> declaracao_variaveis ou declaracao_funcoes'
    regras.append(regra)
    print('declaracao', 'declaracao_variaveis ou declaracao_funcoes')

def p_declaracao_variaveis(p):
    '''declaracao_variaveis : tipo ID ';'
                            | tipo ID '[' NUM ']' ';' '''
    if len(p) == 4: 
        regra = 'declaracao_variaveis -> tipo ' + str(p[2]) + str(p[3])
        regras.append(regra)
        print('declaracao_variaveis', 'tipo', p[2], ';')
    else:
        regra = 'declaracao_variaveis -> tipo ' + str(p[2]) + str(p[3]) + str(p[4]) + str(p[5]) + str(p[6])
        regras.append(regra)
        print('declaracao_variaveis', 'tipo', p[2], '[', p[4], ']', ';')
    
def p_tipo(p):
    '''tipo : INT
             | VOID'''
    regra = 'tipo ->' + str(p[1])
    regras.append(regra)
    print('tipo', p[1])

def p_declaracao_funcoes(p):
    '''declaracao_funcoes : tipo ID '(' parametros ')' declaracao_composta '''
    
    print('declaracao_funcoes', 'tipo', p[2], '(', 'parametros', ')', 'declaracao_composta')
    
def p_parametros(p):
    '''parametros : lista_parametros
                   | VOID '''
    print('parametros', 'lista_parametros ou void')
    
def p_lista_parametros(p):
    '''lista_parametros : lista_parametros ',' param
                        | param '''
    if len(p) == 4:
        print('lista_parametros', 'lista_parametros', ',', 'param')
    else:
        print('lista_parametros', 'param')
    
def p_param(p):
    '''param : tipo ID 
              | tipo ID '[' ']' '''
              
    if len(p) == 5:
        print('param', 'tipo', p[2], '[', ']')
    else:
        print('param', 'tipo', p[2])
    
def p_declaracao_composta(p):
    '''declaracao_composta : '{' declaracao_locais lista_comandos '}' '''
    
    print('declaracao_composta','{','declaracao_locais', 'lista_comandos', '}')
    
def p_declaracao_locais(p):
    '''declaracao_locais : declaracao_locais declaracao_variaveis
                          | empty '''
    if len(p) == 3:
        print('declaracao_locais', 'declaracao_locais', 'declaracao_variaveis')
    else:
        print('declaracao_locais', 'empty')
    
def p_lista_comando(p):
    '''lista_comandos : lista_comandos comando
                      | empty '''
                      
    if len(p) == 3:
        print('lista_comandos', 'lista_comandos', 'comando')
    else:
        print('lista_comandos', 'empty')
    
def p_comando(p):
    '''comando : declaracao_expressao
               | declaracao_composta
               | declaracao_selecao
               | declaracao_iteracao
               | declaracao_retorno'''
    print('comando', 'declaracao_expressao ou declaracao_composta ou declaracao_selecao ou declaracao_iteracao ou declaracao_retorno')
    
def p_declaracao_expressao(p):
    '''declaracao_expressao : expressao ';'
                            | ';' '''
                            
    if len(p) == 3:
        print('declaracao_expressao', 'expressao', ';')
    else:
        print('declaracao_expressao', ';')
    
def p_declaracao_selecao(p):
    '''declaracao_selecao : IF '(' expressao ')' comando
                           | IF '(' expressao ')' comando ELSE comando'''
    if len(p) == 6:
        print('declaracao_selecao', 'IF')
    else:
        print('declaracao_selecao', 'IF Else')
    
def p_declaracao_iteracao(p):
    '''declaracao_iteracao : WHILE '(' expressao ')' comando'''
    
    print('declaracao_iteracao','WHILE', '(', 'expressao', ')', 'comando')
    
def p_declaracao_retorno(p):
    '''declaracao_retorno : RETURN ';'
                           | RETURN expressao ';' '''
    
    if len(p) == 3:
        print('declaracao_retorno', 'RETURN', ';')
    else:
        print('declaracao_retorno', 'RETURN', 'expressao', ';')
    
def p_expressao(p):
    '''expressao : variavel '=' expressao
                  | expressao_simples'''
    
    if len(p) == 4:
        print('expressao', 'variavel', '=', 'expressao')
    else:
        print('expressao', 'expressao_simples')
    
def p_variavel(p):
    '''variavel : ID
                | ID '[' expressao ']' '''
    
    if len(p) == 2:
        print('variavel', p[1])
    else:
        print('variavel', p[1], '[', 'expressao', ']')
    
def p_expressao_simples(p):
    '''expressao_simples : soma_expressao op_relacional soma_expressao
                        | soma_expressao'''
    if len(p) == 4:
        print('expressao_simples', 'soma_expressao', 'op_relacional', 'soma_expressao')
    else:
        print('expressao_simples', 'soma_expressao')

def p_op_relacional(p):
    '''op_relacional : MENORI
                     | '<'
                     | '>'
                     | MAIORI
                     | EQUALS
                     | DIFFERENT'''
    print('op_relacional', p[1])
    
def p_soma_expressao(p):
    '''soma_expressao : soma_expressao soma termo
                       | termo'''
    
    if len(p) == 4:
        print('soma_expressao', 'soma_expressao', 'soma', 'termo')
    else:
        print('soma_expressao', 'termo')

def p_soma(p):
    '''soma : '+'
            | '-' '''
            
    print('soma', p[1])
    
def p_termo(p):
    '''termo : termo mult fator
              | fator'''
              
    if len(p) == 4:
        print('termo', 'termo', 'mult', 'fator')
    else:
        print('declaracao_expressao', 'fator')
    
def p_mult(p):
    '''mult : '*'
            | '/' '''
    
    print('mult', p[1])
    
def p_fator(p):
    '''fator : '(' expressao ')' 
             | variavel
             | ativacao
             | NUM'''
    
    if len(p) == 4:
        print('fator', '(', 'expressao', ')')
    else:
        print('fator', 'variavel ou ativacao ou NUM')
    
def p_ativacao(p):
    '''ativacao : ID '(' argumentos ')' '''
    
    print('ativacao', p[1], '(', 'argumentos', ')')
    
def p_argumentos(p):
    '''argumentos : lista_argumentos
                   | empty'''
    
    print('argumentos', 'lista_argumentos ou empty')
    
def p_lista_argumentos(p):
    '''lista_argumentos : lista_argumentos ',' expressao
                         | expressao'''
    
    if len(p) == 4:
        print('lista_argumentos', 'lista_argumentos', ',', 'expressao')
    else:
        print('lista_argumentos', 'expressao')
    
def p_error(p):
    print("Erro sintatico!", p) 

def Imprimir_Regras():
    for x in range(len(regras)-1, -1, -1):
        print(regras[x])

if __name__ == "__main__":
    parser = yacc.yacc(start = 'programa')#Construir o parser
    
    #Abrir o arquivo do codigo
    arquivo = open('codigo.txt', 'r')
    codigo = arquivo.read()
        
    parser.parse(codigo)
    print()

    Imprimir_Regras()