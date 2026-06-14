# Sistema de Controle de Medicamentos - Cuidado Amigo

🌍 **Status do Deploy (Entrega Intermediária):**
Esta é uma aplicação de Interface de Linha de Comando (CLI). Ela pode ser executada facilmente na nuvem via **Replit** (importando este repositório diretamente na plataforma) ou executada localmente seguindo as instruções abaixo.

## Visão Geral
Este projeto é uma aplicação CLI desenvolvida para auxiliar idosos e cuidadores na organização de rotinas de medicação. O foco é mitigar o problema do esquecimento e da confusão de horários, garantindo maior segurança na administração de remédios.

## Problema Real e Impacto Social
Muitos idosos convivem com a polifarmácia (uso de vários medicamentos diários). A dificuldade em memorizar horários pode causar interações medicamentosas perigosas ou falta de tratamento. O Cuidado Amigo oferece uma solução digital simples para listar e organizar esses dados, promovendo autonomia e saúde.

## Funcionalidades
* **Integração com API Pública (Nova):** Busca automática e validação do endereço do paciente/cuidador através do CEP (utilizando a BrasilAPI).
* **Adicionar Medicamento:** Registro do nome e do horário (HH:MM).
* **Listar Medicamentos:** Exibição clara de todos os itens cadastrados.
* **Validação:** Impede o cadastro de campos vazios para evitar erros de registro.

## Tecnologias Utilizadas
* **Linguagem:** Python 3.10+
* **Integração:** Biblioteca `requests` para consumo de APIs REST.
* **Testes:** Pytest e `unittest.mock` (para testes unitários e testes de integração com a API externa).
* **Linting:** Flake8 (para garantia de qualidade e estilo de código).
* **CI/CD:** GitHub Actions (automação de testes e validação a cada push).

## Instalação e Execução (Local)

1. **Clonar o projeto:**
   ```bash
   git clone [https://github.com/GabrielBatistaDEV/controle-medicamentos-idosos](https://github.com/GabrielBatistaDEV/controle-medicamentos-idosos)
   cd controle-medicamentos-idosos

    Instalar dependências:
    Bash

    pip install -r requirements.txt

    Executar a aplicação:
    Bash

    python app.py

🧪 Testes e Qualidade de Código

Para garantir que o sistema funcione corretamente (incluindo a simulação da API), execute os comandos abaixo na raiz do projeto:

Rodar Testes Automatizados (Unitários e de Integração):
Bash

pytest

Rodar Análise Estática (Lint):
Bash

flake8 .

⚙️ Integração Contínua (CI)

O projeto utiliza GitHub Actions para validar automaticamente cada alteração. O workflow executa:

    Instalação de dependências.

    Verificação de estilo (Linting).

    Execução dos testes automatizados isolados.

📌 Informações Adicionais

    Versão: 1.1.0

    Autores: Gabriel Batista Gomes, Leonardo Ali Yousef

    Licença: MIT

    ---

## Integrantes
- Beatriz Saboia

## Atualização realizada
- Atualização da documentação do projeto para entrega final.
