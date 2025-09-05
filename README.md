# Accenture QA Automation – Projeto Completo (API + Frontend)

## Stack
- Python
- Pytest (API + UI)
- Requests (API)
- Selenium WebDriver (UI) – com Page Object Model (POM)
- Behave (BDD)
- GitHub Actions (CI)

## Estrutura
```
/project
  /tests
    /api
    /frontend
  /features
  /steps
  /pages
  /utils
  .github/workflows/ci.yml
  requirements.txt
  pytest.ini
  behave.ini
  README.md
```
> Obs.: Renomeie `.env.example` para `.env` e ajuste as credenciais se desejar.

## Como rodar
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Rodar testes de API + UI com Pytest
pytest

# Rodar cenários BDD com Behave
behave
```

## Subir no GitHub
```bash
git init
git add .
git commit -m "Desafio Accenture - QA Automation (API + Frontend)"
git branch -M main
git remote add origin <URL_DO_SEU_REPO>
git push -u origin main
```

## Notas
- Os testes de API utilizam a BookStore Demo API (demoqa.com).
- Os testes de UI usam a página https://demoqa.com/text-box.
- O workflow CI baixa Chrome e executa os testes em modo headless.
