Feature: Formulário DemoQA
  Como uma pessoa usuária
  Quero preencher o formulário
  Para validar o comportamento da página

  Scenario: Preencher formulário com sucesso
    Given que estou na página de Text Box
    When eu preencho o formulário corretamente
    Then vejo meu nome no resultado
