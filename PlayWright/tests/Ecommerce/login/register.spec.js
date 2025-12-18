const { test, expect } = require('@playwright/test');
const RegisterPage = require('../../pages/Ecommerce/RegisterPage');

// ===============================
// Cadastro – Validações de Campos
// ===============================

test.describe('Cadastro – Validações de Campos Obrigatórios', () => {
  let registerPage;

  test.beforeEach(async ({ page }) => {
    registerPage = new RegisterPage(page);
    await registerPage.navigate();
  });

  test('CT-01 Elementos Carregados', async () => {
    await expect(registerPage.tipoPessoa).toBeVisible();
    await expect(registerPage.cpfInput).toBeVisible();
    await expect(registerPage.nomeInput).toBeVisible();
    await expect(registerPage.sobrenomeInput).toBeVisible();
    await expect(registerPage.emailInput).toBeVisible();
    await expect(registerPage.phoneInput).toBeVisible();
    await expect(registerPage.senhaInput).toBeVisible();
    await expect(registerPage.repSenhaInput).toBeVisible();
    await expect(registerPage.botaoContinuar).toBeVisible();
  });

  test('CT-02 Campo CPF Obrigatório', async () => {
    await registerPage.register({
      cpf: '',
      email: `teste_${Date.now()}@mail.com`,
      nome: 'Caio',
      sobrenome: 'Silva',
      telefone: '11999999999',
      senha: 'Senha@123',
      repsenha: 'Senha@123',
    });

    await expect(registerPage.erroCpfInvalido)
      .toBeVisible();
  });

  test('CT-03 Campo Nome Obrigatório', async () => {
    await registerPage.register({
      cpf: '45951270812',
      email: `teste_${Date.now()}@mail.com`,
      nome: '',
      sobrenome: 'Silva',
      telefone: '11999999999',
      senha: 'Senha@123',
      repsenha: 'Senha@123',
    });

    await expect(registerPage.erroNomeVazio)
      .toHaveText('Nome deve ter mais de 3 letras');
  });

  test('CT-04 Campo Sobrenome Obrigatório', async () => {
    await registerPage.register({
      cpf: '45951270812',
      email: `teste_${Date.now()}@mail.com`,
      nome: 'Caio',
      sobrenome: '',
      telefone: '11999999999',
      senha: 'Senha@123',
      repsenha: 'Senha@123',
    });

    await expect(registerPage.erroSobrenomeVazio)
      .toHaveText('Sobrenome devem ter mais de 3 letras');
  });

  test('CT-05 Campo Email Obrigatório', async () => {
    await registerPage.register({
      cpf: '45951270812',
      email: '',
      nome: 'Caio',
      sobrenome: 'Silva',
      telefone: '11999999999',
      senha: 'Senha@123',
      repsenha: 'Senha@123',
    });

    await expect(registerPage.erroEmailVazio)
      .toBeVisible();
  });

  test('CT-06 Campo Telefone Obrigatório', async () => {
    await registerPage.register({
      cpf: '45951270812',
      email: `teste_${Date.now()}@mail.com`,
      nome: 'Caio',
      sobrenome: 'Silva',
      telefone: '',
      senha: 'Senha@123',
      repsenha: 'Senha@123',
    });

    await expect(registerPage.erroTelefoneVazio)
      .toBeVisible();
  });

  test('CT-07 Campo Senha Obrigatório', async () => {
    await registerPage.register({
      cpf: '45951270812',
      email: `teste_${Date.now()}@mail.com`,
      nome: 'Caio',
      sobrenome: 'Silva',
      telefone: '11999999999',
      senha: '',
      repsenha: 'Senha@123',
    });

    await expect(registerPage.erroSenhaVazia)
      .toBeVisible();
  });

  test('CT-08 Campo Repetir Senha Obrigatório', async () => {
    await registerPage.register({
      cpf: '45951270812',
      email: `teste_${Date.now()}@mail.com`,
      nome: 'Caio',
      sobrenome: 'Silva',
      telefone: '11999999999',
      senha: 'Senha@123',
      repsenha: '',
    });

    await expect(registerPage.erroRepSenhaVazia)
      .toBeVisible();
  });
});
