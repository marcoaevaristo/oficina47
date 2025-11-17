# 🚀 Guia de Deploy no Render - Oficina 47

## Passo 1: Preparar o repositório Git

### 1.1 Inicializar Git (se ainda não tiver)
```bash
git init
```

### 1.2 Adicionar todos os arquivos
```bash
git add .
```

### 1.3 Fazer commit
```bash
git commit -m "Site Oficina 47 - Torradores de Café"
```

## Passo 2: Criar repositório no GitHub

### 2.1 Criar conta/conectar no GitHub
- Acesse: https://github.com
- Faça login ou crie uma conta

### 2.2 Criar novo repositório
- Clique no botão "+" no canto superior direito
- Selecione "New repository"
- Nome: `oficina47` (ou outro nome de sua preferência)
- Deixe **público** (Public) para plano gratuito do Render
- **NÃO** marque "Initialize with README"
- Clique em "Create repository"

### 2.3 Fazer push do código
No terminal, execute (substitua SEU_USUARIO pelo seu usuário do GitHub):

```bash
git remote add origin https://github.com/SEU_USUARIO/oficina47.git
git branch -M main
git push -u origin main
```

**Nota:** Se pedir login, use seu token de acesso pessoal do GitHub (não a senha).

## Passo 3: Deploy no Render

### 3.1 Criar conta no Render
- Acesse: https://render.com
- Clique em "Get Started for Free"
- Faça login com GitHub (recomendado) ou crie conta com email

### 3.2 Criar novo Web Service
- No dashboard, clique em "New +"
- Selecione "Web Service"
- Conecte seu repositório GitHub
- Selecione o repositório `oficina47` (ou o nome que você usou)

### 3.3 Configurar o serviço

Preencha os campos:

- **Name:** `oficina47` (ou outro nome)
- **Region:** Escolha a mais próxima (ex: São Paulo se disponível)
- **Branch:** `main` (ou `master`)
- **Root Directory:** (deixe vazio)
- **Environment:** `Python 3`
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `python app.py`
- **Plan:** `Free` (gratuito)

### 3.4 Configurações avançadas (opcional)

Na seção "Advanced", você pode configurar:
- **Auto-Deploy:** `Yes` (deploy automático quando fizer push)
- **Health Check Path:** `/` (deixe vazio ou coloque `/`)

### 3.5 Criar o serviço
- Clique em "Create Web Service"
- Aguarde o build (pode levar 5-10 minutos na primeira vez)

## Passo 4: Verificar o deploy

### 4.1 Acompanhar o build
- Você verá os logs do build em tempo real
- Aguarde até aparecer "Your service is live"

### 4.2 Acessar o site
- O Render fornecerá uma URL como: `https://oficina47.onrender.com`
- Clique na URL ou copie para acessar seu site

## ⚠️ Problemas comuns e soluções

### Erro: "Module not found"
- Verifique se o `requirements.txt` está correto
- Certifique-se de que todas as dependências estão listadas

### Erro: "Port already in use"
- O código já está configurado para usar a porta do Render automaticamente
- Não precisa alterar nada

### Imagens não aparecem
- Certifique-se de que a pasta `imagem/` está no repositório Git
- Verifique se todas as imagens foram commitadas

### Site não carrega
- Verifique os logs no Render
- Certifique-se de que o `Start Command` está correto: `python app.py`

## 📝 Checklist final

Antes de fazer deploy, verifique:

- [ ] Todos os arquivos estão commitados no Git
- [ ] A pasta `imagem/` está no repositório
- [ ] O arquivo `requirements.txt` está atualizado
- [ ] O arquivo `runtime.txt` existe
- [ ] O `app.py` está configurado para usar `PORT` do ambiente
- [ ] O número do WhatsApp está correto no `app.py`

## 🔄 Atualizar o site

Para fazer atualizações:

1. Faça as alterações no código
2. Commit e push:
   ```bash
   git add .
   git commit -m "Descrição da atualização"
   git push
   ```
3. O Render fará deploy automático (se configurado)
4. Aguarde alguns minutos e acesse o site

## 💡 Dicas

- O plano gratuito do Render pode "dormir" após 15 minutos de inatividade
- A primeira requisição após dormir pode demorar ~30 segundos
- Para evitar isso, considere fazer upgrade para plano pago
- Ou use serviços como UptimeRobot para manter o site "acordado"

## 🆘 Precisa de ajuda?

Se encontrar problemas:
1. Verifique os logs no dashboard do Render
2. Confira se todos os arquivos estão no repositório
3. Verifique se o `requirements.txt` está correto

