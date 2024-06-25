import re
 
def validar_cpf(cpf):
    cpf = re.sub(r'\D', '', cpf)  # Remove todos os caracteres não numéricos
    return len(cpf) == 11
 
def validar_cnpj(cnpj):
    cnpj = re.sub(r'\D', '', cnpj)  # Remove todos os caracteres não numéricos
    return len(cnpj) == 14
 
def validar_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None 
 
def validar_cep(cep):
    cep = re.sub(r'\D', '', cep)  # Remove todos os caracteres não numéricos
    return len(cep) == 8
 
def validar_telefone(telefone):
    telefone = re.sub(r'\D', '', telefone)  # Remove todos os caracteres não numéricos
    return len(telefone) >= 10
 
 
# Listas para armazenar os dados
usuarios_comuns = []
pontos_de_coleta = []
entregadores = []
empresas = []
 
# Funções de cadastro
def cadastrar_usuario_comum():
    cpf = input("Digite o CPF: ")
    if not validar_cpf(cpf):
        print("CPF inválido!")
        return
    email = input("Digite o email: ")
    if not validar_email(email):
        print("Email inválido!")
        return
    senha = input("Digite a senha: ")
    usuario = {'cpf': cpf, 'email': email, 'senha': senha}
    usuarios_comuns.append(usuario)
    print("Usuário comum cadastrado com sucesso!")
 
def cadastrar_ponto_de_coleta():
    cep = input("Digite o CEP: ")
    if not validar_cep(cep):
        print("CEP inválido!")
        return
    numero_residencial = input("Digite o número residencial: ")
    telefone = input("Digite o telefone: ")
    if not validar_telefone(telefone):
        print("Telefone inválido!")
        return
    ponto = {'cep': cep, 'numero_residencial': numero_residencial, 'telefone': telefone}
    pontos_de_coleta.append(ponto)
    print("Ponto de coleta cadastrado com sucesso!")
 
def cadastrar_entregador():
    cpf = input("Digite o CPF: ")
    if not validar_cpf(cpf):
        print("CPF inválido!")
        return
    email = input("Digite o email: ")
    if not validar_email(email):
        print("Email inválido!")
        return
    senha = input("Digite a senha: ")
    numero = input("Digite o número de telefone: ")
    if not validar_telefone(numero):
        print("Telefone inválido!")
        return
    cep = input("Digite o CEP: ")
    if not validar_cep(cep):
        print("CEP inválido!")
        return
    residencial = input("Digite o número residencial: ")
    placa = input("Digite a placa do veículo: ")
    entregador = {'cpf': cpf, 'email': email, 'senha': senha, 'numero': numero, 'cep': cep, 'residencial': residencial, 'placa': placa}
    entregadores.append(entregador)
    print("Entregador cadastrado com sucesso!")
 
def cadastrar_empresa():
    cnpj = input("Digite o CNPJ: ")
    if not validar_cnpj(cnpj):
        print("CNPJ inválido!")
        return
    email_representante = input("Digite o email do representante: ")
    if not validar_email(email_representante):
        print("Email inválido!")
        return
    cep = input("Digite o CEP: ")
    if not validar_cep(cep):
        print("CEP inválido!")
        return
    numero_sede = input("Digite o número da sede: ")
    tipo_pagamento = input("Digite o tipo de pagamento: ")
    empresa = {'cnpj': cnpj, 'email_representante': email_representante, 'cep': cep, 'numero_sede': numero_sede, 'tipo_pagamento': tipo_pagamento}
    empresas.append(empresa)
    print("Empresa cadastrada com sucesso!")
 
# Funções para listar, consultar e remover usuários
def listar_usuarios():
    print("Usuários Comuns:")
    for usuario in usuarios_comuns:
        print(usuario)
   
    print("Pontos de Coleta:")
    for ponto in pontos_de_coleta:
        print(ponto)
   
    print("Entregadores:")
    for entregador in entregadores:
        print(entregador)
   
    print("Empresas:")
    for empresa in empresas:
        print(empresa)
 
def consultar_usuario():
    tipo_usuario = input("Digite o tipo de usuário (comum, ponto de coleta, entregador, empresa): ").strip()
    if tipo_usuario == 'comum':
        cpf = input("Digite o CPF: ")
        for usuario in usuarios_comuns:
            if usuario['cpf'] == cpf:
                print("Usuário encontrado:", usuario)
                return
        print("Usuário não encontrado.")
    elif tipo_usuario == 'ponto de coleta':
        cep = input("Digite o CEP: ")
        for ponto in pontos_de_coleta:
            if ponto['cep'] == cep:
                print("Ponto de coleta encontrado:", ponto)
                return
        print("Ponto de coleta não encontrado.")
    elif tipo_usuario == 'entregador':
        cpf = input("Digite o CPF: ")
        for entregador in entregadores:
            if entregador['cpf'] == cpf:
                print("Entregador encontrado:", entregador)
                return
        print("Entregador não encontrado.")
    elif tipo_usuario == 'empresa':
        cnpj = input("Digite o CNPJ: ")
        for empresa in empresas:
            if empresa['cnpj'] == cnpj:
                print("Empresa encontrada:", empresa)
                return
        print("Empresa não encontrada.")
    else:
        print("Tipo de usuário inválido.")
 
def remover_usuario():
    tipo_usuario = input("Digite o tipo de usuário (comum, ponto de coleta, entregador, empresa): ").strip().lower()
    if tipo_usuario == 'comum':
        cpf = input("Digite o CPF: ")
        for usuario in usuarios_comuns:
            if usuario['cpf'] == cpf:
                usuarios_comuns.remove(usuario)
                print("Usuário comum removido com sucesso!")
                return
        print("Usuário não encontrado.")
    elif tipo_usuario == 'ponto de coleta':
        cep = input("Digite o CEP: ")
        for ponto in pontos_de_coleta:
            if ponto['cep'] == cep:
                pontos_de_coleta.remove(ponto)
                print("Ponto de coleta removido com sucesso! ")
                return
        print("Ponto de coleta não encontrado.")
    elif tipo_usuario == 'entregador':
        cpf = input("Digite o CPF: ")
        for entregador in entregadores:
            if entregador['cpf'] == cpf:
                entregadores.remove(entregador)
                print("Entregador removido com sucesso!")
                return
        print("Entregador não encontrado.")
    elif tipo_usuario == 'empresa':
        cnpj = input("Digite o CNPJ: ")
        for empresa in empresas:
            if empresa['cnpj'] == cnpj:
                empresas.remove(empresa)
                print("Empresa removida com sucesso!")
                return
        print("Empresa não encontrada.")
    else:
        print("Tipo de usuário inválido.")
 
# Função de login
def login():
    tipo_usuario = input("Digite o tipo de usuário (comum, entregador, empresa): ").strip()
    if tipo_usuario == 'comum':
        cpf = input("Digite o CPF: ")
        senha = input("Digite a senha: ")
        for usuario in usuarios_comuns:
            if usuario['cpf'] == cpf and usuario['senha'] == senha:
                print("Login bem-sucedido!")
                return
        print("CPF ou senha inválidos!")
    elif tipo_usuario == 'entregador':
        cpf = input("Digite o CPF: ")
        senha = input("Digite a senha: ")
        for entregador in entregadores:
            if entregador['cpf'] == cpf and entregador['senha'] == senha:
                print("Login bem-sucedido!")
                return
        print("CPF ou senha inválidos!")
    elif tipo_usuario == 'empresa':
        cnpj = input("Digite o CNPJ: ")
        senha = input("Digite a senha: ")
        for empresa in empresas:
            if empresa['cnpj'] == cnpj and empresa['senha'] == senha:
                print("Login bem-sucedido!")
                return
        print("CNPJ ou senha inválidos!")
    else:
        print("Tipo de usuário inválido!")
 
# Menu principal
def menu():
    while True:
        print("\nMenu:")
        print("1. Cadastrar Usuário Comum")
        print("2. Cadastrar Ponto de Coleta")
        print("3. Cadastrar Entregador")
        print("4. Cadastrar Empresa")
        print("5. Login")
        print("6. Listar Usuários")
        print("7. Consultar Usuário")
        print("8. Remover Usuário")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")
       
        if opcao == '1':
            cadastrar_usuario_comum()
        elif opcao == '2':
            cadastrar_ponto_de_coleta()
        elif opcao == '3':
            cadastrar_entregador()
        elif opcao == '4':
            cadastrar_empresa()
        elif opcao == '5':
            login()
        elif opcao == '6':
            listar_usuarios()
        elif opcao == '7':
            consultar_usuario()
        elif opcao == '8':
            remover_usuario()
        elif opcao == '0':
            break
        else:
            print("Opção inválida!")
 
if __name__ == "__main__":
    menu()
 