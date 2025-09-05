# DesafioQA – Automação de Testes

Link do vídeo https://drive.google.com/file/d/14AXyC0u5ZvttVeID_2cddq0JCsJauwBS/view?usp=sharing

## Descrição

Este projeto tem como objetivo automatizar testes de API e interface de usuário utilizando Python, Pytest, Selenium WebDriver e Behave. Foi desenvolvido como parte do desafio técnico para a vaga de QA Automation.

## Tecnologias Utilizadas

- **Python**: Linguagem principal para automação.
- **Pytest**: Framework para testes de API e UI.
- **Requests**: Biblioteca para testes de API.
- **Selenium WebDriver**: Automação de testes de UI com Page Object Model (POM).
- **Behave**: Framework BDD para testes de comportamento.
- **GitHub Actions**: Integração contínua para execução automatizada de testes.

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
=======
# DesafioQA
DesafioQA
Contribuições

Sinta-se à vontade para contribuir com melhorias ou correções. Para isso, faça um fork deste repositório, crie uma branch com suas alterações e envie um pull request.
Atualizando README
>>>>>>> 7ae00d58413ed0c3722cfab729edb0e57321f7b8
