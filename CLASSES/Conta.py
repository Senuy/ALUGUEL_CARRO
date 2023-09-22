class Conta:
    def __init__(self, num_conta, nome, saldo):  # método construtor
        self.num_conta = num_conta
        self.nome = nome
        self.saldo = saldo

    def cadastrar(self) -> bool:
        try:
            self.num_conta = self.num_conta
            self.nome = self.nome
            self.saldo = self.saldo
            return True
        except:
            return False

    def depositar(self, valor) -> bool:
        try:
            self.saldo += valor
            return True
        except:
            return False

    def sacar(self, valor) -> bool:
        if self.saldo >= valor:
            self.saldo -= valor
            return True
        else:
            return False

    def listarDados(self) -> str:
        dados = {"Número da Conta: ": self.num_conta,
                 "Nome: ": self.nome,
                 "Saldo R$": self.saldo}
        return dados
