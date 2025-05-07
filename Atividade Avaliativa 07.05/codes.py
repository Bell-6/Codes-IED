tarefas = []            #Lista principal de tarefas
historico = []          #Pilha para desfazer tarefas
fila_execucao = []      #Fila para executar tarefas

def adicionar_tarefa(tarefa):  #Função para adicionar uma tarefa 
    tarefas.append(tarefa)  #Adiciona a tarefa à lista principal de tarefas
    historico.append(tarefa)  #Adiciona a tarefa à pilha de histórico para desfazer
    fila_execucao.append(tarefa)  #Adiciona a tarefa à fila de execução
    print(f"Tarefa '{tarefa}' adicionada!\n")  #Mostra a mensagem confirmando que a tarefa foi adicionada

def desfazer_ultima_tarefa():  #Função para desfazer a última tarefa adicionada
    if historico:  #Verifica se há tarefas no histórico
        ultima = historico.pop()  #Remove a última tarefa do histórico(pilha)
        tarefas.remove(ultima)  #Remove a tarefa da lista principal
        fila_execucao.remove(ultima)  #Remove a tarefa da fila de execução
        print(f"Tarefa '{ultima}' desfeita!\n")  #Mostra mensagem no terminando confirmando a remoção
    else:  # Caso não tenha tarefas no histórico
        print("Nenhuma tarefa para desfazer.\n")  #Exibe uma mensagem informando que não há tarefas para desfazer

def atender_como_feita(): #Função para atender a próxima tarefa na fila
    if fila_execucao:  #Verifica se há tarefas na fila de execução
        feita = fila_execucao.pop(0)  #Remove a primeira tarefa da fila
        tarefas.remove(feita)  #Remove a tarefa da lista principal
        print(f"Tarefa '{feita}' atendida!\n")  #Mostra uma mensagem confirmando o atendimento da tarefa      
    else:  #Caso não tenha alguma tarefa na fila
        print("Nenhuma tarefa para atender.\n")  #Mostra uma mensagem informando que não há tarefas para atendimento

def mostrar_tarefas():  #Função para mostrar todas as tarefas na lista principal
    print("\n📋 Lista de Tarefas:")  #Mostra o título da lista
    for i, t in enumerate(tarefas):  #Itera sobre as tarefas com índice
        print(f"{i + 1}. {t}")  #Mostra cada tarefa com sua posição na lista
    print() #Vazio entre os parenteses para separação visual 

while True:  #Loop que analisa todo o codigo do programa para mostrar ao usuário no terminal

    #Exibe o menu para o usuario escolher qual opção deseja
    print("1. Adicionar Tarefa")  
    print("2. Desfazer Última Tarefa")
    print("3. Atender Tarefa (modo fila)")
    print("4. Mostrar Tarefas")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")  #Pede ao usuário que escolha uma opção

    if opcao == '1':  #Adiciona uma tarefa
        tarefa = input("Digite a tarefa: ")  #Pede ao usuário que digite a tarefa
        data_atual = input("Digite a data atual (dd/mm/aa): ") #Pede ao usuário que digite a data atual
        data_conclu = input("Digite a data de conclusão (dd/mm/aa): ") #Pede ao usuário que digite a data de conclusão da tarefa
        adicionar_tarefa(f'{tarefa}, Inicio: ({data_atual}) - Fim: ({data_conclu})') #Chama a função para adicionar a tarefa com as informações ditas pelo usuário
    elif opcao == '2':  #Desfaz a última tarefa
        desfazer_ultima_tarefa()  #Chama a função para desfazer a última tarefa
    elif opcao == '3':  #Atende a tarefa
        atender_como_feita()  #Chama a função para atender a próxima tarefa
    elif opcao == '4':  #Mostra as tarefas
        mostrar_tarefas()  #Chama a função para exibir as tarefas
    elif opcao == '5':  #Saí do programa
        print("Saindo do programa...")  #Mostra uma mensagem indicando que o programa está saindo
        break  #Encerra o loop (while True)
    else:  #Caso o usuário insira uma opção inválida
        print("Opção inválida!\n")  #Mostra uma mensagem de erro

arquivo_nome = "list_task.txt" #Nome do arquivo para salvar as tarefas

if tarefas: #Verifica se há tarefas na lista principal
    with open(arquivo_nome, "w") as file: #Abre o arquivo para escrita
        for item in tarefas:#Itera sobre as tarefas
            file.write(item + "\n")#Escreve cada tarefa no arquivo, separando cada uma por uma nova linhas

    print(f'Tudo list salva em {arquivo_nome}!') #Mostra uma mensagem confirmando que as tarefas foram salvas no arquivo
