from datetime import datetime  # <-- NOVO IMPORT para validação de horário
import os
from flask import Flask, jsonify, request
import psycopg2
import requests
from datetime import datetime

app = Flask(__name__)

# CONFIGURAÇÃO DO BANCO

DB_HOST = "db.tganllgynuakgqpsszpf.supabase.co"
DB_PORT = "5432"
DB_NAME = "postgres"
DB_USER = "postgres"

DB_PASSWORD = os.getenv("DB_PASSWORD")


def conectar_banco():
    """
    Conecta ao banco PostgreSQL do Supabase.
    """
    try:
        conexao = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
        )
        return conexao
    except Exception as erro:
        print(f"Erro ao conectar no banco: {erro}")
        return None


# ROTA INICIAL


@app.route("/")
def inicio():
    return jsonify(
        {
            "projeto": "Cuidado Amigo",
            "status": "online",
            "mensagem": "API funcionando corretamente",
        }
    )


# BRASIL API - CEP


@app.route("/cep/<cep>")
def buscar_cep(cep):
    cep_limpo = "".join(filter(str.isdigit, cep))
    if len(cep_limpo) != 8:
        return jsonify({"erro": "CEP inválido"})

    url = f"https://brasilapi.com.br/api/cep/v1/{cep_limpo}"

    try:
        resposta = requests.get(url, timeout=5)
        return jsonify(resposta.json())
    except Exception:
        return jsonify({"erro": "Falha ao consultar CEP"})


# LISTAR MEDICAMENTOS


@app.route("/medicamentos", methods=["GET"])
def listar_medicamentos():
    conexao = conectar_banco()
    if conexao is None:
        return jsonify({"erro": "Banco indisponível"})

    cursor = conexao.cursor()

    # Alterado de 'ORDER BY id' para 'ORDER BY horario ASC'

    cursor.execute(
        """
        SELECT id, nome, horario
        FROM medicamentos
        ORDER BY horario ASC;
        """
    )

    medicamentos = cursor.fetchall()

    cursor.close()
    conexao.close()

    lista = []

    for medicamento in medicamentos:
        lista.append(
            {
                "id": medicamento[0],
                "nome": medicamento[1],
                "horario": medicamento[2],
                "tomado": False,  
            }
        )

    return jsonify(lista)


# CADASTRAR MEDICAMENTO


@app.route("/medicamentos", methods=["POST"])
def adicionar_medicamento():
    dados = request.json
    nome = dados.get("nome")
    horario = dados.get("horario")

    # Validação
    if not nome or not horario:
        return (
            jsonify({"erro": "Nome e horário são obrigatórios"}),
            400,
        )

    # Nova validação: formato do horário
    try:
        datetime.strptime(horario, "%H:%M")
    except ValueError:
        return (
            jsonify(
                {
                    "erro": "O horário deve estar no formato válido HH:MM (ex: 08:30 ou 22:00)"
                }
            ),
            400,
        )

    conexao = conectar_banco()

    if conexao is None:
        return jsonify({"erro": "Banco indisponível"})

    cursor = conexao.cursor()
    cursor.execute(
        """
        INSERT INTO medicamentos(nome, horario)
        VALUES(%s,%s);
        """,
        (nome, horario),
    )

    conexao.commit()

    cursor.close()
    conexao.close()

    # Retorna o objeto completo criado, incluindo o status padrão da nova feature
    return (
        jsonify(
            {
                "mensagem": "Medicamento cadastrado com sucesso",
                "medicamento": {
                    "nome": nome,
                    "horario": horario,
                    "tomado": False,  # <-- Nova funcionalidade integrada na resposta do cadastro
                },
            }
        ),
        201,
    )

        "mensagem": "Medicamento cadastrado com sucesso"

    })
    # REMOVER MEDICAMENTO

@app.route("/medicamentos/<int:id>", methods=["DELETE"])
def remover_medicamento(id):

    conexao = conectar_banco()

    if conexao is None:
        return jsonify({
            "erro": "Banco indisponível"
        }), 500

    cursor = conexao.cursor()

    cursor.execute(
        """
        DELETE FROM medicamentos
        WHERE id = %s
        RETURNING id;
        """,
        (id,)
    )

    removido = cursor.fetchone()

    conexao.commit()

    cursor.close()
    conexao.close()

    if removido is None:
        return jsonify({
            "erro": "Medicamento não encontrado"
        }), 404

    return jsonify({
        "mensagem": "Medicamento removido com sucesso"
    }), 200

# EXECUÇÃO LOCAL

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)