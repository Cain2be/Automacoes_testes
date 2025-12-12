class LoginPage {
    constructor(page) {
        this.page = page;

        this.url = 'https://www.consuladoracao.com.br/conta/acessar'; //Voltar pra Global depois
        this.cpfInput = page.locator('#input-email');
        this.senhaInput = page.locator('#input-password');
        this.continuarButton = page.locator('[name="login"]');
        this.modalUsuario = page.locator('span.lable', { hasText: 'Minha Conta' });
        this.botaoLogout = page.getByRole('link', { name: 'Sair'});
    }

    async navigate() {
        await this.page.goto(this.url);  // Browser acessar URL declarada
    }


    async login(cpf, senha) {        // Criação função Login
        await this.cpfInput.fill(cpf);
        await this.senhaInput.fill(senha);
        await this.continuarButton.click();
    }


    async logout() {    //Criando função Logout
        await this.modalUsuario.click();
        await this.botaoLogout.click();
    }
}


module.exports = LoginPage;
