const { test, expect } = require('@playwright/test');
const RegisterPage = require('../../../pages/Ecommerce/login/RegisterPage.js');
const { gerarCPF } = require('../../../helper/Ecommerce/utils/geradorcpf.js');
const { camposExistentes } = require('../../../helper/Ecommerce/utils/camposExistentes.js');
const { tabAteSairDoCampoData } = require('../../../helper/Ecommerce/utils/tabUtils.js');


// ==============================
// Dados base reutilizáveis
// ==============================
function dadosBase(overrides = {}) {
  return {
    cpf: gerarCPF(),
    nome: 'Caio',
    sobrenome: 'QABigTwoBe',
    email: `teste_${Date.now()}@testemail.com`,
    telefone: '11999999999',
    senha: 'Senha@123',
    repsenha: 'Senha@123',
    ...overrides,
  };
}



//SECTION Happy Path
test.describe('Cadastro – HAPPY PATH', () => {
  let registerPage;

  test.beforeEach(async ({ page }) => {
    registerPage = new RegisterPage(page);
    await registerPage.navigate();
  });


});


// ===========================================
// Cadastro – Validações de Campos Obrigatórios
// ===========================================

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
    const dados = dadosBase({
      cpf: '',
    });

    await registerPage.register(dados);

    await expect(registerPage.erroCpfInvalido).toBeVisible();
  });


  test('CT-03 Campo Nome Obrigatório', async () => {
    const dados = dadosBase({
      nome: '',
    });

    await registerPage.register(dados);

    if (await registerPage.erroNomeVazio.isVisible()) {
      await expect(registerPage.erroNomeVazio)
        .toHaveText('Nome deve ter mais de 3 letras');
    } else {
      await expect(registerPage.erroNomeVazio2)
        .toHaveText('O nome deve ter entre 1 e 32 caracteres.');
    }
  });


  test('CT-04 Campo Sobrenome Obrigatório', async () => {
    const dados = dadosBase({
      sobrenome: '',
    });

    await registerPage.register(dados);

    if (await registerPage.erroSobrenomeVazio.isVisible()) {
      await expect(registerPage.erroSobrenomeVazio)
        .toHaveText('Sobrenome devem ter mais de 3 letras');
    } else {
      await expect(registerPage.erroSobrenomeVazio2)
        .toHaveText('O sobrenome deve ter entre 1 e 32 caracteres.');
    }
  });


  test('CT-05 Campo Email Obrigatório', async () => {
    const dados = dadosBase({
      email: '',
    });

    await registerPage.register(dados);

    await expect(registerPage.erroEmailVazio)
      .toBeVisible();
  });


  test('CT-06 Campo Telefone Obrigatório', async () => {
    const dados = dadosBase({
      telefone: '',
    });

    await registerPage.register(dados);

    await expect(registerPage.erroTelefoneVazio)
      .toBeVisible();
  });


  test('CT-07 Campo Senha Obrigatório', async () => {
    const dados = dadosBase({
      senha: '',
    });

    await registerPage.register(dados);

    await expect(registerPage.erroSenhaVazia)
      .toBeVisible();
  });


  test('CT-08 Campo Repetir Senha Obrigatório', async () => {
    const dados = dadosBase({
      repsenha: '',
    });

    await registerPage.register(dados);

    await expect(registerPage.erroRepSenhaVazia)
      .toBeVisible();
  });
});



// =================================
// Cadastro – Validações de Formatos
// =================================
test.describe('Cadastro – Validação nos Formatos', () => {
  let registerPage;

  test.beforeEach(async ({ page }) => {
    registerPage = new RegisterPage(page);
    await registerPage.navigate();
  });


  test('CT-09 Nome Com Mais de 32 Caracteres', async () => {
    const dados = dadosBase({
      nome: 'CaioCaioCaioCaioCaioCaioCaioCaioCaioCaioCaioCaioCaioCaioCaioCaioCaioCaioCaioCaioCaio',
    });

    await registerPage.register(dados);

    if (await registerPage.erroNomeVazio.isVisible()) {
      await expect(registerPage.erroNomeVazio)
        .toHaveText('Nome deve ter mais de 3 letras');
    } else {
      await expect(registerPage.erroNomeVazio2)
        .toHaveText('O nome deve ter entre 1 e 32 caracteres.');
    }
  });


  test('CT-10 Nome apenas com espaços', async () => {
    const dados = dadosBase({
      nome: '          ',
    });

    await registerPage.register(dados);

    if (await registerPage.erroNomeVazio.isVisible()) {
      await expect(registerPage.erroNomeVazio)
        .toHaveText('Nome deve ter mais de 3 letras');
    } else {
      await expect(registerPage.erroNomeVazio2)
        .toHaveText('O nome deve ter entre 1 e 32 caracteres.');
    }
  });


  test('CT-11 Senha com Poucos Caracteres', async () => {
    const dados = dadosBase({
      senha: 'a',
      repsenha: 'a',
    });

    await registerPage.register(dados);

    await expect(registerPage.erroSenhaVazia)
      .toBeVisible();
  });


  test.skip('CT-12 Senha com Espaços', async () => { //NOTE Tarefa criada para a correção https://app.clickup.com/t/86aemdtct
    const dados = dadosBase({
      senha: '          ',
      repsenha: '          ',
    });

    await registerPage.register(dados);

    await expect(registerPage.erroSenhaVazia)
    .toBeVisible();
  });
});



// ================================
// Cadastro – Testes Campo a Campo
// ================================
//SECTION TESTES CAMPO NOME
test.describe('Cadastro – Campo NOME', () => {
  let registerPage;

  test.beforeEach(async ({ page }) => {
    registerPage = new RegisterPage(page);
    await registerPage.navigate();
  });


  test.skip('CT-13 Nome com 1 caractere', async () => { //NOTE Tarefa criada para a correção https://app.clickup.com/t/86aemdtct
    const dados = dadosBase({
      nome: 'C',
    });

    await registerPage.register(dados);

    if (await registerPage.erroNomeVazio.isVisible()) {
      await expect(registerPage.erroNomeVazio)
        .toHaveText('Nome deve ter mais de 3 letras');
    } else {
      await expect(registerPage.erroNomeVazio2)
        .toHaveText('O nome deve ter entre 1 e 32 caracteres.');
    }
  });


  test.skip('CT-14 Nome com 2 caracteres', async () => { //NOTE Tarefa criada para a correção https://app.clickup.com/t/86aemdtct
    const dados = dadosBase({
      nome: 'Ca',
    });

    await registerPage.register(dados);

    if (await registerPage.erroNomeVazio.isVisible()) {
      await expect(register.erroNomeVazio)
      .toHaveText('Nome deve ter mais de 3 letras');
    } else {
      await expect(registerPage.erroNomeVazio2)
      .toHaveText('O nome deve ter entre 1 e 32 caracteres.');
    }
  });


  test('CT-15 Nome com 3 caracteres (mínimo)', async () => { 
    const dados = dadosBase({
      nome: 'Cai',
    });

    await registerPage.register(dados);

    await expect(
      registerPage.telaHomeEcommerce
    ).toBeVisible();
  });


  test('CT-16 Nome com 32 caracteres (máximo)', async () => { 
    const dados = dadosBase({
      nome: 'CaioCaioCaioCaioCaioCaioCaioCaio',
    });

    await registerPage.register(dados);

    await expect(
      registerPage.telaHomeEcommerce
    ).toBeVisible();
  });


  test.skip('CT-17 Nome com mais de 32 caracteres (60 no teste)', async () => { //NOTE Tarefa criada para a correção https://app.clickup.com/t/86aemdtct
    const dados = dadosBase({
      nome: 'CaioCaioCaioCaioCaioCaioCaioCaioCaioCaioCaioCaioCaioCaioCaio',
    });

    await registerPage.register(dados);

    if (await registerPage.erroNomeVazio.isVisible()) {
      await expect(registerPage.erroNomeVazio)
        .toHaveText('Nome deve ter mais de 3 letras');
    } else {
      await expect(registerPage.erroNomeVazio2)
        .toHaveText('O nome deve ter entre 1 e 32 caracteres.');
    }
  });


  test.skip('CT-18 Nome somente com números', async () => {  //NOTE Tarefa criada para a correção https://app.clickup.com/t/86aemdtct
    const dados = dadosBase({
      nome: '12345678910',
    });

    await registerPage.register(dados);

    if (await registerPage.erroNomeVazio.isVisible()) {
      await expect(registerPage.erroNomeVazio)
        .toHaveText('Nome deve ter mais de 3 letras');
    } else {
      await expect(registerPage.erroNomeVazio2)
        .toHaveText('O nome deve ter entre 1 e 32 caracteres.');
    }
  });
});



//SECTION TESTES CAMPO SOBRENOME
test.describe('Cadastro – Campo SOBRENOME', () => {
  let registerPage;

  test.beforeEach(async ({ page }) => {
    registerPage = new RegisterPage(page);
    await registerPage.navigate();
  });


  test.skip('CT-19 Sobrenome com 1 caractere', async () => {  //NOTE Tarefa criada para a correção https://app.clickup.com/t/86aeqhehe
    const dados = dadosBase({
      sobrenome: 'Q',
    });

    await registerPage.register(dados);

    if (await registerPage.erroSobrenomeVazio.isVisible()) {
      await expect(registerPage.erroSobrenomeVazio)
        .toHaveText('Sobrenome devem ter mais de 3 letras');
    } else {
      await expect(registerPage.erroSobrenomeVazio2)
        .toHaveText('O sobrenome deve ter entre 1 e 32 caracteres.');
    }
  });


  test.skip('CT-20 Sobrenome com 2 caractere', async () => {  //NOTE Tarefa criada para a correção https://app.clickup.com/t/86aeqhehe
    const dados = dadosBase({
      sobrenome: 'QA',
    });

    await registerPage.register(dados);

    if (await registerPage.erroSobrenomeVazio.isVisible()) {
      await expect(registerPage.erroSobrenomeVazio)
        .toHaveText('Sobrenome devem ter mais de 3 letras');
    } else {
      await expect(registerPage.erroSobrenomeVazio2)
        .toHaveText('O sobrenome deve ter entre 1 e 32 caracteres.');
    }
  });


  test('CT-21 Sobrenome com 3 caracteres (mínimo)', async () => { 
    const dados = dadosBase({
      sobrenome: 'QAB',
    });

    await registerPage.register(dados);

    await expect(
      registerPage.telaHomeEcommerce
    ).toBeVisible();
  });


  test('CT-22 Sobrenome com mais de 32 caracteres (70 no teste)', async () => { //NOTE Tarefa criada para a correção https://app.clickup.com/t/86aeqhehe
    const dados = dadosBase({
      sobrenome: 'QABigTwoBeQABigTwoBeQABigTwoBeQABigTwoBeQABigTwoBeQABigTwoBeQABigTwoBe',
    });

    await registerPage.register(dados);

    if (await registerPage.erroSobrenomeVazio.isVisible()) {
      await expect(registerPage.erroSobrenomeVazio)
        .toHaveText('Sobrenome devem ter mais de 3 letras');
    } else {
      await expect(registerPage.erroSobrenomeVazio2)
        .toHaveText('O sobrenome deve ter entre 1 e 32 caracteres.');
    }
  });

  
  test.skip('CT-23 Sobrenome somente com números', async () => {  //NOTE Tarefa criada para a correção https://app.clickup.com/t/86aemdtct
    const dados = dadosBase({
      sobrenome: '12345678910',
    });

    await registerPage.register(dados);

    if (await registerPage.erroSobrenomeVazio.isVisible()) {
      await expect(registerPage.erroSobrenomeVazio)
        .toHaveText('Sobrenome devem ter mais de 3 letras');
    } else {
      await expect(registerPage.erroSobrenomeVazio2)
        .toHaveText('O sobrenome deve ter entre 1 e 32 caracteres.');
    }
  });
});



//SECTION TESTES CAMPO CPF
test.describe('Cadastro – Campo CPF', () => {
  let registerPage;

  test.beforeEach(async ({ page }) => {
    registerPage = new RegisterPage(page);
    await registerPage.navigate();
  });


  test('CT-24 CPF com menos de 11 dígitos', async () => {
    const dados = dadosBase({
      cpf: '4595127081',
    });

    await registerPage.register(dados);

    await expect(registerPage.erroCpfInvalido)
      .toBeVisible();
  });


  test('CT-25 CPF com mais de 11 dígitos', async () => {
    const dados = dadosBase({
      cpf: '459512708122',
    });

    await registerPage.register(dados);

    await expect(registerPage.erroCpfInvalido)
      .toBeVisible();
  });


  test('CT-26 CPF com letras', async () => {
    const dados = dadosBase({
      cpf: '459512708I2',
    });

    await registerPage.register(dados);

    await expect(registerPage.erroCpfInvalido)
      .toBeVisible();
  });


  test('CT-27 CPF com caracteres especiais', async () => {
    const dados = dadosBase({
      cpf: '459512708!2',
    });

    await registerPage.register(dados);

    await expect(registerPage.erroCpfInvalido)
      .toBeVisible();
  });


  test('CT-28 CPF Inválido', async () => {
    const dados = dadosBase({
      cpf: '12345678910',
    });

    await registerPage.register(dados);

    await expect(registerPage.erroCpfInvalido)
      .toBeVisible();
  });


  test('CT-29 CPF já cadastrado (do Dionatan usado como teste)', async () => {
    const dados = dadosBase({
      cpf: '35186881899',
    });

    await registerPage.register(dados);

    await expect(registerPage.erroCpfJaCadastrado)
      .toBeVisible();
  });
});



//SECTION TESTES CAMPO EMAIL
test.describe('Cadastro – Campo Email', () => {
  let registerPage;

  test.beforeEach(async ({ page }) => {
    registerPage = new RegisterPage(page);
    await registerPage.navigate();
  });

      
  test('CT-30 Email sem @', async () => {
    const dados = dadosBase({
      email: `teste_${Date.now()}mail.com`,
    });

    await registerPage.register(dados);

    await expect(registerPage.emailInput)
    .toHaveJSProperty('validity.valid', false);
  });


  test('CT-31 Email sem domínio', async () => {
    const dados = dadosBase({
      email: `teste_${Date.now()}@`,
    });

    await registerPage.register(dados);

    await expect(registerPage.emailInput)
    .toHaveJSProperty('validity.valid', false);
  });


  test('CT-32 Email com espaço', async () => {
    const dados = dadosBase({
      email: `teste_ ${Date.now()}@gmail.com`,
    });

    await registerPage.register(dados);

    await expect(registerPage.emailInput)
    .toHaveJSProperty('validity.valid', false);
  });


  test('CT-33 Email em maiúsculas', async () => { 
    const dados = dadosBase({
      email: `TESTE_${Date.now()}@TESTEMAIL.COM`,
    });

    await registerPage.register(dados);

    await expect(
      registerPage.telaHomeEcommerce
    ).toBeVisible();
  });


  test('CT-34 Email já cadastrado', async () => {
    const dados = dadosBase({
      email: 'abadia.dionatan@gmail.com',
    });

    await registerPage.register(dados);

    await expect(
      registerPage.erroEmailJaCadastrado
    ).toBeVisible();
  });
});



//SECTION TESTES CAMPO TELEFONE
test.describe('Cadastro – Campo Telefone', () => {
  let registerPage;

  test.beforeEach(async ({ page }) => {
    registerPage = new RegisterPage(page);
    await registerPage.navigate();
  });


  test('CT-35 Telefone com poucos dígitos', async () => {
    const dados = dadosBase({
      telefone: '1199999',
    });

    await registerPage.register(dados);

    await expect(registerPage.erroTelefoneVazio)
      .toBeVisible();
  });


  test('CT-36 Telefone com muitos dígitos', async () => {
    const dados = dadosBase({
      telefone: '1199999999999',
    });

    await registerPage.register(dados);

    await expect(registerPage.erroTelefoneVazio)
      .toBeVisible();
  });


  test.skip('CT-37 Telefone com letras e caracteres especiais', async () => { //NOTE Tarefa criada para a correção https://app.clickup.com/t/86aeqz279
    const dados = dadosBase({
      telefone: 'ab!$@fghijk',
    });

    await registerPage.register(dados);

    await expect(registerPage.erroTelefoneVazio)
      .toBeVisible();
  });

});

//SECTION TESTES CAMPO SENHA
test.describe('Cadastro – Campo Senha', () => {
  let registerPage;

  test.beforeEach(async ({ page }) => {
    registerPage = new RegisterPage(page);
    await registerPage.navigate();
  });


  test('CT-38 Senha muito longa ', async () => {
    const dados = dadosBase({
      senha: 'Senha@123Senha@123Senha@123Senha@123Senha@123Senha@123Senha@123Senha@123Senha@123',
      repsenha: 'Senha@123Senha@123Senha@123Senha@123Senha@123Senha@123Senha@123Senha@123Senha@123',
    });

    await registerPage.register(dados);

    await expect(registerPage.erroSenhaVazia)
      .toBeVisible();
  });
});



//SECTION TESTES CAMPO REPETIR SENHA
test.describe('Cadastro – Campo Repetir Senha', () => {
  let registerPage;

  test.beforeEach(async ({ page }) => {
    registerPage = new RegisterPage(page);
    await registerPage.navigate();
  });


  test('CT-39 Senhas diferentes', async () => {
    const dados = dadosBase({
      senha: 'Senha@123',
      repsenha: 'Senha123',
    });

    await registerPage.register(dados);

    await expect(registerPage.erroRepSenhaVazia
    )
      .toBeVisible();
  });
});


// =======================================
// Cadastro – Validações de Campos de Data
// =======================================


//SECTION TESTES CAMPO CEP
test.describe('Cadastro – Campo CEP', () => {
  let registerPage;

  test.beforeEach(async ({ page }) => {
    registerPage = new RegisterPage(page);
    await registerPage.navigate();
  });


  test('CT-40 Campo CEP Vazio', async ({ page }) => {
    const dados = dadosBase({
      cep: '',
    });
    await registerPage.register(dados);

    await expect(registerPage.cepInput)
    .toHaveJSProperty('validity.valid', false);
  });


  test('CT-41 CEP com menos de 8 dígitos', async ({ page }) => {
    const dados = dadosBase({
      cep: '1405710',
    });

    const mensagemEsperada = 'Preencha um cep válido!';
    page.once('dialog', async dialog => {
      expect(dialog.type()).toBe('alert');
      expect(dialog.message()).toContain(mensagemEsperada);
      await dialog.accept();
    });

    await registerPage.register(dados);
    });


  test('CT-42 CEP com mais de 8 dígitos', async ({ page }) => {
    const dados = dadosBase({
      cep: '140571000',
    });

    const mensagemEsperada = 'Preencha um cep válido!';
    page.once('dialog', async dialog => {
      expect(dialog.type()).toBe('alert');
      expect(dialog.message()).toContain(mensagemEsperada);
      await dialog.accept();
    });

    await registerPage.register(dados);
    });


  test('CT-43 CEP com letras', async ({ page }) => {
    const dados = dadosBase({
      cep: 'testecep',
    });

    const mensagemEsperada = 'Preencha um cep válido!';
    page.once('dialog', async dialog => {
      expect(dialog.type()).toBe('alert');
      expect(dialog.message()).toContain(mensagemEsperada);
      await dialog.accept();
    });

    await registerPage.register(dados);
    });


  test('CT-44 CEP com caracteres especiais', async ({ page }) => {
    const dados = dadosBase({
      cep: '14057!00',
    });

    const mensagemEsperada = 'Preencha um cep válido!';
    page.once('dialog', async dialog => {
      expect(dialog.type()).toBe('alert');
      expect(dialog.message()).toContain(mensagemEsperada);
      await dialog.accept();
    });

    await registerPage.register(dados);
    });


  test('CT-45 CEP inexistente', async ({ page }) => {
    const dados = dadosBase({
      cep: '12312312',
    });

    const mensagemEsperada = 'Preencha um cep válido!';
    page.once('dialog', async dialog => {
      expect(dialog.type()).toBe('alert');
      expect(dialog.message()).toContain(mensagemEsperada);
      await dialog.accept();
    });

    await registerPage.register(dados);
    });


  test('CT-46 CEP com auto-preenchimento', async ({ page }) => {
    const dados = dadosBase({
      cep: '01001000',
    });

    await registerPage.navigate();
    await registerPage.cepInput.fill(dados.cep);
    await page.keyboard.press('Tab');

    // Aguarda auto-preenchimento
    await expect(registerPage.enderecoInput).not.toHaveValue('');
    await expect(registerPage.bairroInput).not.toHaveValue('');
    await expect(registerPage.estadoInput).not.toHaveValue('');
  });


  test('CT-47 CEP sem auto-reenchimento', async ({ page }) => {
    const dados = dadosBase({
      cep: '09400000',
    });

    await registerPage.navigate();
    await registerPage.cepInput.fill(dados.cep);
    await page.keyboard.press('Tab');

    // Aguarda auto-preenchimento
    await expect(registerPage.enderecoInput).toHaveValue('');
    await expect(registerPage.bairroInput).toHaveValue('');
    await expect(registerPage.estadoInput).toHaveValue('');
  });


  test('CT-48 Alteração de CEP atualiza dados do endereço', async ({ page }) => {
    await registerPage.navigate();

    // ===== CEP 1 =====
    await registerPage.cepInput.fill('01001000');
    await page.keyboard.press('Tab');

    // Aguarda auto-preenchimento
    await expect(registerPage.enderecoInput).not.toHaveValue('');
    await expect(registerPage.bairroInput).not.toHaveValue('');
    await expect(registerPage.estadoInput).not.toHaveValue('');

    // Grava valores do CEP 1
    const enderecoCEP1 = await registerPage.enderecoInput.inputValue();
    const bairroCEP1 = await registerPage.bairroInput.inputValue();
    const estadoCEP1 = await registerPage.estadoInput.inputValue();

    await registerPage.cepInput.fill('69900064'); // outro CEP real
    await page.keyboard.press('Tab');

    await expect     // Espera os valores serem atualizados
      .poll(() => registerPage.enderecoInput.inputValue())
      .not.toBe(enderecoCEP1);

      // Grava valores do CEP 1
    const enderecoCEP2 = await registerPage.enderecoInput.inputValue();
    const bairroCEP2 = await registerPage.bairroInput.inputValue();
    const estadoCEP2 = await registerPage.estadoInput.inputValue();

    expect(enderecoCEP2).not.toBe(enderecoCEP1);
    expect(bairroCEP2).not.toBe(bairroCEP1);
    expect(estadoCEP2).not.toBe(estadoCEP1);
  });
});



//SECTION TESTES CAMPO ENDEREÇO
test.describe('Cadastro – Campo Endereço', () => {
  let registerPage;

  test.beforeEach(async ({ page }) => {
    registerPage = new RegisterPage(page);
    await registerPage.navigate();
  });


  test('CT-49 Endereço em branco', async () => {
    const dados = dadosBase({
      cep: '09400000',
      endereco: '',
      bairro: 'Acccc',
      estado: 'AC',
      numero: '123',
    });
    await registerPage.register(dados);


    await expect(registerPage.enderecoInput)
    .toHaveJSProperty('validity.valid', false);
  });

  
  test.skip('CT-50 Endereço com apenas números', async () => { //NOTE - Tare criada para correção https://app.clickup.com/t/86aeu8gfk
    const dados = dadosBase({
      cep: '09400000',
      endereco: '123',
      bairro: 'Acccc',
      estado: 'AC',
      numero: '123',
    });
    await registerPage.register(dados);

    await expect(registerPage.enderecoInput)
    .toHaveJSProperty('validity.valid', false);
  });

  
  test.skip('CT-51 Endereço com 1 caractere', async () => { //NOTE - Tare criada para correção https://app.clickup.com/t/86aeu8gfk
    const dados = dadosBase({
      cep: '09400000',
      endereco: 'R',
      bairro: 'Acccc',
      estado: 'AC',
      numero: '123',
    });
    await registerPage.register(dados);

    await expect(registerPage.enderecoInput)
    .toHaveJSProperty('validity.valid', false);
  });


  test('CT-52 Endereço com caracteres especiais', async () => { //NOTE - Tare criada para correção https://app.clickup.com/t/86aeu8gfk
    const dados = dadosBase({
      cep: '09400000',
      endereco: "Rúa Téste' !@#$%¨&*()óíáúéãõôêâîû.;~'",
      bairro: 'Acccc',
      estado: 'AC',
      numero: '123',
    });
    await registerPage.register(dados);

    await expect(
      registerPage.telaHomeEcommerce
    ).toBeVisible();
  });


  test.skip('CT-53 Endereço com mais de 80 caracteres', async () => { //NOTE - Tare criada para correção https://app.clickup.com/t/86aeu8gfk
    const dados = dadosBase({
      cep: '09400000',
      endereco: "RuaTesteRuaTesteRuaTesteRuaTesteRuaTesteRuaTesteRuaTesteRuaTesteRuaTesteRuaTeste",
      bairro: 'Acccc',
      estado: 'AC',
      numero: '123',
    });
    await registerPage.register(dados);

    await expect(registerPage.enderecoInput)
    .toHaveJSProperty('validity.valid', false);
  });
});




//SECTION TESTES CAMPO NÚMERO
test.describe('Cadastro – Campo Número', () => {
  let registerPage;

  test.beforeEach(async ({ page }) => {
    registerPage = new RegisterPage(page);
    await registerPage.navigate();
  });


  test('CT-54 Número em branco', async () => { 
    const dados = dadosBase({
      cep: '09400000',
      endereco: "Rua Teste",
      bairro: 'Acccc',
      estado: 'AC',
      numero: '',
    });
    await registerPage.register(dados);

    await expect(registerPage.numeroInput)
    .toHaveJSProperty('validity.valid', false);
  });


  test.skip('CT-55 Número com letras', async () => { //NOTE - Tare criada para correçãohttps://app.clickup.com/t/86aeukr42
    const dados = dadosBase({
      cep: '09400000',
      endereco: "Rua Teste",
      bairro: 'Acccc',
      estado: 'AC',
      numero: 'AAAA',
    });
    await registerPage.register(dados);

    await expect(registerPage.numeroInput)
    .toHaveJSProperty('validity.valid', false);
  });


  test.skip('CT-56 Número com caracteres especiais', async () => { //NOTE - Tare criada para correçãohttps://app.clickup.com/t/86aeukr42
    const dados = dadosBase({
      cep: '09400000',
      endereco: "Rua Teste",
      bairro: 'Acccc',
      estado: 'AC',
      numero: '!@#$%¨&*(=',
    });
    await registerPage.register(dados);

    await expect(registerPage.numeroInput)
    .toHaveJSProperty('validity.valid', false);
  });
});



//SECTION TESTES CAMPO BAIRRO
test.describe('Cadastro – Campo Bairro', () => {
  let registerPage;

  test.beforeEach(async ({ page }) => {
    registerPage = new RegisterPage(page);
    await registerPage.navigate();
  });


  test('CT-57 Bairro em branco', async () => { 
    const dados = dadosBase({
      cep: '09400000',
      endereco: "Rua Teste",
      bairro: '',
      estado: 'AC',
      numero: '123',
    });
    await registerPage.register(dados);

    await expect(registerPage.bairroInput)
    .toHaveJSProperty('validity.valid', false);
  });


  test.skip('CT-58 Bairro com números', async () => { 
    const dados = dadosBase({
      cep: '09400000',
      endereco: "Rua Teste",
      bairro: '123123',
      estado: 'AC',
      numero: '123',
    });
    await registerPage.register(dados);

    await expect(registerPage.bairroInput)
    .toHaveJSProperty('validity.valid', false);
  });


  test.skip('CT-59 Bairro com 1 caractere', async () => { 
    const dados = dadosBase({
      cep: '09400000',
      endereco: "Rua Teste",
      bairro: 'B',
      estado: 'AC',
      numero: '123',
    });
    await registerPage.register(dados);

    await expect(registerPage.bairroInput)
    .toHaveJSProperty('validity.valid', false);
  });


  test.skip('CT-60 Bairro com mais de 100 caracteres', async () => { 
    const dados = dadosBase({
      cep: '09400000',
      endereco: "Rua Teste",
      bairro: 'TesteBairroTesteBairroTesteBairroTesteBairroTesteBairroTesteBairroTesteBairroTesteBairroTesteBairroTesteBairro',
      estado: 'AC',
      numero: '123',
    });
    await registerPage.register(dados);

    await expect(registerPage.bairroInput)
    .toHaveJSProperty('validity.valid', false);
  });
});




//SECTION TESTES CAMPO COMPLEMENTO
test.describe('Cadastro – Campo Complemento', () => {
  let registerPage;
  test.use({ storageState: undefined });

  test.beforeEach(async ({ page }) => {
    registerPage = new RegisterPage(page);
    await registerPage.navigate();
  });

  test('CT-61 Complemento em branco', async () => {
    const dados = dadosBase({
      cep: '09400000',
      endereco: 'Rua Teste',
      bairro: 'Teste Bairro',
      estado: 'AC',
      numero: '123',
      complemento: '',
    });

    await registerPage.register(dados);

    await expect(registerPage.telaHomeEcommerce).toBeVisible();
  });

  test('CT-62 Complemento com letras, números e caracteres especiais', async () => {
    const dados = dadosBase({
      cep: '09400000',
      endereco: 'Rua Teste',
      bairro: 'Teste Bairro',
      estado: 'AC',
      numero: '123',
      complemento: 'Teste123Compl3m3nt0!@#$%¨&*()',
    });

    await registerPage.register(dados);

    await expect(registerPage.telaHomeEcommerce).toBeVisible();
  });

  test.skip('CT-63 Complemento com texto longo demais', async () => {
    const dados = dadosBase({
      cep: '09400000',
      endereco: 'Rua Teste',
      bairro: 'Teste Bairro',
      estado: 'AC',
      numero: '123',
      complemento: 'Complemento'.repeat(30),
    });

    await registerPage.register(dados);

    await expect(registerPage.telaHomeEcommerce).toBeVisible();
  });
});




//SECTION TESTES CAMPO ESTADO
test.describe('Cadastro – Campo Estado', () => {
  let registerPage;

  test.beforeEach(async ({ page }) => {
    registerPage = new RegisterPage(page);
    await registerPage.navigate();
  });


  test('CT-63 Estado em branco', async () => {
    const dados = dadosBase({
      cep: '09400000',
      endereco: 'Rua Teste',
      bairro: 'Teste Bairro',
      estado: '',
      numero: '123',
    });

    await registerPage.register(dados);

    await expect(registerPage.estadoInput)
    .toHaveJSProperty('validity.valid', false);
  });


  test('CT-63 Estado auto-preenchido', async ({ page }) => {
  const registerPage = new RegisterPage(page);

  await registerPage.navigate();
  await registerPage.cepInput.fill('14057100');
  await registerPage.cepInput.blur();
  await expect(registerPage.estadoInput).toHaveValue('SP');
  });
});

































