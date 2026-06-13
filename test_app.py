from unittest.mock import patch
from app import adicionar_medicamento, buscar_endereco_por_cep


def test_adicionar_medicamento_sucesso():
    lista = []
    assert adicionar_medicamento(lista, "Dipirona", "08:00") is True
    assert len(lista) == 1


def test_adicionar_medicamento_vazio():
    lista = []
    assert adicionar_medicamento(lista, "", "") is False


def test_lista_comeca_vazia():
    lista = []
    assert len(lista) == 0


def test_buscar_endereco_por_cep_sucesso():
    """
    Valida se a função consegue interpretar corretamente o retorno de sucesso.
    """
    mock_resposta_api = {
        "cep": "01001000",
        "state": "SP",
        "city": "São Paulo",
        "neighborhood": "Sé",
        "street": "Praça da Sé"
    }

    with patch('app.requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_resposta_api

        resultado = buscar_endereco_por_cep("01001000")

        assert resultado["sucesso"] is True
        assert resultado["cidade"] == "São Paulo"
        assert resultado["estado"] == "SP"
        assert resultado["rua"] == "Praça da Sé"


def test_buscar_endereco_cep_curto_invalido():
    """
    Valida a regra de limite/validação para CEPs com tamanho errado.
    """
    resultado = buscar_endereco_por_cep("123")
    assert resultado["sucesso"] is False
    assert "erro" in resultado
