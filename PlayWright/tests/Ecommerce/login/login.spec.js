const { test, expect, chromium } = require('@playwright/test');
const LoginPage = require('../pages/LoginPage');




test('Login Válido', async ({ page }) => {
    const loginPage = new LoginPage(page);

    await loginPage.navigate();
    await loginPage.login('45951270812', '++bi2be##');
    
    const sucesso = page.locator('span.lable', { hasText: 'Minha Conta' });
    await expect(sucesso).toBeVisible();
});



test('Manter Logado', async () => {

    const browser = await chromium.launch();
    const context = await browser.newContext();
    const page = await context.newPage();

    const loginPage = new LoginPage(page);

    await loginPage.navigate();
    await loginPage.login('45951270812' , '++big2be##');

    await context.storageState({ path: 'loginState.json' }); //Isso aqui grava os dados da sessão
    await browser.close(); //Isso aq Fecha o navegador depois de gravar os dados da sessão

    const browser2 = await chromium.launch();
    const context2 = await browser2.newContext({
        storageState: 'loginState.json' //Importa os dados da sessão
    });
    
    const page2 = await context2.newPage();
    console.log("URL do login:", loginPage.url);
    const baseUrl = new URL(loginPage.url).origin;

    await page2.goto(baseUrl);

    await browser2.close();

});




test('Login inválido', async ({ page }) => {
    const loginPage = new LoginPage(page);

    await loginPage.navigate();
    await loginPage.login('12312312312', 'senha123');

    const erro1 = page.getByText('Seus dados de acesso não estão corretos');
    const erro2 = page.getByText('Você excedeu o limite de tentativas de acesso');
    const erroCombinado = erro1.or(erro2);

    await expect(erroCombinado).toBeVisible();
});







