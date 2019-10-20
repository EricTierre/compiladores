import os
from PyQt5 import QtWidgets, uic

def CarregarArquivo():
	nome_arquivo = janela.lineEdit.text()
	if nome_arquivo=="":
		return
	try:
		arq = open(nome_arquivo, 'r')
		janela.campotexto_arquivo.setPlainText(arq.read())
	except IOError:
		print("Erro ao Abrir arquivo")

def printar(t):
	texto = 'TOKEN: ' + str(t.type) + ', LEXEMA: ' + str(t.value) +' , linha: ' + str(t.lineno)
	janela.campotexto_lexico.append(texto)
	
	#texto = str(t.type) + ', '
	#janela.campotexto_lexico.insertPlainText(texto);

def apagar():
	janela.campotexto_lexico.clear()
    
def apagar2():
	janela.campotexto_sintatico.clear()
	
def Refresh():
	janela.arquivos.clear()
	arq=os.listdir()
	for i in arq:
		if str(i).find(".txt")>0 or str(i).find(".py")>0 or str(i).find(".c")>0 or str(i).find(".cpp")>0 or str(i).find(".h")>0 or str(i).find(".java")>0:
			janela.arquivos.append(str(i))
			
def ZoomUp():
	janela.campotexto_arquivo.zoomIn(1)
	
def ZoomDown():
	janela.campotexto_arquivo.zoomOut(1)


app = QtWidgets.QApplication([])
janela = uic.loadUi("Interface.ui") #.ui
	