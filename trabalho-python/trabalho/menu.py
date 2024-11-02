from produto import Produto

# Lista para armazenar os produtos cadastrados pelo usuário
produtos = []

def adicionar_produto() -> None:
    """Solicita ao usuário as informações de um novo produto e o adiciona à lista de produtos."""
    # Solicita ao usuário o nome, preço e quantidade do produto
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade do produto: "))
    
    # Cria uma nova instância da classe Produto e a adiciona à lista 'produtos'
    produto = Produto(nome, preco, quantidade)
    produtos.append(produto)
    print("Produto adicionado com sucesso!")

def exibir_produtos() -> None:
    """Exibe todos os produtos cadastrados, mostrando nome, preço e quantidade de cada um."""
    # Verifica se a lista 'produtos' está vazia
    if not produtos:
        print("Nenhum produto cadastrado.")
    else:
        # Percorre e exibe informações de cada produto na lista
        for produto in produtos:
            produto.exibir_informacoes()
            print("==============")  # Separador visual entre produtos

def atualizar_preco() -> None:
    """Permite ao usuário atualizar o preço de um produto específico pelo nome."""
    # Solicita o nome do produto para atualização
    nome = input("Digite o nome do produto para atualizar o preço: ")
    
    # Busca o produto na lista 'produtos' com base no nome fornecido
    produto = next((p for p in produtos if p.nome == nome), None)
    
    if produto:
        # Se o produto for encontrado, atualiza o preço com o valor inserido
        novo_preco = float(input(f"Digite o novo preço para '{nome}': "))
        produto.atualizar_preco(novo_preco)
    else:
        # Caso o produto não exista, informa que não foi encontrado
        print("Produto não encontrado.")

def atualizar_quantidade() -> None:
    """Permite ao usuário atualizar a quantidade de um produto específico pelo nome."""
    # Solicita o nome do produto para atualização de quantidade
    nome = input("Digite o nome do produto para atualizar a quantidade: ")
    
    # Busca o produto na lista 'produtos' pelo nome
    produto = next((p for p in produtos if p.nome == nome), None)
    
    if produto:
        # Se o produto for encontrado, atualiza a quantidade com o valor inserido
        nova_quantidade = int(input(f"Digite a nova quantidade para '{nome}': "))
        produto.atualizar_quantidade(nova_quantidade)
    else:
        # Informa que o produto não foi encontrado se ele não existir na lista
        print("Produto não encontrado.")

def menu() -> None:
    """Exibe o menu interativo e executa operações até que o usuário escolha sair."""
    while True:
        # Apresenta as opções do menu ao usuário
        print("\nMenu:")
        print("1. Adicionar Produto")
        print("2. Exibir Produtos")
        print("3. Atualizar Preço")
        print("4. Atualizar Quantidade")
        print("5. Sair")
        
        # Captura a opção escolhida pelo usuário
        opcao = input("Escolha uma opção: ")

        # Verifica a opção e executa a função correspondente
        if opcao == '1':
            adicionar_produto()
        elif opcao == '2':
            exibir_produtos()
        elif opcao == '3':
            atualizar_preco()
        elif opcao == '4':
            atualizar_quantidade()
        elif opcao == '5':
            # Encerra o programa quando a opção de sair é escolhida
            print("Saindo do programa...")
            break
        else:
            # Informa o usuário sobre uma entrada inválida
            print("Opção inválida. Tente novamente.")

# O programa inicia a execução do menu se este arquivo for o ponto de entrada
if __name__ == "__main__":
    menu()