import ply.lex as lex

reserved = {
	'void'	:	'VOID',
	'int'	:	'INT',
}

# List of token names.   This is always required
tokens = ['NUMBER','PLUS','MINUS','TIMES','DIVIDE','LPAREN','RPAREN',
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

# A regular expression rule with some action code
def t_NUMBER(t):
	r'\d+'
	t.value = int(t.value)
	return t
	
def t_ID(t):
	r'[a-zA-Z_][a-zA-Z_0-9]*'
	if t.value in reserved:# Check for reserved words
		t.type = reserved[ t.value ]
	return t

# Define a rule so we can track line numbers
def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
	print("Illegal character '%s'" , t.value[0])
	t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

def main():
	teste = open('codigo.txt', 'r')
	codigo = teste.read()
	# Give the lexer some input
	lexer.input(codigo)

	# Tokenize
	while True:
		tok = lexer.token()
		if not tok: 
			break      # No more input
		print(tok)
		
main()