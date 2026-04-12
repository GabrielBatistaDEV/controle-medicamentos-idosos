from app import adicionar_medicamento

def test_adicionar_medicamento_sucesso():
    lista = []
    assert adicionar_medicamento(lista, "Dipirona", "08:00") is True
    assert len(lista) == 1

def test_adicionar_medicamento_vazio():
    lista = []
    # Teste de entrada inválida (requisito do trabalho)
    assert adicionar_medicamento(lista, "", "") is False

def test_lista_comeca_vazia():
    lista = []
    assert len(lista) == 0