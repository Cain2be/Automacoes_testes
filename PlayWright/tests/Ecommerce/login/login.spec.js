const { test, expect, chromium } = require('@playwright/test');
const LoginPage = require('../../../pages/Ecommerce/login/LoginPage.js');





//SECTION - CENÁRIOS DE SUCESSO
test.describe('SUCESSO', () => {

    test('CT-01 Login com CPF Válido', async ({ page }) => {
        const loginPage = new LoginPage(page);

        await loginPage.navigate();
        await loginPage.login('35186881899', '++big2be##');
        
        const sucesso = page.locator('sub:has-text("Olá,")');
        await expect(sucesso).toBeVisible();
    });




    test('CT-02 Login com email Válido', async ({ page }) => {
    const loginPage = new LoginPage(page);

    await loginPage.navigate();
    await loginPage.login('caio.bstabile@hotmail.com', '++big2be##');
    
    const sucesso = page.locator('sub:has-text("Olá,")');
    await expect(sucesso).toBeVisible();
    });




    test('CT-03 Login com CPF Válido usando Enter', async ({ page }) => {
        const loginPage = new LoginPage(page);

        await loginPage.navigate();
        await loginPage.loginEnter('35186881899', '++big2be##');
        const sucesso = page.locator('sub:has-text("Olá,")');
        await expect(sucesso).toBeVisible();
    });




    test('CT-04 Login Após Erro', async ({ page }) => {
        const loginPage = new LoginPage(page);

        await loginPage.navigate();
        await loginPage.login('35186881899','++bi2be##');

        await loginPage.errorInLogin();

        await loginPage.login('35186881899', '++big2be##');
        const sucesso = page.locator('sub:has-text("Olá,")');
        await expect(sucesso).toBeVisible();
    });
});





//SECTION - CENÁRIOS DE ERRO
test.describe('ERRO', () => {

    test('CT-05 CPF inexistente', async ({ page }) => {
        const loginPage = new LoginPage(page);

        await loginPage.navigate();
        await loginPage.login('12312312312', 'senha123');

        await loginPage.errorInLogin();
    });




    test('CT-06 CPF Inválido', async ({ page }) => {
        const loginPage = new LoginPage(page);

        await loginPage.navigate();
        await loginPage.login('351868818-99','++big2be##');

        await loginPage.errorInLogin();
    });




    test('CT-07 CPF Vazio', async ({ page }) => {
        const loginPage = new LoginPage(page);

        await loginPage.navigate();
        const urlBeforeLogin = page.url();
        await loginPage.login('','++big2be##')

        await expect(page).toHaveURL(urlBeforeLogin);
    });




    test('CT-08 Senha Vazia', async ({ page }) => {
        const loginPage = new LoginPage(page);

        await loginPage.navigate();
        const urlBeforeLogin = page.url();
        await loginPage.login('35186881899','')

        await expect(page).toHaveURL(urlBeforeLogin);
    });




        test('CT-09 Ambos Vazios', async ({ page }) => {
        const loginPage = new LoginPage(page);

        await loginPage.navigate();
        const urlBeforeLogin = page.url();
        await loginPage.login('','')

        await expect(page).toHaveURL(urlBeforeLogin);
    });
});





//SECTION - CENÁRIOS DE SEGURANÇA
test.describe('SEGURANÇA', () => {

    test('CT-10 SQL Injection', async ({ page }) => {
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
                    page.waitForTimeout(10000) // Timeout de 5segunsdos por payload
                ]);
                
                // Verifica as tentativas de login com timeout curto
                const loggedIn = await Promise.race([
                    page.locator('sub:has-text("Olá,")').isVisible(),
                    page.waitForTimeout(10000).then(() => false)
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
            await page.waitForTimeout(5000);
        }
    });



    test('CT-11 XSS', async ({ page }) => {
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
    test('CT-12 Recuperação de Senha', async ({ page }) => {
        const loginPage = new LoginPage(page);
        await loginPage.navigate();

        loginPage.forgotPassword('45951270812');
        
        const mensagem = page.getByText('Enviamos para o seu e-mail a nova senha');
        await expect(mensagem).toBeVisible({ timeout: 10000 });
    });
});


