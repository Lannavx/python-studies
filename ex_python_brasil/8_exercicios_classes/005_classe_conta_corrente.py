'''Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. 
A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. 
Os métodos são os seguintes: alterarNome, depósito e saque; 
No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.'''

class ContaCorrente():
    def __init__(self, numero_conta: int, correntista: str, saldo: float = 0):
        self.numero_conta = numero_conta
        self.correntista = correntista
        self.saldo = saldo

    def alterarNome(self, novo_valor: str) -> None:
        self.correntista = novo_valor

    def deposito(self, valor_deposito: float) -> None:
        self.saldo += valor_deposito
        print(f'+ R${valor_deposito}')

    def saque(self, valor_saque: float) -> None:
        self.saldo -= valor_saque 
        print(f'- R${valor_saque}')          


correntista_um = ContaCorrente(4355, 'Lucia', 6000)

correntista_um.deposito(100)
print(f'Saldo atual: R${correntista_um.saldo}')
correntista_um.saque(5000)
print(f'Saldo atual: R${correntista_um.saldo}')