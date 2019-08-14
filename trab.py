import ply.lex as lex
from ply.lex import TOKEN
from PyQt5 import QtWidgets, uic
from threading import Thread
import os

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
	invalid = 'Inválido ' + t.value[0] + ', linha: ' + str(t.lineno)
	dlg.campotexto_lexico.append(invalid)
	print("Caracter inválido '%s'" , t.value[0])
	t.lexer.skip(1)
	
def CarregarArquivo():
	nome_arquivo = dlg.lineEdit.text()
	if nome_arquivo=="":
		return
	try:
		arq = open(nome_arquivo, 'r')
		dlg.campotexto_arquivo.setText(arq.read())
	except IOError:
		print("Erro ao Abrir arquivo")

def printar(t):
	texto = 'TOKEN: ' + str(t.type) + ', LEXEMA: ' + str(t.value) +' , linha: ' + str(t.lineno)
	dlg.campotexto_lexico.append(texto)

def apagar():
	dlg.campotexto_lexico.clear()
	
def main():
	#lexer = lex.lex(debug=1)
	# Build the lexer
	lexer = lex.lex()

	#Passar ao lexer uma entrada
	lexer.input(dlg.campotexto_arquivo.toPlainText())
	#Tokenize
	for tok in lexer:
		printar(tok)

def Refresh():
	dlg.arquivos.clear()
	arq=os.listdir()
	for i in arq:
		if str(i).find(".txt")>0 or str(i).find(".py")>0 or str(i).find(".c")>0 or str(i).find(".cpp")>0 or str(i).find(".h")>0 or str(i).find(".java")>0:
			dlg.arquivos.append(str(i))

if __name__ == "__main__":
	app = QtWidgets.QApplication([])
	dlg = uic.loadUi("teste.ui") #.ui
	
	dlg.botao_abrirarquivo.clicked.connect(CarregarArquivo)
	dlg.botao_lexico.clicked.connect(main)
	dlg.botao_deletar.clicked.connect(apagar)
	dlg.refreshbtn.clicked.connect(Refresh)
	
	dlg.show()
	app.exec()