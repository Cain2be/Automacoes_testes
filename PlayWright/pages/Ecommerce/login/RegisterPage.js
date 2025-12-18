const { expect } = require("@playwright/test");

class RegisterPage {
    constructor(page) {
        this.page = page;
        this.url = 'https://www.consuladoracao.com.br/conta/cadastro';

        this.tipoPessoa = page.locator('#input-person-type');
        this.cpfInput = page.locator('#input-custom-field1');
        this.nomeInput = page.locator('#input-firstname');
        this.sobrenomeInput = page.locator('#input-lastname');
        this.emailInput = page.locator('#input-email');
        this.phoneInput = page.locator('#input-telephone');
        this.senhaInput = page.locator('#input-password');
        this.repSenhaInput = page.locator('#input-confirm');
        this.negarEmail = page.getByRole('radio', { name: 'Não' });
        this.aceitarPolitica = page.getByRole('checkbox'); // pode pegar vários checkboxes se tiver
        this.botaoContinuar = page.getByRole('button', { name: 'Continuar' });
        this.erroCpfInvalido = page.locator('#cpf-error');
        this.erroNomeVazio = page.locator('#firstname-error');
        this.erroSobrenomeVazio = page.locator('#lastname-error');
        this.erroEmailVazio = page.getByText('O e-mail não é válido');
        this.erroTelefoneVazio = page.getByText('O telefone deve ter entre 10 e 11 números');
        this.erroSenhaVazia = page.getByText('A senha deve ter entre 4 e 20 caracteres');
        this.erroRepSenhaVazia = page.getByText('A senha repetida esta errada');
    }

    async navigate() {
        await this.page.goto(this.url, {
            waitUntil: 'domcontentloaded',
            timeout: 60000
        });
    }

    

    async preencherFormulario({
        cpf,
        email,
        nome,
        sobrenome,
        telefone,
        senha,
        repsenha,
    }) {
        if (cpf !== undefined) await this.cpfInput.fill(cpf);
        if (email !== undefined) await this.emailInput.fill(email);
        if (nome !== undefined) await this.nomeInput.fill(nome);
        if (sobrenome !== undefined) await this.sobrenomeInput.fill(sobrenome);
        if (telefone !== undefined) await this.phoneInput.fill(telefone);
        if (senha !== undefined) await this.senhaInput.fill(senha);
        if (repsenha !== undefined) await this.repSenhaInput.fill(repsenha);
    }



    async register(dados) {
        await this.preencherFormulario(dados);
        await this.selecionarNewsletter('Não');
        if (dados.aceitaTermos) await this.marcarPolitica();
        await this.botaoContinuar.click();
    }


    async registerEnter(dados) {
        await this.preencherFormulario(dados);
        await this.selecionarNewsletter('Não');
        if (dados.aceitaTermos) await this.marcarPolitica();
        await this.senhaInput.press('Enter');
    }



































    async selecionarNewsletter(opcao = 'Não') {
        try {
            const radio = this.page.getByRole('radio', { name: opcao });
            
            // Aguardar estar disponível
            await radio.waitFor({ state: 'visible', timeout: 5000 });
            
            // Verificar se já está selecionado
            const isChecked = await radio.isChecked();
            
            if (!isChecked) {
                await radio.check({ force: true });
            } else {
            }
        } catch (error) {
        }
    }

    async marcarPolitica() {
        try {
            // Tente encontrar o checkbox específico de política
            const checkboxSelectors = [
                'input[name="agree"]',
                'input[type="checkbox"][name*="agree"]',
                '#input-agree',
                'input#agree',
                'input[type="checkbox"][id*="agree"]'
            ];
            
            for (const selector of checkboxSelectors) {
                const checkbox = this.page.locator(selector);
                if (await checkbox.count() > 0) {
                    const isChecked = await checkbox.isChecked();
                    
                    if (!isChecked) {
                        await checkbox.check({ force: true });
                    } else {
                    }
                    return;
                }
            }
            
            // Se não encontrou, tenta pelo texto do label
            const labelWithText = this.page.locator('label:has-text("política"), label:has-text("termos"), label:has-text("concordo")');
            if (await labelWithText.count() > 0) {
                const checkboxNearLabel = labelWithText.locator('input[type="checkbox"]');
                if (await checkboxNearLabel.count() > 0) {
                    await checkboxNearLabel.check({ force: true });
                    return;
                }
            }
            
            // Último recurso: primeiro checkbox da página
            const firstCheckbox = this.page.locator('input[type="checkbox"]').first();
            if (await firstCheckbox.count() > 0) {
                await firstCheckbox.check({ force: true });
                return;
            }
            
            
        } catch (error) {
        }
    }
}

module.exports = RegisterPage;
