import ply.lex as lex
import interface

#Palvras reservadas com seus respectivos tokens
reserved = {
	'void' : 'VOID',
	'int' : 'INT',
	'if' : 'IF',
	'else' : 'ELSE',
	'return' : 'RETURN',
	'while' : 'WHILE',	
}

#Palavras especiais
literals = ['+', '-', '*', '/', '{', '}', '(', ')',
			'[', ']', '<', '>', '=', ';', ','			
]	

#Lista com os nomes dos tokens
tokens = ['NUM','ID', 'EQUALS', 'MENORI', 'MAIORI', 'DIFFERENT'] + list(reserved.values())

t_ignore_COMMENT = r'(/\*(.|\n)*?\*/)|(//.*)'
t_ignore  = ' \t'

t_EQUALS = r'=='
t_MENORI = r'<='
t_MAIORI = r'>='
t_DIFFERENT = r'!='

#Expressão regular para número
def t_NUM(t):
	r'[0-9][0-9]*'
	t.value = int(t.value)
	return t

#Expressão regular para id
def t_ID(t):
	r'[a-zA-Z][a-zA-Z]*'
	if t.value in reserved:# Checar por palavras reservadas
		t.type = reserved[ t.value ]
	return t

#Define a rule so we can track line numbers
def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

#Error handling rule
def t_error(t):
	#Erro = 'Erro: ' + t.value[0] + ', '
	#interface.janela.campotexto_lexico.insertPlainText(Erro)
	
	Erro = 'Erro Lexico: ' + str(t.value[0]) + ', ' + 'Linha: ' + str(t.lineno)
	interface.janela.campo_terminal.append(Erro)
	
	#interface.janela.campotexto_lexico.setText(Erro)
	t.lexer.skip(1)
   
def Construir():
    lexer = lex.lex()#Construir o lexico
    return lexer
	