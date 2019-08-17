import os
from PyQt5 import QtWidgets, uic

def CarregarArquivo():
	nome_arquivo = janela.lineEdit.text()
	if nome_arquivo=="":
		return
	try:
		arq = open(nome_arquivo, 'r')
		janela.campotexto_arquivo.setText(arq.read())
	except IOError:
		print("Erro ao Abrir arquivo")

def printar(t):
	#texto = 'TOKEN: ' + str(t.type) + ', LEXEMA: ' + str(t.value) +' , linha: ' + str(t.lineno)
	texto = str(t.type) + ', '
	janela.campotexto_lexico.insertPlainText(texto);
	#janela.campotexto_lexico.append(texto)

def apagar():
	janela.campotexto_lexico.clear()
	
def Refresh():
	janela.arquivos.clear()
	arq=os.listdir()
	for i in arq:
		if str(i).find(".txt")>0 or str(i).find(".py")>0 or str(i).find(".c")>0 or str(i).find(".cpp")>0 or str(i).find(".h")>0 or str(i).find(".java")>0:
			janela.arquivos.append(str(i))


app = QtWidgets.QApplication([])
janela = uic.loadUi("teste.ui") #.ui
	