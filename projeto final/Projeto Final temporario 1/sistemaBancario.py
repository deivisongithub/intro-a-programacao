from validacaoDados import ValidacaoDados
from caixaEletronico import CaixaEletronico


tela = ValidacaoDados()
tela.Iniciar()

if type(tela) != bool:

    tela_sec = CaixaEletronico()
    tela_sec.Inic()
