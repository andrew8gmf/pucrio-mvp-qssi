# Back-end - API de Predição e Validação de Modelos

Este componente fornece a inteligência do sistema através de uma API RESTful desenvolvida em FastAPI. O serviço é responsável por carregar o modelo de Machine Learning e disponibilizar o endpoint de inferência.

## Pré-requisitos
- Ambiente de execução Python 3.10 ou superior.
- Dependências listadas no arquivo requirements.txt.

## Procedimentos de Execução

### Instalação de Dependências
Instale os pacotes necessários utilizando o gerenciador de pacotes pip:
```bash
pip install -r requirements.txt
```

### Treinamento e Persistência Local
Caso seja necessário regerar o arquivo de modelo (.pkl) no ambiente local para garantir compatibilidade de versão:
```bash
python train_model.py
```

### Inicialização do Servidor
Para iniciar o serviço de API:
```bash
python app.py
```
O servidor será instanciado em http://localhost:8000. A documentação OpenAPI (Swagger) pode ser acessada em /docs.

## Validação de Desempenho
O sistema inclui testes automatizados para garantir que o modelo em produção atenda aos requisitos mínimos de acurácia definidos nos critérios de avaliação:
```bash
pytest test_model.py
```
O teste realiza o carregamento do modelo persistido e valida sua performance contra uma amostra de teste, assegurando a integridade do sistema em caso de substituição de modelos.
