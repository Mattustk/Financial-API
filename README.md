# 💰 API de Controle e Análise Financeira Pessoal

API RESTful desenvolvida em Python com **FastAPI** para gerenciamento de transações financeiras e geração de insights agregados de gastos. 

🚀 **Link da API Rodando ao Vivo (Swagger UI):** https://financial-api-production.up.railway.app/docs

## 🧠 Diferencial Técnico (Background em Dados)
Diferente de CRUDs tradicionais, esta API conta com um endpoint de inteligência financeira (`/summary`) focado em performance analítica. Utilizando **SQLAlchemy ORM**, a aplicação realiza consultas agregadas diretamente na camada do banco de dados (`group_by`, `func.sum` e `func.count`), reduzindo o overhead de memória do servidor e garantindo consistência rápida dos dados.

## 🛠️ Tecnologias e Arquitetura
* **Framework:** FastAPI (Validação estrita de contratos com Pydantic)
* **Banco de Dados:** SQLite (Camada de persistência via SQLAlchemy)
* **Deploy:** Railway (Infraestrutura em nuvem com variáveis de ambiente configuradas)
* **Arquitetura:** Estrutura modular de pacotes (`app/`) com tratamento rigoroso de exceções HTTP (Ex: erros 404 em rotas de atualização/deleção).

## 🔀 Rotas Disponíveis
* `GET /health` - Verificação de integridade do servidor.
* `POST /transactions` - Cria uma nova transação financeira.
* `GET /transactions` - Lista todas as transações persistidas.
* `PUT /transactions/{id}` - Atualiza os dados de uma transação existente.
* `DELETE /transactions/{id}` - Remove uma transação com validação de ID.
* `GET /transactions/summary` - Retorna o total gasto, volume de transações e a divisão de despesas agrupada por categoria.

## 💻 Como Rodar o Projeto Localmente

1. Clone o repositório:
```bash

Crie e ative o ambiente virtual:
```

```bash
python -m venv venv
```

# No Windows:
```bash
.\venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute a aplicação:
```bash
uvicorn app.main:app --reload
```
Acesse localmente em: https://financial-api-production.up.railway.app/docs
