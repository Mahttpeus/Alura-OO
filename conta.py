# 'self' é um valor implicito, ou seja, quando chamarmos uma conta


class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo uma conta...")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    # metodos

    def extrato(self):
        print("O titlular {} tem o valor de {} na conta".format(self.__titular, self.__saldo))

    def depositar(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def sacar(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print("O valor {} foi maior que seu limite".format(valor))

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    @property   # GET
    def saldo(self):
        return self.__saldo

    @property # GET
    def limite(self):
        return self.__limite

    @property # GET
    def titular(self):
        return self.__titular

    @property   # GET
    def limite(self):
        return self.__limite

    @limite.setter  # SET
    def limite(self, limite):
        self.__limite = limite

    @staticmethod  # Qnd definimos um método estático, ou seja, de classe, podemos chamá-lo sem a necessidade de criação de um objeto antes.
    def codigo_banco():
        return '001'

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco':'237'}