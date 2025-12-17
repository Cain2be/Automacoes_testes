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
    }

    async navigate() {
        await this.page.goto(this.url);
    }

    

    async register({
        cpf,
        email,
        nome,
        sobrenome,
        telefone,
        senha,
        aceitaTermos = true
    }) {
        // Preencher campos básicos
        if (cpf) await this.cpfInput.fill(cpf);
        if (email) await this.emailInput.fill(email);
        if (nome) await this.nomeInput.fill(nome);
        if (sobrenome) await this.sobrenomeInput.fill(sobrenome);
        if (telefone) await this.phoneInput.fill(telefone);
        if (senha) {
            await this.senhaInput.fill(senha);
            await this.repSenhaInput.fill(senha);
        }

        // Newsletter
        await this.selecionarNewsletter('Não');

        // Aceitar termos
        if (aceitaTermos) {
            await this.marcarPolitica();
        }

        // Clicar no CAPTCHA
        await this.clicarCaptcha();

        // Clicar em continuar
        await this.botaoContinuar.click();
    }

    async registerEnter({
        cpf,
        email,
        nome,
        sobrenome,
        telefone,
        senha,
        confirmarSenha,
        aceitaTermos = true
    }) {
        // Preencher campos
        if (cpf) await this.cpfInput.fill(cpf);
        if (email) await this.emailInput.fill(email);
        if (nome) await this.nomeInput.fill(nome);
        if (sobrenome) await this.sobrenomeInput.fill(sobrenome);
        if (telefone) await this.phoneInput.fill(telefone);
        if (senha) await this.senhaInput.fill(senha);
        if (confirmarSenha) await this.repSenhaInput.fill(confirmarSenha);

        // Newsletter
        await this.selecionarNewsletter('Não');

        // Aceitar termos
        if (aceitaTermos) {
            await this.marcarPolitica();
        }

        // Clicar no CAPTCHA
        await this.clicarCaptcha();

        // Pressionar Enter no campo de senha
        await this.senhaInput.press('Enter');
    }








































    async clicarCaptcha() {
        console.log('Procurando o CAPTCHA...');
        
        try {
            // Verifica se existe iframe do CAPTCHA
            const iframeSelector = 'iframe[title*="reCAPTCHA"], iframe[src*="google.com/recaptcha"]';
            const encontrou = await this.page.locator(iframeSelector).count() > 0;
            
            if (encontrou) {
                console.log('CAPTCHA encontrado!');
                
                // Encontra o iframe e clica no checkbox dentro dele
                const iframe = this.page.frameLocator(iframeSelector).first();
                await iframe.locator('#recaptcha-anchor').click({ 
                    force: true,
                    timeout: 5000 
                });
                
                console.log('Clicou no CAPTCHA!');
                
                // Espera para verificar se foi marcado
                await this.page.waitForTimeout(2000);
                
                // Verifica se o CAPTCHA foi aceito
                try {
                    await iframe.locator('#recaptcha-anchor[aria-checked="true"]').waitFor({
                        state: 'visible',
                        timeout: 5000
                    });
                    console.log('CAPTCHA marcado com sucesso!');
                } catch {
                    console.log('CAPTCHA pode exigir verificação adicional');
                }
                
                return true;
            } else {
                console.log('Não encontrou CAPTCHA na página');
                return false;
            }
        } catch (error) {
            console.log('Erro ao clicar no CAPTCHA:', error.message);
            return false;
        }
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
                console.log(`Newsletter "${opcao}" selecionado`);
            } else {
                console.log(`Newsletter "${opcao}" já estava selecionado`);
            }
        } catch (error) {
            console.log(`Erro ao selecionar newsletter "${opcao}":`, error.message);
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
                        console.log('Checkbox de política marcado');
                    } else {
                        console.log('Checkbox de política já estava marcado');
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
                    console.log('Checkbox encontrado via label');
                    return;
                }
            }
            
            // Último recurso: primeiro checkbox da página
            const firstCheckbox = this.page.locator('input[type="checkbox"]').first();
            if (await firstCheckbox.count() > 0) {
                await firstCheckbox.check({ force: true });
                console.log('Usando primeiro checkbox da página');
                return;
            }
            
            console.warn('Não foi possível encontrar checkbox de política');
            
        } catch (error) {
            console.error('Erro ao marcar política:', error.message);
        }
    }
}

module.exports = RegisterPage;
