import interface
import analisador_lex
import analisador_sin

def Interface():
    interface.janela.botao_abrirarquivo.clicked.connect(interface.CarregarArquivo)
    interface.janela.botao_lexico.clicked.connect(Lexico)
    interface.janela.botao_deletar.clicked.connect(interface.apagar)
    interface.janela.botao_sintatico.clicked.connect(Sintatico)
    interface.janela.botao_deletar_2.clicked.connect(interface.apagar2)
    interface.janela.refreshbtn.clicked.connect(interface.Refresh)
	
    interface.janela.botao_zoomdown.clicked.connect(interface.ZoomDown)
    interface.janela.botao_zoomup.clicked.connect(interface.ZoomUp)

    interface.janela.show()
    interface.app.exec()

def Lexico():
    lex = analisador_lex.Construir()
	
    #Passar ao lexer uma entrada
    lex.input(interface.janela.campotexto_arquivo.toPlainText())

    #Tokenize
    for tok in lex:
        interface.printar(tok)

def Sintatico():
    sin = analisador_sin.Construir()
    sin.parse(interface.janela.campotexto_arquivo.toPlainText(), tracking=True)
    analisador_sin.Imprimir_Regras()
    
if __name__ == "__main__":
    print('Executando...')

    Interface()
    #Lexico()
    #Sintatico()
	
	
	