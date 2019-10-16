import ply.yacc as yacc
from trabLexico import tokens

def p_empty(p):
    'empty :'
    pass

def p_programa(p):
    'programa : lista_declaracoes'
    print('programa', 'lista_declaracoes')

def p_lista_declaracoes(p):
    '''lista_declaracoes : lista_declaracoes declaracao
                       | declaracao'''
    if len(p) == 3:
        print('lista_declaracoes', 'lista_declaracoes', 'declaracao')
    else:
        print('declaracao')
        
def p_declaracao(p):
    '''declaracao : declaracao_variaveis
                    | declaracao_funcoes '''
    
    print('declaracao', p[1])

def p_declaracao_variaveis(p):
    '''declaracao_variaveis : tipo ID ';'
                            | tipo ID '[' NUM ']' ';' '''
    print('declaracao_variaveis', 'tipo')
    
def p_tipo(p):
    '''tipo : INT
             | VOID'''
    print('tipo', p[1])

def p_declaracao_funcoes(p):
    '''declaracao_funcoes : tipo ID '(' parametros ')' declaracao_composta '''
    
    print()
    
def p_parametros(p):
    '''parametros : lista_parametros
                   | VOID '''
    print()
    
def p_lista_parametros(p):
    '''lista_parametros : lista_parametros ',' param
                        | param '''
    
    print()
    
def p_param(p):
    '''param : tipo ID 
              | tipo ID '[' ']' '''
              
    print()
    
def p_declaracao_composta(p):
    '''declaracao_composta : '{' declaracao_locais lista_comandos '}' '''
    
    print()
    
def p_declaracao_locais(p):
    '''declaracao_locais : declaracao_locais declaracao_variaveis
                          | empty '''
    print()
    
def p_lista_comando(p):
    '''lista_comandos : lista_comandos comando
                      | empty '''
                      
    print()
    
def p_comando(p):
    '''comando : declaracao_expressao
               | declaracao_composta
               | declaracao_selecao
               | declaracao_iteracao
               | declaracao_retorno'''
    print()
    
def p_declaracao_expressao(p):
    '''declaracao_expressao : expressao ';'
                            | ';' '''
                            
    print()
    
def p_declaracao_selecao(p):
    '''declaracao_selecao : IF '(' expressao ')' comando
                           | IF '(' expressao ')' comando ELSE comando'''
    print()
    
def p_declaracao_iteracao(p):
    '''declaracao_iteracao : WHILE '(' expressao ')' comando'''
    print()
    
def p_declaracao_retorno(p):
    '''declaracao_retorno : RETURN ';'
                           | RETURN expressao ';' '''
    print()
    
def p_expressao(p):
    '''expressao : variavel '=' expressao
                  | expressao_simpes'''
    print()
    
def p_variavel(p):
    '''variavel : ID
                | ID '[' expressao ']' '''
    print()
    
def p_expressao_simples(p):
    '''expressao_simpes : soma_expressao op_relacional soma_expressao
                        | soma_expressao'''
    print()

def p_op_relacional(p):
    '''op_relacional : MENORI
                     | '<'
                     | '>'
                     | MAIORI
                     | EQUALS
                     | DIFFERENT'''
    print()
    
def p_soma_expressao(p):
    '''soma_expressao : soma_expressao soma termo
                       | termo'''
    print()

def p_soma(p):
    '''soma : '+'
            | '-' '''
    print()
    
def p_termo(p):
    '''termo : termo mult fator
              | fator'''
    print()
    
def p_mult(p):
    '''mult : '*'
            | '/' '''
    print()
    
def p_fator(p):
    '''fator : '(' expressao ')' 
             | variavel
             | ativacao
             | NUM'''
    print()
    
def p_ativacao(p):
    '''ativacao : ID '(' argumentos ')' '''
    print()
    
def p_argumentos(p):
    '''argumentos : lista_argumentos
                   | empty'''
    print()
    
def p_lista_argumentos(p):
    '''lista_argumentos : lista_argumentos ',' expressao
                         | expressao'''
    print()
    
# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")
  
parser = yacc.yacc()  #build the parser 
 
while True:
   try:
       s = input('calc > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)
   
'''
parser = yacc.yacc(start = 'Soma')  #build the parser
#Abrir o arquivo do codigo
arquivo = open('soma.txt', 'r')
codigo = arquivo.read()

#parser.input(codigo)

result = parser.parse(codigo)
print(result)'''