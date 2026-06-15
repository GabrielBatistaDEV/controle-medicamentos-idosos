from unittest.mock import MagicMock, patch
import pytest
from app import app, buscar_cep


@pytest.fixture
def client():
    """Configura o cliente de testes do Flask."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


# === TESTES DE MEDICAMENTOS (ROTAS FLASK) ===


@patch("app.conectar_banco")
def test_adicionar_medicamento_sucesso(mock_conectar, client):
    """Valida se a rota POST responde com sucesso e traz a nova propriedade 'tomado'."""
    # Mock do banco de dados para não mexer no banco real durante o teste
    mock_conexao = MagicMock()
    mock_conectar.return_value = mock_conexao

    dados_envio = {"nome": "Dipirona", "horario": "08:00"}

    resposta = client.post("/medicamentos", json=dados_envio)
    dados_resposta = resposta.get_json()

    assert resposta.status_code == 201
    assert dados_resposta["mensagem"] == "Medicamento cadastrado com sucesso"

    # Valida se a sua NOVA funcionalidade está vindo no retorno do cadastro
    assert dados_resposta["medicamento"]["nome"] == "Dipirona"
    assert dados_resposta["medicamento"]["tomado"] is False


def test_adicionar_medicamento_vazio(client):
    """Valida se a API impede o cadastro de campos vazios (Erro 400)."""
    dados_invalidos = {"nome": "", "horario": ""}

    resposta = client.post("/medicamentos", json=dados_invalidos)
    dados_resposta = resposta.get_json()

    assert resposta.status_code == 400
    assert "erro" in dados_resposta


def test_adicionar_medicamento_horario_invalido(client):
    """Valida se a API rejeita horários em formatos textuais ou incorretos (Erro

    400).
    """
    dados_invalidos = {"nome": "Dipirona", "horario": "08 horas"}

    resposta = client.post("/medicamentos", json=dados_invalidos)
    dados_resposta = resposta.get_json()

    assert resposta.status_code == 400
    assert (
        "O horário deve estar no formato válido HH:MM" in dados_resposta["erro"]
    )


def test_adicionar_medicamento_horario_impossivel(client):
    """Valida se a API rejeita horas ou minutos que não existem, como 25:61 (Erro

    400).
    """
    dados_invalidos = {"nome": "Dipirona", "horario": "25:00"}

    resposta = client.post("/medicamentos", json=dados_invalidos)
    dados_resposta = resposta.get_json()

    assert resposta.status_code == 400
    assert (
        "O horário deve estar no formato válido HH:MM" in dados_resposta["erro"]
    )


@patch("app.conectar_banco")
def test_listar_medicamentos_inclui_status_tomado(mock_conectar, client):
    """Valida se a rota GET retorna a lista e se injeta corretamente o campo

    'tomado' como False para o controle do idoso.
    """
    # Simula o retorno do banco de dados: (id, nome, horario)
    mock_cursor = MagicMock()
    mock_cursor.fetchall.return_value = [(1, "Dipirona", "08:00")]

    mock_conexao = MagicMock()
    mock_conexao.cursor.return_value = mock_cursor
    mock_conectar.return_value = mock_conexao

    resposta = client.get("/medicamentos")
    dados_resposta = resposta.get_json()

    assert resposta.status_code == 200
    assert len(dados_resposta) == 1
    assert dados_resposta[0]["nome"] == "Dipirona"

    # Garante que a listagem está entregando a chave da nova funcionalidade
    assert dados_resposta[0]["tomado"] is False


# === TESTES DA API DE CEP (MANTIDOS E ADAPTADOS PARA A ROTA) ===


@patch("app.requests.get")
def test_buscar_endereco_por_cep_sucesso(mock_get, client):
    """Valida se a rota consegue interpretar corretamente o retorno de sucesso

    difundido pela BrasilAPI.
    """
    mock_resposta_api = {
        "cep": "01001000",
        "state": "SP",
        "city": "São Paulo",
        "neighborhood": "Sé",
        "street": "Praça da Sé",
    }

    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_resposta_api

    # Faz a requisição direto na rota da sua API Flask
    resposta = client.get("/cep/01001000")
    dados_resposta = resposta.get_json()

    assert resposta.status_code == 200
    assert dados_resposta["city"] == "São Paulo"
    assert dados_resposta["state"] == "SP"
    assert dados_resposta["street"] == "Praça da Sé"


def test_buscar_endereco_cep_curto_invalido(client):
    """Valida a regra de validação para CEPs com tamanho errado."""
    resposta = client.get("/cep/123")
    dados_resposta = resposta.get_json()

    assert dados_resposta["erro"] == "CEP inválido"