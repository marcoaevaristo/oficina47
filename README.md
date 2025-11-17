# Site de Vendas - Oficina 47

Site de vendas de torradores de café desenvolvido em Python com Flask.

## 🚀 Como usar localmente

### 1. Instalar dependências

```bash
pip install -r requirements.txt
```

### 2. Configurar número do WhatsApp

Abra o arquivo `app.py` e altere o número do WhatsApp na linha 9:

```python
WHATSAPP_NUMBER = '5535997500438'  # Telefone: (35) 99750-0438
```

**Formato:** código do país + DDD + número (sem espaços, parênteses ou hífens)
- Exemplo: `5511999999999` (Brasil: 55, São Paulo: 11, número: 999999999)

### 3. Executar o site

```bash
python app.py
```

O site estará disponível em: `http://localhost:5000`

## 📁 Estrutura do projeto

```
projeto_oficina47/
├── app.py                 # Aplicação Flask principal
├── requirements.txt       # Dependências Python
├── runtime.txt            # Versão do Python para Render
├── .gitignore            # Arquivos ignorados pelo Git
├── templates/
│   └── index.html        # Template HTML da página
├── static/
│   └── css/
│       └── style.css     # Estilos CSS
└── imagem/               # Pasta com imagens dos produtos
```

## ☁️ Deploy no Render

### Passo a passo:

1. **Criar conta no Render**
   - Acesse [render.com](https://render.com)
   - Crie uma conta gratuita

2. **Conectar repositório Git**
   - Faça push do código para GitHub, GitLab ou Bitbucket
   - No Render, clique em "New" → "Web Service"
   - Conecte seu repositório

3. **Configurar o serviço**
   - **Name:** oficina47 (ou o nome que preferir)
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python app.py`
   - **Plan:** Free (gratuito)

4. **Variáveis de ambiente (opcional)**
   - O Render automaticamente define a variável `PORT`
   - Não é necessário configurar nada adicional

5. **Deploy**
   - Clique em "Create Web Service"
   - Aguarde o build e deploy (pode levar alguns minutos)
   - Seu site estará online!

### ⚠️ Importante para Render:

- O arquivo `runtime.txt` especifica a versão do Python
- O `app.py` já está configurado para usar a porta do Render automaticamente
- Certifique-se de que a pasta `imagem/` está no repositório Git
- O modo debug está desabilitado para produção

## ✨ Funcionalidades

- ✅ Exibição de produtos com imagens
- ✅ Design moderno e responsivo
- ✅ Botão "Comprar" que direciona para WhatsApp
- ✅ Mensagem automática com nome do produto
- ✅ Texto "Consultar valores" no lugar de preços
- ✅ Seção de história da produção
- ✅ Navegação com link para história
- ✅ Contato no cabeçalho

## 🎨 Personalização

Você pode editar:
- **Nomes e descrições dos produtos:** arquivo `app.py`, função `get_products()`
- **Design e cores:** arquivo `static/css/style.css`
- **Layout da página:** arquivo `templates/index.html`

## 📱 WhatsApp

Quando o cliente clicar em "Comprar no WhatsApp", será aberta uma conversa no WhatsApp com uma mensagem pré-formatada contendo o nome do produto de interesse.

