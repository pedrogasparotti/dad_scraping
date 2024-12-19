# Web Scraping de Notícias Agrícolas

## Descrição
Script em Python para coletar notícias dos últimos 5 dias utilizando a biblioteca GNews. O script busca por palavras-chave específicas e salva os resultados em um arquivo Excel.

## Funcionalidades
- Busca por múltiplas palavras-chave
- Filtragem por data (últimos 5 dias)
- Remoção de duplicatas
- Exportação para Excel com timestamp
- Log de execução
- Estatísticas básicas de resultados

## Pré-requisitos
- Python 3.8 ou superior
- Bibliotecas Python listadas em `requirements.txt`

## Instalação
1. Clone o repositório
   ```bash
   git clone [URL_DO_REPOSITÓRIO]
   ```

2. Instale as dependências
   ```bash
   pip install -r requirements.txt
   ```

## Como usar
1. Execute o script principal:
   ```bash
   python main.py
   ```

2. Os resultados serão salvos em um arquivo Excel com o formato `agros_[DATA]_[HORA].xlsx`

## Estrutura do projeto
```
.
├── main.py
├── requirements.txt
├── README.md
└── logs/
```

## Saída
O script gera um arquivo Excel com as seguintes colunas:
- Keyword (palavra-chave usada)
- Title (título da notícia)
- Link (URL da notícia)
- Published (data de publicação)
- Description (descrição/resumo)
- Source (fonte da notícia)

## Requirements.txt
```
gnews>=0.3.0
pandas>=1.5.0
openpyxl>=3.1.0
python-dateutil>=2.8.2
```

## Contribuição
Sinta-se livre para contribuir com o projeto através de Pull Requests.

## Licença
Este projeto está sob a licença MIT.