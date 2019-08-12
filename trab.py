import ply.lex as lex
from ply.lex import TOKEN
from PyQt5 import QtWidgets, uic
from threading import Thread

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

# List of token names.   This is always required
tokens = ['NUM','ID', 'EQUALS', 'MENORI', 'MAIORI', 'DIFFERENT'] + list(reserved.values())

t_ignore_COMMENT = r'/\*'+ r'(\n|.*)*' + r'\*/'
t_ignore  = ' \t'
t_EQUALS = r'=='
t_MENORI = r'<='
t_MAIORI = r'>='
t_DIFFERENT = r'!='

#t_CLOSECOMMENT = r'*/'

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
	
def CarregarArquivo():
	nome_arquivo = dlg.lineEdit.text()
	arq = open(nome_arquivo, 'r')
	dlg.campotexto_arquivo.setText(arq.read())

def printar(t):
	texto = 'TOKEN: ' + str(t.type) + ', LEXEMA: ' + str(t.value) +' , linha: ' + str(t.lineno)
	dlg.campotexto_lexico.append(texto)

def apagar():
	dlg.campotexto_lexico.clear()
	
def main():
	# Build the lexer
	#lexer = lex.lex(debug=1)
	lexer = lex.lex()

	#Passar ao lexer uma entrada
	lexer.input(dlg.campotexto_arquivo.toPlainText())
	#Tokenize
	for tok in lexer:
		printar(tok)
	'''
	while True:
		tok = lexer.token()
		if not tok: 
			break      # No more input
		printar(tok)
		#print(tok.type, end=', ')
	#print()
	'''
if __name__ == "__main__":
	app = QtWidgets.QApplication([])
	dlg = uic.loadUi("teste.ui") #.ui
	
	dlg.botao_abrirarquivo.clicked.connect(CarregarArquivo)
	dlg.botao_lexico.clicked.connect(main)
	dlg.botao_deletar.clicked.connect(apagar)
	
	t1 = Thread(target=dlg.show())
	t2 = Thread(target=app.exec())
	t1.start()
	t2.start()
	#dlg.show()
	#app.exec()