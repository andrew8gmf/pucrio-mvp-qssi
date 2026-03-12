# Sistema de Classificação para Triagem de Saúde Mental (DASS-42)

Este repositório contém o Produto Mínimo Viável (MVP) desenvolvido para a pós-graduação em Ciência de Dados e Analytics da PUC-Rio. Ele consiste em um sistema de software inteligente capaz de classificar níveis de depressão com base em traços de personalidade e indicadores demográficos, utilizando o dataset Depression Anxiety Stress Scales (DASS-42).

## Arquitetura do Projeto

O sistema está estruturado em componentes independentes para garantir a separação de responsabilidades:

- **Módulo de Machine Learning (/notebook):** Documentação do processo de extração, transformação, carga (ETL), treinamento de modelos clássicos de classificação e análise comparativa de resultados.
- **Back-end (/backend):** Serviço de API RESTful responsável por embarcar o modelo preditivo e processar requisições de inferência.
- **Front-end (/frontend):** Interface de usuário para coleta de dados e exibição das predições geradas pelo sistema.
- **Dados (/archive):** Armazenamento do conjunto de dados original utilizado para o treinamento dos modelos.

## Tecnologias e Bibliotecas

### Ciência de Dados

- Python 3.x
- Scikit-Learn (Modelagem e Pipelines)
- Pandas (Manipulação de dados)
- Joblib (Persistência de modelos)

### Desenvolvimento Full Stack

- FastAPI (Back-end e Servidor ASGI)
- React e TypeScript (Front-end SPA)
- Pytest (Testes automatizados de performance)

## Instruções de Operação

Para detalh soes técnicosbre a execução e configuração de cada módulo, consulte as documentações específicas:

- [Documentação Técnica do Back-end](./backend/README.md)
- [Documentação Técnica do Front-end](./frontend/README.md)

---

*Este software foi desenvolvido exclusivamente para fins acadêmicos como parte dos requisitos de avaliação da disciplina de Engenharia de Sistemas de Software Inteligentes.*