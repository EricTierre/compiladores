import interface
import analisador_lex
import analisador_sin

def Interface():
    interface.janela.botao_abrirarquivo.clicked.connect(interface.CarregarArquivo)
    interface.Lexico.botao_lexico.clicked.connect(Lexico)
    interface.janela.botao_Run.clicked.connect(Run)
    interface.Sintatico.botao_sintatico.clicked.connect(Sintatico)
	
    ###menu###
    interface.janela.Open_Lexico.triggered.connect(ShowLex)
    interface.janela.Open_Sintatico.triggered.connect(ShowSin)
    interface.janela.action_Sair.triggered.connect(CloseALL)
    interface.janela.action_Abrir.triggered.connect(OpenFile)

    interface.janela.botao_zoomdown.clicked.connect(interface.ZoomDown)
    interface.janela.botao_zoomup.clicked.connect(interface.ZoomUp)

    interface.janela.show()
    interface.app.exec()

def CloseALL():
    interface.app.closeAllWindows()

def OpenFile():
    interface.CarregarArquivoOpenFile()
    
def ShowLex():
    interface.Lexico.show()
    
def ShowSin():
    interface.Sintatico.show()
    
def Lexico():
    interface.Lexico.campotexto_lexico.clear()
    interface.janela.campo_terminal.clear()
    
    lex = analisador_lex.Construir()
    lex.input(interface.janela.campotexto_arquivo.toPlainText())

    #Tokenize
    for tok in lex:
        interface.printar(tok)

def Sintatico():
    interface.Sintatico.campotexto_sintatico.clear()
    interface.janela.campo_terminal.clear()
    
    sin = analisador_sin.Construir()
    sin.parse(interface.janela.campotexto_arquivo.toPlainText(),lexer = analisador_lex.Construir(), tracking=True)
    analisador_sin.Imprimir_Regras()

def Run():
    Lexico()
    Sintatico()
    
if __name__ == "__main__":
    print('Executando...')
       
    Interface()	
    