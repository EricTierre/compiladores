import ply.lex as lex

#Palvras reservadas com seus respectivos tokens
reserved = {
	'void' : 'VOID',
	'int' : 'INT',
	'if' : 'IF',
	'else' : 'ELSE',
	'return' : 'RETURN',
	'while' : 'WHILE',	
}

literals = ['+', '-', '*', '/', '{', '}', '(', ')',
			'[', ']', '<', '>', '=', ';', ','			
]	

#Lista dos tokens
tokens = ['NUM','ID', 'EQUALS', 'MENORI', 'MAIORI', 'DIFFERENT'] + list(reserved.values())

t_ignore_COMMENT = r'/\*'+ r'(\n|.*)*' + r'\*/'
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
	print("Caracter inválido: " , t.value[0])
	t.lexer.skip(1)	

if __name__ == "__main__":
	
	#Contruir o lexer
	lexer = lex.lex()
	
	#Abrir o arquivo do codigo
	arquivo = open('codigo.txt', 'r')
	codigo = arquivo.read()

	#Passar ao lexer uma entrada
	lexer.input(codigo)
	
	for tok in lexer:
		print(tok.type, end =', ')