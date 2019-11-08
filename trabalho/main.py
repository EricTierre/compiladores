import interface
import analisador_lex
import analisador_sin

def Interface():
    interface.janela.botao_abrirarquivo.clicked.connect(interface.CarregarArquivo)
    interface.janela.botao_Run.clicked.connect(Run)
    #interface.Sintatico.botao_sintatico.clicked.connect(Sintatico)
    #interface.Lexico.botao_lexico.clicked.connect(Lexico)
	
    ###menu###
    interface.janela.Open_Lexico.triggered.connect(ShowLex)
    interface.janela.Open_Semantico.triggered.connect(ShowSem)
    interface.janela.Open_Sintatico.triggered.connect(ShowSin)
    interface.janela.Open_Tabela.triggered.connect(ShowTab)
    interface.janela.action_Sair.triggered.connect(CloseALL)
    interface.janela.action_Abrir.triggered.connect(OpenFile)
    interface.janela.action_Salvar.triggered.connect(SaveFile)
    
    interface.janela.botao_zoomdown.clicked.connect(interface.ZoomDown)
    interface.janela.botao_zoomup.clicked.connect(interface.ZoomUp)

    interface.janela.show()
    interface.app.exec()

def CloseALL():
    interface.app.closeAllWindows()

def OpenFile():
    interface.CarregarArquivoOpenFile()
    
def SaveFile():
    interface.SalvarArquivo()
    
def ShowLex():
    interface.Lexico.show()
    
def ShowSem():
    interface.Semantico.show()
    
def ShowSin():
    interface.Sintatico.show()

def ShowTab():
    interface.Tabela.show()
    
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
    interface.Semantico.campotexto_semantico.clear()
    interface.janela.campo_terminal.clear()
    interface.Tabela.campotexto_tabela.clear()
    
    sin = analisador_sin.Construir()
    sin.parse(interface.janela.campotexto_arquivo.toPlainText(),lexer = analisador_lex.Construir(), tracking=True)
    analisador_sin.Imprimir_Regras()
    analisador_sin.Imprimir_Regras_Anotadas()

def Run():
    Lexico()
    Sintatico()
    
if __name__ == "__main__":
    print('Executando...')
       
    Interface()	
    