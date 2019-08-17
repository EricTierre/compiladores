import interface
import analisador_lex

def Interface():
	interface.janela.botao_abrirarquivo.clicked.connect(interface.CarregarArquivo)
	interface.janela.botao_lexico.clicked.connect(Lexico)
	interface.janela.botao_deletar.clicked.connect(interface.apagar)
	interface.janela.refreshbtn.clicked.connect(interface.Refresh)
	
	interface.janela.show()
	interface.app.exec()

def Lexico():
	lex = analisador_lex.Executar()
	
	#Passar ao lexer uma entrada
	lex.input(interface.janela.campotexto_arquivo.toPlainText())

	#Tokenize
	for tok in lex:
		interface.printar(tok)
		
if __name__ == "__main__":
	print('Executando...')
	
	Interface()
	Lexico()
	
	
	