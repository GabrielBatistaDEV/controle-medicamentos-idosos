def adicionar_medicamento(lista, nome, horario):
    if not nome or not horario:
        return False
    lista.append({"nome": nome, "horario": horario})
    return True

def listar_medicamentos(lista):
    return lista

def menu():
    medicamentos = []
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
            for m in listar_medicamentos(medicamentos):
                print(f"Remédio: {m['nome']} - Hora: {m['horario']}")
        elif opcao == "3":
            break

if __name__ == "__main__":
    menu()