import ply.lex as lex

#Palvras reservadas com seus respectivos tokens
reserved = {
	'void' : 'VOID',
	'int' : 'INT',
	'if' : 'IF',
	'return' : 'RETURN',
	'while' : 'WHILE',	
}

# List of token names.   This is always required
tokens = ['NUM','PLUS','MINUS','TIMES','DIVIDE','LPAREN','RPAREN',
	'ID',
	]+ list(reserved.values())
 
# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

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

# Define a rule so we can track line numbers
def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
	print("Caracter inválido '%s'" , t.value[0])
	t.lexer.skip(1)

def main():
	# Build the lexer
	lexer = lex.lex()
	
	teste = open('codigo.txt', 'r')
	codigo = teste.read()
	#Passar ao lexer uma entrada
	lexer.input(codigo)

	#Tokenize
	while True:
		tok = lexer.token()
		if not tok: 
			break      # No more input
		print(tok)
		
main()