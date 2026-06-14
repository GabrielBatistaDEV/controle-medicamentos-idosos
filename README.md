# 🏥 Cuidado Amigo – Sistema de Controle de Medicamentos

## Bootcamp II – Desafio Entrega Final

### Integrantes

* Vinícius Martins
* Gabriel Batista Gomes
* João Pedro dos Santos
* Leonardo Ali
* Beatriz Saboia

---

# 📌 Visão Geral do Projeto

O **Cuidado Amigo** é uma aplicação desenvolvida para auxiliar idosos e cuidadores no controle de medicamentos.

O objetivo do sistema é facilitar o gerenciamento de horários e informações dos medicamentos, reduzindo riscos relacionados a esquecimento, confusão de horários e administração incorreta.

A aplicação foi evoluída de uma versão inicial em linha de comando para uma API web publicada em nuvem, utilizando banco de dados real para persistência das informações.

---

# 🎯 Problema e Impacto Social

Muitos idosos utilizam diversos medicamentos diariamente e podem enfrentar dificuldades para lembrar horários e organizar seus tratamentos.

O Cuidado Amigo busca oferecer uma solução simples para organizar essas informações, proporcionando maior segurança e autonomia para usuários e cuidadores.

---

# 🚀 Funcionalidades

## Funcionalidades iniciais

* Cadastro de medicamentos.
* Registro do nome do medicamento.
* Registro do horário de utilização.
* Listagem dos medicamentos cadastrados.
* Validação de informações obrigatórias.
* Consulta de endereço através do CEP utilizando a BrasilAPI.

---

## Funcionalidades implementadas na entrega final

* Migração da aplicação para uma API utilizando Flask.
* Integração com banco de dados PostgreSQL hospedado no Supabase.
* Persistência real dos medicamentos cadastrados.
* Consulta e retorno dos medicamentos armazenados no banco.
* Deploy da aplicação utilizando Render.
* Configuração de ambiente para execução em nuvem.
* Manutenção dos testes automatizados.
* Integração com GitHub Actions para validação do projeto.

---

# 🛠️ Tecnologias Utilizadas

* Python
* Flask
* PostgreSQL
* Supabase
* Render
* GitHub Actions
* BrasilAPI
* Pytest

---

# 🌐 Links

## Repositório GitHub

https://github.com/GabrielBatistaDEV/controle-medicamentos-idosos

## Aplicação Publicada

https://controle-medicamentos-idosos.onrender.com

---

# 🗄️ Banco de Dados

A aplicação utiliza PostgreSQL através do Supabase.

Tabela principal:

### medicamentos

| Campo   | Tipo   |
| ------- | ------ |
| id      | SERIAL |
| nome    | TEXT   |
| horario | TEXT   |

---

# ▶️ Como executar localmente

Clonar o repositório:

```bash
git clone https://github.com/GabrielBatistaDEV/controle-medicamentos-idosos
```

Instalar dependências:

```bash
pip install -r requirements.txt
```

Executar aplicação:

```bash
python app.py
```

---

# 👥 Trabalho Colaborativo

O desenvolvimento foi realizado utilizando GitHub com divisão de tarefas, branches, commits e Pull Requests revisados pelos integrantes da equipe.

Cada integrante realizou contribuições no projeto através do histórico do GitHub.

## Atualização da entrega final

Projeto atualizado com deploy em nuvem utilizando Render e banco PostgreSQL via Supabase.
