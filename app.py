import requests

def buscar_endereco_por_cep(cep):
    """
    Consome a BrasilAPI para buscar dados de endereço de forma gratuita.
    Retorna um dicionário com os dados ou uma mensagem de erro.
    """
    cep_limpo = ''.join(filter(str.isdigit, cep))
    
    if len(cep_limpo) != 8:
        return {"erro": "CEP inválido. Deve conter 8 dígitos.", "sucesso": False}

    url = f"https://brasilapi.com.br/api/cep/v1/{cep_limpo}"
    
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            dados = response.json()
            return {
                "sucesso": True,
                "rua": dados.get("street"),
                "bairro": dados.get("neighborhood"),
                "cidade": dados.get("city"),
                "estado": dados.get("state")
            }
        else:
            return {"erro": "CEP não localizado na base de dados.", "sucesso": False}
    except requests.exceptions.RequestException:
        return {"erro": "Falha de conexão com o serviço de CEP.", "sucesso": False}

def adicionar_medicamento(lista, nome, horario):
    if not nome or not horario:
        return False
    lista.append({"nome": nome, "horario": horario})
    return True

def listar_medicamentos(lista):
    return lista

def menu():
    medicamentos = []
    
    print("       CUIDADO AMIGO - v1.1.0            ")
    
    cep = input("Para iniciar, digite seu CEP (ou Enter para pular): ")
    if cep:
        info_cep = buscar_endereco_por_cep(cep)
        if info_cep.get("sucesso"):
            print(f"\n📍 Localidade confirmada: {info_cep['rua']}, {info_cep['bairro']} - {info_cep['cidade']}/{info_cep['estado']}")
        else:
            print(f"\n⚠️ Não foi possível validar o CEP: {info_cep.get('erro')}")
            
    while True:
        print("\n--- Controle de Medicamentos ---")
        print("1. Adicionar Remédio")
        print("2. Listar Todos")
        print("3. Sair")
        opcao = input("Escolha: ")
        
        if opcao == "1":
            nome = input("Nome do remédio: ")
            hora = input("Horário (HH:MM): ")
            adicionar_medicamento(medicamentos, nome, hora)
        elif opcao == "2":
            lista = listar_medicamentos(medicamentos)
            if not lista:
                print("Nenhum remédio cadastrado ainda.")
            for m in lista:
                print(f"Remédio: {m['nome']} - Hora: {m['horario']}")
        elif opcao == "3":
            print("Saindo do sistema... Até logo!")
            break

if __name__ == "__main__":
    menu()
