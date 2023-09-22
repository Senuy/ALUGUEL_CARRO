import sqlite3

banco = sqlite3.connect('db_conta.db')
cursor = banco.cursor()


# criar o banco
# cursor.execute("CREATE TABLE  conta (num_conta integer, nome text, valor float)")

class ContaDb:
    def __init__(self, num_conta, nome, saldo):
        self.num_conta = num_conta
        self.nome = nome
        self.saldo = saldo

    def cadastro(self) -> bool:
        try:
            self.num_conta = self.num_conta
            self.nome = self.nome
            self.saldo = self.saldo
            cursor.execute("INSERT INTO conta VALUES " + str(self.num_conta) + ",'" + self.nome + "'," + str(self.saldo)+ "")
            return True
        except:
            return False
