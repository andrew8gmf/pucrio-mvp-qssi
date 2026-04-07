# Front-end - Interface de Usuário e Integração

O front-end é uma Single Page Application (SPA) desenvolvida em React, projetada para facilitar a interação do usuário com o modelo de classificação de saúde mental.

## Requisitos de Ambiente
- Node.js 18.x ou superior.
- Gerenciador de pacotes NPM.

## Procedimentos de Execução

### Instalação
Proceda com a instalação das dependências do projeto:
```bash
npm install
```

### Ambiente de Desenvolvimento
Para executar a aplicação em modo de desenvolvimento com atualização automática (hot-reload):
```bash
npm run dev
```
A aplicação estará acessível em `http://localhost:5173` por padrão.

### Ambiente de Produção
Para realizar o build e executar a versão otimizada:
```bash
npm run build
npm start
```

## Protocolo de Comunicação
A interface está configurada para realizar requisições assíncronas ao back-end por meio do endpoint `POST http://localhost:8000/predict`. É imperativo que o serviço de back-end esteja operacional para o funcionamento da predição.
