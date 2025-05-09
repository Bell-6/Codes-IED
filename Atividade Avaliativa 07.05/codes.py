tarefas = []            #Lista principal de tarefas
historico = []          #Pilha para desfazer tarefas
fila_execucao = []      #Fila para executar tarefas

def adicionar_tarefa(tarefa):  #Função para adicionar uma tarefa 
    # O metodo append Adiciona a tarefa à lista principal de tarefas, à pilha de histórico para desfazer,e à fila de execução.
    tarefas.append(tarefa)  
    historico.append(tarefa)  
    fila_execucao.append(tarefa) 
    print(f"Tarefa '{tarefa}' adicionada!\n") 

def desfazer_ultima_tarefa():  #Função para desfazer a última tarefa adicionada
    if historico:  #O if Verifica se há tarefas no histórico
        ultima = historico.pop()  #O pop remove a última tarefa do histórico(pilha)
        #O remove retira a tarefa da lista principal e da fila de execução
        tarefas.remove(ultima) 
        fila_execucao.remove(ultima)
        print(f"Tarefa '{ultima}' desfeita!\n")  #o print mostra mensagem no terminando confirmando a remoção
    else:  # o else está sendo usado caso não tenha tarefas no histórico
        print("Nenhuma tarefa para desfazer.\n")  #O print exibe uma mensagem informando que não há tarefas para desfazer

def atender_como_feita(): #Função para atender a próxima tarefa na fila
    if fila_execucao:  #O if verifica se há tarefas na fila de execução
        feita = fila_execucao.pop(0)  #O pop remove e retorna a primeira tarefa da fila
        tarefas.remove(feita)  #O remove retira a tarefa da lista principal
        print(f"Tarefa '{feita}' atendida!\n")  # O print mostra uma mensagem confirmando o atendimento da tarefa      
    else:  #o else é usado caso não tenha alguma tarefa na fila
        print("Nenhuma tarefa para atender.\n")  #O print mostra uma mensagem informando que não há tarefas para atendimento

def mostrar_tarefas():  #Função para mostrar todas as tarefas na lista principal
    print("\n📋 Lista de Tarefas:")  # O print mostra o título da lista
    for i, t in enumerate(tarefas):  #O for percorre pelas tarefas dentro da lista principal 'tarefas'
        print(f"{i + 1}. {t}")  #O print mostra cada tarefa com sua posição na lista
    print() #No print o vazio entre os parenteses é usado para separação visual 

while True:  #O while true é um Loop que analisa todo o codigo do programa para mostrar ao usuário no terminal

    #Os prints que contém as opções exibem o menu para o usuario escolher qual opção deseja
    print("1. Adicionar Tarefa")  
    print("2. Desfazer Última Tarefa")
    print("3. Atender Tarefa (modo fila)")
    print("4. Mostrar Tarefas")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")  #O input pede ao usuário que digite uma opção

    if opcao == '1':  #O if é usado quando o usuario digita 1 para adicionar uma tarefa
        tarefa = input("Digite a tarefa: ")  #O input pede ao usuário que digite a tarefa
        data_atual = input("Digite a data atual (dd/mm/aa): ") #O input pede ao usuário que digite a data atual
        data_conclu = input("Digite a data de conclusão (dd/mm/aa): ") #Pede ao usuário que digite a data de conclusão da tarefa
        adicionar_tarefa(f'{tarefa}, Inicio: ({data_atual}) - Fim: ({data_conclu})') #Chama a função para adicionar a tarefa com as informações ditas pelo usuário
    elif opcao == '2':  #O elif é usado quando o usuario digita 2 para desfazer a última tarefa
        desfazer_ultima_tarefa()  #Chama a função para desfazer a última tarefa
    elif opcao == '3':  #O elif é usado quando o usuario digita 3 para atende a tarefa
        atender_como_feita()  #Chama a função para atender a próxima tarefa
    elif opcao == '4':  #O elif é usado quando o usuario digita 4 para mostra as tarefas
        mostrar_tarefas()  #Chama a função para exibir as tarefas
    elif opcao == '5':  #Elif usado quando o usuario digitar 5 para sair do programa
        print("Saindo do programa...")  #O print mostra uma mensagem indicando que o programa está saindo
        break  #Break usado para encerrar o loop (while True)
    else:  #Else usado caso o usuário insira uma opção inválida
        print("Opção inválida!\n")  #Print mostra uma mensagem de erro

arquivo_nome = "list_task.txt" #Nome do arquivo para salvar as tarefas

if tarefas: #O if verifica se há tarefas na lista principal
    with open(arquivo_nome, "w") as file: #O open abre o arquivo para escrita e o w substituirá qualquer conteúdo existente
        for item in tarefas:#O for verificará cada tarefa na lista principal e in item será cada tarefa
            file.write(item + "\n")#O file escreve cada tarefa no arquivo,o \n separando cada uma por uma nova linhas

    print(f'Tudo list salva em {arquivo_nome}!') #O print mostra uma mensagem confirmando que as tarefas foram salvas no arquivo
