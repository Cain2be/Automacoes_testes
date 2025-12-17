const { test, expect, chromium } = require('@playwright/test');
const RegisterPage = require('../../pages/Ecommerce/RegisterPage');





//SECTION - CENÁRIOS DE SUCESSO
test.describe('Sucesso', () => {

    test.only('Cadastro Válido', async ({ page }) => {
        const registerPage = new RegisterPage(page);

        await registerPage.navigate();
        await registerPage.register({
            cpf: '72425495070',
            email: `teste_big2be${Date.now()}@mail.com`,
            nome: 'Caio',
            sobrenome: 'Silva',
            telefone: '11999999999',
            senha: 'Senha@123',
        })

        await page.pause();
        
        const sucesso = page.locator('sub:has-text("Olá,")');
        await expect(sucesso).toBeVisible();
    });
});