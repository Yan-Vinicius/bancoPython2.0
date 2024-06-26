class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

        def fazer_transacao(self, conta, transacao):
            transacao.registrar(conta)

        def add_conta(self, conta):
            self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, dt_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.dt_nascimento = dt_nascimento
        self.cpf = cpf


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico - Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, saldo, valor, limite_valor_saque, num_saques, limite_qtd_saque):

        saldo = self.saldo
        if num_saques >= limite_qtd_saque:
            print("Você não pode mais efetuar saques hoje o limite é de", limite_qtd_saque, "saques por dia")
        elif valor > limite_valor_saque:
            print("Você não pode efetuar esse saque, pois o limite para um saque é de", limite_valor_saque, "\n")
        elif valor > self.saldo:
            print("Você não possui saldo o suficiente em conta\n")
        elif valor > 0:
            saldo -= valor
            num_saques += 1
            print("Saque efetuado com sucesso")
        else:
            print("Saque falhou! Tente novamente")

        return saldo


    def depositar(self, deposito):

        if deposito > 0:
            self._saldo += deposito
            extrato = "Depósito: R$ ", deposito, "\n"
            print("Depósito feito com sucesso\n")

        else:
            print("Não foi possível fazer o depósito\n")

        return saldo


def mostrar_saldo():
    return print("O seu extrato é igual a R$", saldo, "\n")

def filtrar_user(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_user(usuarios):
    cpf = input("Informeo CPF (somente números): ")
    usuario = filtrar_user(cpf, usuarios)

    if usuario:
        print("Usuário já existente")
        return

    nome = input("Nome completo: ")
    dt_nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (rua, número - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": dt_nascimento, "cpf": cpf, "endereço": endereco})
    print("Usuário adicionado com sucesso!")

def lista_contas(contas):
    for conta in contas:
        linha = f"""
        Agencia: {conta['agencia']}
        Conta corrente: {conta['num_conta']}
        Titular: {conta['usuario']['nome']}
        """
        print(linha)

def criar_conta(agencia, num_conta, usuarios):
    cpf = input("Digite o cpf do usuário: ")
    usuario = filtrar_user(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso")
        return {"agencia": agencia, "número_conta": num_conta, "usuario": usuario}

    print("Usuário não encontrado!!")


saldo = 0
extrato = ""
limite_valor_saque = 500.00
limite_qtd_saque = 3
num_saques = 0
usuarios = []
contas = []
agencia = "0001"

while True:

    opcao = input("Escolha uma opção: \n"
                  "1 - Depósito\n"
                  "2 - Saque\n"
                  "3 - Extrato\n"
                  "4 - Novo usuário\n"
                  "5 - Listar contas\n"
                  "6 - Nova conta\n"
                  "0 - Sair\n")

    if opcao == "0":
        break

    elif opcao == "1":
        deposito = float(input("Digite o valor do seu depósito: "))
        saldo, extrato = depositar(saldo, deposito, extrato)

    elif opcao == "2":
        valor = float(input("Digite o valor do seu saque: "))
        saldo = sacar(saldo, valor, limite_valor_saque, num_saques, limite_qtd_saque)

    elif opcao == "3":
        mostrar_saldo()

    elif opcao == "4":
        criar_user(usuarios)

    elif opcao == "5":
        lista_contas(contas)

    elif opcao == "6":
        num_conta = len(contas) + 1
        conta = criar_conta(agencia, num_conta, usuarios)
        if conta:
            contas.append(conta)

    else:
        print("Opção inválida\n")
