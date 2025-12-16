const { test, expect, chromium } = require('@playwright/test');
const LoginPage = require('../../pages/Ecommerce/LoginPage');





//SECTION - CENÁRIOS DE SUCESSO
test.describe('SUCESSO', () => {

    test('Login com CPF Válido', async ({ page }) => {
        const loginPage = new LoginPage(page);

        await loginPage.navigate();
        await loginPage.login('45951270812', '++big2be##');
        
        const sucesso = page.locator('sub:has-text("Olá,")');
        await expect(sucesso).toBeVisible();
    });




    test('Login com email Válido', async ({ page }) => {
    const loginPage = new LoginPage(page);

    await loginPage.navigate();
    await loginPage.login('caio.bstabile@gmail.com', '12345678');
    
    const sucesso = page.locator('sub:has-text("Olá,")');
    await expect(sucesso).toBeVisible();
    });




    test('Login com CPF Válido usando Enter', async ({ page }) => {
        const loginPage = new LoginPage(page);

        await loginPage.navigate();
        await loginPage.loginEnter('45951270812', '++big2be##');
        const sucesso = page.locator('sub:has-text("Olá,")');
        await expect(sucesso).toBeVisible();
    });




    test('Login Após Erro', async ({ page }) => {
        const loginPage = new LoginPage(page);

        await loginPage.navigate();
        await loginPage.login('45951270812','++bi2be##');

        await loginPage.errorInLogin();

        await loginPage.login('45951270812', '++big2be##');
        const sucesso = page.locator('sub:has-text("Olá,")');
        await expect(sucesso).toBeVisible();
    });
});





//SECTION - CENÁRIOS DE ERRO
test.describe('ERRO', () => {

    test('CPF inexistente', async ({ page }) => {
        const loginPage = new LoginPage(page);

        await loginPage.navigate();
        await loginPage.login('12312312312', 'senha123');

        await loginPage.errorInLogin();
    });




    test('CPF Inválido', async ({ page }) => {
        const loginPage = new LoginPage(page);

        await loginPage.navigate();
        await loginPage.login('459512708-12','++big2be##');

        await loginPage.errorInLogin();
    });




    test('CPF Vazio', async ({ page }) => {
        const loginPage = new LoginPage(page);

        await loginPage.navigate();
        const urlBeforeLogin = page.url();
        await loginPage.login('','++big2be##')

        await expect(page).toHaveURL(urlBeforeLogin);
    });




    test('Senha Vazia', async ({ page }) => {
        const loginPage = new LoginPage(page);

        await loginPage.navigate();
        const urlBeforeLogin = page.url();
        await loginPage.login('45951270812','')

        await expect(page).toHaveURL(urlBeforeLogin);
    });




        test('Ambos Vazios', async ({ page }) => {
        const loginPage = new LoginPage(page);

        await loginPage.navigate();
        const urlBeforeLogin = page.url();
        await loginPage.login('','')

        await expect(page).toHaveURL(urlBeforeLogin);
    });
});





//SECTION - CENÁRIOS DE SEGURANÇA
test.describe('SEGURANÇA', () => {

    test('SQL Injection', async ({ page }) => {
        const loginPage = new LoginPage(page);
        await loginPage.navigate();
        
        const payloads = [
            "' OR '1'='1",
            "' OR '1'='1' --",
            "' OR '1'='1' #",
            "admin' --",
            "' OR 'a'='a",
            "' OR 1=1 --",
            "\" OR \"1\"=\"1",
            "' UNION SELECT NULL --",
        ];
        
        for (const payload of payloads) {
            await loginPage.navigate();
            

            try {
                await Promise.race([
                    loginPage.login(payload, "teste123"),
                    page.waitForTimeout(5000) // Timeout de 5segunsdos por payload
                ]);
                
                // Verifica as tentativas de login com timeout curto
                const loggedIn = await Promise.race([
                    page.locator('sub:has-text("Olá,")').isVisible(),
                    page.waitForTimeout(2000).then(() => false)
                ]);
                
                if (loggedIn) {
                    console.error(`❌ VULNERABILIDADE ENCONTRADA com payload: ${payload}`);
                    try {
                        await page.locator('sub:has-text("Olá,")').click({ timeout: 3000 });
                        await page.getByRole('link', { name: 'Sair'}).click({ timeout: 3000 });
                    } catch {
                    }
                }
                
            } catch (error) {
                console.log(`⚠️  Erro com payload ${payload}: ${error.message}`);
            }
            await page.waitForTimeout(300);
        }
    });



    test('XSS', async ({ page }) => {
        const loginPage = new LoginPage(page);
        await loginPage.navigate();

        const XSSpayloads = [
            "<script>alert('xss')</script>",
            "<img src=x onerror=alert(1)>",
            "javascript:alert('xss')",
            "\" onfocus=\"alert('xss')\" autofocus=\"",
        ];


        for (const payload of XSSpayloads) {
            await loginPage.cpfInput.fill(payload);
            await loginPage.senhaInput.fill(payload);
            await loginPage.continuarButton.click();


            page.on('dialog', async dialog => {
                console.error(`❌ XSS Vulnerável: ${dialog.message()} com payload: ${payload}`);
                await dialog.dismiss();
                test.fail();
            });

            await page.waitForTimeout(1000);
            await loginPage.navigate();
        }
    });
});




//SECTION - TESTES DE USABILIDADE
test.describe('USABILIDADE', () => {
    test.only('Recuperação de Senha', async ({ page }) => {
        const loginPage = new LoginPage(page);
        await loginPage.navigate();

        loginPage.forgotPassword('45951270812');
        
        const mensagem = page.getByText('Enviamos para o seu e-mail a nova senha');
        await expect(mensagem).toBeVisible({ timeout: 10000 });
    });

});


