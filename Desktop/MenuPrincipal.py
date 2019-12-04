from Auxiliar import Auxiliar

opcao = 0

while opcao != 7:
    opcao = Auxiliar.exibeMenu()

    if opcao == 1:
        Auxiliar.cadastraPessoa()
    if opcao == 2:
        Auxiliar.listarPessoas()
    if opcao == 3:
        Auxiliar.cadastraBebida()
    if opcao == 4:
        Auxiliar.listarBebidas()
    if opcao == 5:
        Auxiliar.cadastraPedido()
    if opcao == 6:
        Auxiliar.listaPedidos()