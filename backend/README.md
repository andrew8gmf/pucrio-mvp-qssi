# Back-end - API de Predição e Validação de Modelos

Este componente fornece a inteligência do sistema por meio de uma API RESTful desenvolvida em FastAPI. O serviço é responsável por carregar o modelo de Machine Learning e disponibilizar o endpoint de inferência.

## Pré-requisitos
- Ambiente de execução Python 3.10 ou superior.
- Dependências listadas no arquivo `requirements.txt`.

## Gerenciamento do Modelo Preditivo
Para o funcionamento correto da API, é imperativo que o arquivo do modelo treinado (formato `.pkl`) esteja localizado no diretório `backend/models/`. O servidor foi projetado para carregar automaticamente o primeiro arquivo com extensão `.pkl` encontrado nesta pasta.

## Procedimentos de Execução

### Instalação de Dependências
Instale os pacotes necessários utilizando o gerenciador de pacotes pip:
```bash
pip install -r requirements.txt
```

### Treinamento e Persistência Local
Caso seja necessário gerar o arquivo de modelo no ambiente local para garantir compatibilidade de versão:
```bash
python train_model.py
```

### Inicialização do Servidor
Para iniciar o serviço de API:
```bash
python app.py
```
O servidor será instanciado em `http://localhost:8000`. A documentação OpenAPI (Swagger) pode ser acessada em `/docs`.

## Validação de Desempenho (Item 5 do MVP)
O sistema inclui testes automatizados para assegurar que o modelo em produção atenda aos requisitos mínimos de acurácia estabelecidos:
```bash
pytest test_model.py
```
O teste realiza o carregamento do modelo persistido e valida sua performance contra uma amostra de teste, assegurando a integridade do sistema em caso de substituição de modelos.
