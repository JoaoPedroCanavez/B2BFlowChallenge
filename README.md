# B2BFlow Challenge
Aplicação que faz o consumo das API's Supabase e Z-API para fazer o envio de mensagens automatizadas para clientes, colaboradores, etc. por meio do app whatsapp.

## Requisitos
* Python 3.x
* Chaves de API para Z-API e Supabase

## Configuração do Ambiente de Desenvolvimento

### 1. Instalação do Python
Faça o download da última versão do Python no site oficial: [https://www.python.org/downloads/](https://www.python.org/downloads/).

Durante a instalação, **é crucial** marcar a opção **"Add Python to PATH"** no canto inferior da tela.

![Imagem da tela de instalação do Python, mostrando a opção "Add Python to PATH" selecionada.](https://education.launchcode.org/lchs/_images/win-python-installer.png)

### 2. Instalação das Dependências
Após a instalação do Python, abra o terminal de sua preferência (CMD, PowerShell, etc.) e instale as bibliotecas necessárias usando o `pip`:

```bash
pip install supabase
pip install requests
pip install python-dotenv
```

Em casos de erros relacionados a path para uso do comando pip em windows consulte este video: [https://Youtube.com/@thecodebear](https://www.youtube.com/watch?v=MZZwXonQwdI).


## Configurando as API's para uso da aplicação

### 1. Supabase
Abra o site Supabase e crie uma conta ou faça login: [https://supabase.com/](https://supabase.com/).

![Imagem da tela de login do site Supabase.](https://user-images.githubusercontent.com/17494745/215134801-68458462-5b87-4a04-a6ca-55520460365f.png)

Crie uma nova tabela chamada Contatos com 2 colunas(nome_contato, telefone) e insira dados na tabela. 

### 2. Z-API
Abra o site Supabase e crie uma conta ou faça login: [https://z-api.io/](https://app.z-api.io/).

Ative o token de segurança da conta
![Imagem da tela de ativação de token de segurança.](https://developer.z-api.io/en/assets/images/security-token-EN-9ce4414e106f8944a6c19bcf674c1325.jpeg)

E crie uma nova instancia para fazer envio de mensagens.

![Imagem da tela de criação de nova instacia no z-api.](https://developer.z-api.io/assets/images/EditInstance-3b17fbd4b73d06954876b8467a590d87.jpeg)

## Executando o codigo

### 1. Clonando repositorio
Faça o dowload do repositorio como .zip, ou faça um clone via CommandLine usando gitBash ou terminal de sua preferencia.

**git clone https://github.com/JoaoPedroCanavez/B2BFlowChallenge.git**


### 2. Coloque suas chaves de acesso
Abra o arquivo .env e coloque as informações sendo requisitadas ID, Keys, etc.

![Imagem da tela .env.](assets\env.jpg)

### 3. executando o codigo

execute o codico com debug ou em terminal no Main.py

**python main.py**

executa a classe via terminal.