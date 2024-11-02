class Produto:
    def __init__(self, nome: str, preco: float, quantidade: int) -> None:
        """
        Construtor da classe Produto. Inicializa o produto com os valores fornecidos.

        Args:
            nome (str): Nome do produto.
            preco (float): Preço do produto.
            quantidade (int): Quantidade disponível do produto.
        """
        # Atributos de instância que armazenam informações sobre o produto
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def exibir_informacoes(self) -> None:
        """Exibe as informações do produto formatadas para facilitar a leitura."""
        print("Informações do Produto:")
        print(f"Nome: {self.nome}")
        print(f"Preço: R$ {self.preco:.2f}")
        print(f"Quantidade: {self.quantidade}")

    def atualizar_preco(self, novo_preco: float) -> None:
        """Atualiza o preço do produto para um novo valor.

        Args:
            novo_preco (float): Novo preço do produto.
        """
        # Atualiza o atributo preco com o novo valor e confirma a atualização
        self.preco = novo_preco
        print(f"Preço atualizado para R$ {self.preco:.2f}")

    def atualizar_quantidade(self, nova_quantidade: int) -> None:
        """Atualiza a quantidade do produto para um novo valor.

        Args:
            nova_quantidade (int): Nova quantidade do produto.
        """
        # Atualiza o atributo quantidade e confirma a atualização
        self.quantidade = nova_quantidade
        print(f"Quantidade atualizada para {self.quantidade}")