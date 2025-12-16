const { expect } = require("@playwright/test");

class LoginPage {
    constructor(page) {
        this.page = page;

        this.url = 'https://devecommerce.big2be.com/conta/acessar'; //Voltar pra Global depois
        this.cpfInput = page.locator('#input-email');
        this.senhaInput = page.locator('#input-password');
        this.continuarButton = page.locator('[name="login"]');
        this.modalUsuario = page.locator('sub:has-text("Olá,")');
        this.botaoLogout = page.getByRole('link', { name: 'Sair'});
        this.botaoEsqueciSenha = page.getByRole('link', { name: 'Esqueceu sua senha?' });
        this.cpfInputEsqueciSenha = page.locator('#input-cpf');
        this.botaoContinuarEsqueciSenha = page.locator('#check-cpf');
    }

    async navigate() {
        await this.page.goto(this.url);             // Browser acessar URL declarada
    }


    async login(cpf, senha) {           // Criação função Login
        await this.cpfInput.fill(cpf);
        await this.senhaInput.fill(senha);
        await this.continuarButton.click();
    }


    async loginEnter(cpf, senha) {              // Criação função Login
        await this.cpfInput.fill(cpf);
        await this.senhaInput.fill(senha);
        await this.senhaInput.press('Enter');
    }

    async logout() {                //Criando função Logout
        await this.modalUsuario.click();
        await this.botaoLogout.click();
    }


    async verifyLogout() {              // Checa se está deslogado no ecommerce
        const entre_ou_cadastre = this.page.locator('sub:has-text("Entre ou Cadastre-se")');
        await expect(entre_ou_cadastre).toBeVisible();
    }


    async errorInLogin() {
        const erro1 = this.page.getByText('Seus dados de acesso não estão corretos');
        const erro2 = this.page.getByText('Você excedeu o limite de tentativas de acesso');
        const erroCombinado = erro1.or(erro2);
        await expect(erroCombinado).toBeVisible();
    }


    async forgotPassword(cpf) {
        await this.botaoEsqueciSenha.click();
        await this.cpfInputEsqueciSenha.fill(cpf);
        await this.botaoContinuarEsqueciSenha.click();
    }
}


module.exports = LoginPage;
