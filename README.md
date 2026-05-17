Sistema de Controle de Medicamentos - Cuidado Amigo

## Visão Geral
Este projeto é uma aplicação CLI (Interface de Linha de Comando) desenvolvida para auxiliar idosos e cuidadores na organização de rotinas de medicação. O foco é mitigar o problema do esquecimento e da confusão de horários, garantindo maior segurança na administração de remédios.

## Problema Real e Impacto Social
Muitos idosos convivem com a polifarmácia (uso de vários medicamentos diários). A dificuldade em memorizar horários pode causar interações medicamentosas perigosas ou falta de tratamento. O Cuidado Amigo oferece uma solução digital simples para listar e organizar esses dados, promovendo autonomia e saúde.

## Funcionalidades
* **Adicionar Medicamento:** Registro do nome e do horário (HH:MM).
* **Listar Medicamentos:** Exibição clara de todos os itens cadastrados.
* **Validação:** Impede o cadastro de campos vazios para evitar erros de registro.

## Tecnologias Utilizadas
* **Linguagem:** Python 3.10+
* **Testes:** Pytest (para validação das regras de negócio).
* **Linting:** Flake8 (para garantia de qualidade e estilo de código).
* **CI/CD:** GitHub Actions (automação de testes a cada push).

## Instalação e Execução

1. **Clonar o projeto:**
   ```bash
   git clone SEU_LINK_DO_GITHUB_AQUI

    Instalar dependências:
    Bash

    pip install -r requirements.txt

    Executar a aplicação:
    Bash

    python app.py

🧪 Testes e Qualidade de Código

Para garantir que o sistema funcione corretamente, execute os comandos abaixo:

    Rodar Testes Automatizados:
    Bash

    pytest

    Rodar Análise Estática (Lint):
    Bash

    flake8 .

⚙️ Integração Contínua (CI)

O projeto utiliza GitHub Actions para validar automaticamente cada alteração. O workflow executa:

    Instalação de dependências.

    Verificação de estilo (Linting).

    Execução dos testes automatizados.

📌 Informações Adicionais

    Versão: 1.0.0

    Autor: Gabriel Batista Gomes

    Licença: MIT
