const { expect } = require("@playwright/test");

class RegistrationPage {
    constructor(page) {
        this.page = page;

        this.url = 'https://devecommerce.big2be.com/conta/cadastro'; //Voltar pra Global depois
        this.tipoPessoa = page.locator('#input-person-type');
        this.cpfInput = page.locator('#input-custom-field1');
        this.nomeInput = page.locator('#input-firstname');
        this.sobrenomeInput = page.locator('#input-lastname');
        this.emailInput = page.locator('#input-email');
        this.phoneInput = page.locator('#input-telephone');
        this.senhaInput = page.locator('#input-password');
        this.repSenhaInput = page.locator('#input-confirm');
        this.botaoContinuar = page.getByRole('button', { name: 'Continuar' }).click();
    }
}
