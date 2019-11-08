import os
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog

nome_arquivo = None

def CarregarArquivo():
    global nome_arquivo
    nome_arquivo = janela.lineEdit.text()
    if nome_arquivo=="":
        return
    try:
        arq = open(nome_arquivo, 'r')
        janela.campotexto_arquivo.setPlainText(arq.read())
    except IOError:
        print("Erro ao Abrir arquivo")

def CarregarArquivoOpenFile():
    global nome_arquivo
    nome_arquivo = QFileDialog.getOpenFileName(None, 'Open File')   

    if nome_arquivo=="":
        return
    try:
        arq = open(nome_arquivo[0], 'r')
        janela.campotexto_arquivo.setPlainText(arq.read())
    except IOError:
        print("Erro ao Abrir arquivo")

def SalvarArquivo():
    #if nome_arquivo == None:
    #    return
    nome_arquivo = QFileDialog.getSaveFileName(None)
    try:
        arq = open(nome_arquivo[0], 'w')
        arq.write(janela.campotexto_arquivo.toPlainText())
        arq.close()
    except IOError:
        print("Erro ao Abrir arquivo")
        
def printar(t):
    texto = 'TOKEN: ' + str(t.type) + ', LEXEMA: ' + str(t.value) +' , linha: ' + str(t.lineno)
    #janela.campotexto_lexico.append(texto)
    Lexico.campotexto_lexico.append(texto)
       
    #texto = str(t.type) + ', '
    #janela.campotexto_lexico.insertPlainText(texto);
		
def ZoomUp():
	janela.campotexto_arquivo.zoomIn(1)
	
def ZoomDown():
	janela.campotexto_arquivo.zoomOut(1)


app = QtWidgets.QApplication([])
janela = uic.loadUi("Interface.ui") #.ui
Lexico = uic.loadUi("Analisador_Lexico.ui") #.ui
Sintatico = uic.loadUi("Analisador_Sintatico.ui") #.ui
Semantico = uic.loadUi("Analisador_Semantico.ui") #.ui
Tabela = uic.loadUi("Tabela_Simbolos.ui") #.ui
	