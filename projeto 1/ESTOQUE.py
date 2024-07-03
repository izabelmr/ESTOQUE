# Dicionário para armazenar o estoque (produtos e quantidades)
estoque = {}

def exibir_estoque():
    #Exibe o estoque atual, listando os produtos e suas quantidades.
    print("Estoque atual:")
    for produto, quantidade in estoque.items():
        print(f"{produto}: {quantidade}") #exibe a mensagem

def adicionar_produto(produto, quantidade):
    #Adiciona um produto ao estoque ou atualiza sua quantidade.
    if produto in estoque: #verifica uma condição e executar um bloco de código se essa condição for verdadeira.
        estoque[produto] += quantidade
    else: #verifica múltiplas condições sequencialmente
        estoque[produto] = quantidade
    print(f"{quantidade} unidades de {produto} foram adicionadas ao estoque.") #exibe a mensagem

def remover_produto(produto):
    #Remove um produto do estoque.
    if produto in estoque: #verifica uma condição e executar um bloco de código se essa condição for verdadeira.
        del estoque[produto]
        print(f"{produto} foi removido do estoque.") #exibe a mensagem
    else: #verifica múltiplas condições sequencialmente
        print(f"{produto} não está no estoque.") #exibe a mensagem

def atualizar_estoque(produto, quantidade):
    #Atualiza a quantidade de um produto no estoque.
    if produto in estoque: #verifica uma condição e executar um bloco de código se essa condição for verdadeira.
        estoque[produto] = quantidade
        print(f"Estoque de {produto} atualizado para {quantidade}.") #exibe a mensagem
    else: #verifica múltiplas condições sequencialmente
        print(f"{produto} não está no estoque.") #exibe a mensagem

# Menu de opções
while True: # repete uma sequência de instruções um número desconhecido de vezes.
    print("\nOpções:")
    print("1 - Exibir estoque") #exibe a mensagem
    print("2 - Adicionar produto") #exibe a mensagem
    print("3 - Remover produto") #exibe a mensagem
    print("4 - Atualizar estoque") #exibe a mensagem
    print("5 - Sair") #exibe a mensagem
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1": #verifica uma condição e executar um bloco de código se essa condição for verdadeira.
        exibir_estoque()
    elif opcao == "2": #verifica múltiplas condições sequencialmente, abreviação de "else if"
        produto = input("Digite o nome do produto a ser adicionado: ")
        quantidade = int(input("Digite a quantidade a ser adicionada: "))
        adicionar_produto(produto, quantidade)
    elif opcao == "3": #verifica múltiplas condições sequencialmente, abreviação de "else if"
        produto = input("Digite o nome do produto a ser removido: ")
        remover_produto(produto)
    elif opcao == "4": #verifica múltiplas condições sequencialmente, abreviação de "else if"
        produto = input("Digite o nome do produto a ser atualizado: ")
        quantidade = int(input("Digite a nova quantidade em estoque: "))
        atualizar_estoque(produto, quantidade)
    elif opcao == "5": #verifica múltiplas condições sequencialmente, abreviação de "else if"
        break #usada para interromper imediatamente um laço de repetição.
    else: #verifica múltiplas condições sequencialmente
        print("Opção inválida. Tente novamente.") #exibe a mensagem
