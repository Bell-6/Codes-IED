dados_usuario = []
usuario = {}
transporte = {}

def cadastrar_usuario(e):
    dados_usuario.append(e)

def mostrar_usuario():
    print(dados_usuario)

def deletar_usuario():
    dados_usuario.pop(0)

while True:
    print()
    print("---- Cadastro de Usuário ----")
    print()
    opc = int(input( " | Digite 1 para cadastrar \n | Digite 2 para mostrar\n | Digite 3 para deletar\n | Digite 4 para sair\n"))
    match opc:
        case 1:
            usuario["transporte"] = transporte
            usuario["nome"] = input("Digite o nome:")
            usuario["Cidade"] = input ("Digite a cidade:")
            usuario["Idade"] = int(input("Digite a sua idade:"))

            transporte["pos_transporte"] = input("Você utiliza transporte?(Sim/Não)")

            if transporte["pos_transporte"] == "sim":
                transporte["modelo"] = input("qual o modelo do transporte?")
                transporte["cor"] = input("qual a cor do transporte?")
                transporte["placa"] = input("qual a placa do transporte?")
                cadastrar_usuario(usuario)
            else:
                cadastrar_usuario(usuario)
        case 2:
            mostrar_usuario() 
        
        case 3:
            deletar_usuario()

        case 4:    
            print("Saindo do programa...")
            break

        