# Telegram Scraper

Este projeto é um scraper para grupos do Telegram, permitindo buscar mensagens dentro de um intervalo de datas e salvá-las em um arquivo CSV.

## Estrutura do Projeto



telegram_scraper/</br>
├── data/</br>
│   └── messages.csv</br>
├── src/</br>
│   ├── __init__.py</br>
│   ├── etl.py</br>
│   ├── analytics.py</br>
│   └── main.py</br>
├── tests/</br>
│   ├── __init__.py</br>
│   ├── test_etl.py</br>
│   └── test_analytics.py</br>
├── .env</br>
├── .gitignore</br>
├── requirements.txt</br>
├── README.md</br>
└── setup.py</br>




## Configuração
Certifique-se de ter o Python instalado em sua máquina.

1. Clone o repositório para sua máquina local:
```bash
git clone https://github.com/seu_usuario/005_Screping_Telegram.git
```

2. Navegue até o diretório do projeto:
```bash
cd 005_Screping_Telegram
```

3. Crie um ambiente virtual Python usando o venv:
```bash
python -m venv .venv
```

4. Ative o ambiente virtual:
```bash Windows
.venv\Scripts\activate
```
```bash Linux
source .venv/bin/activate
```

5. Instale as dependências do projeto:
```basic
pip install -r requirements.txt
```

6. Crie um arquivo .env na raiz do projeto e adicione as seguintes variáveis de ambiente:
```makefile
API_ID=sua_api_id
API_HASH=sua_api_hash
PHONE_NUMBER=seu_numero_de_telefone
```

7. Substitua sua_api_id, sua_api_hash e seu_numero_de_telefone pelos valores apropriados. Você pode obter a API_ID e API_HASH aqui após criar um aplicativo Telegram.

8. Uso
Execute o script principal main.py:

```bash
python src/main.py
```

#### Siga as instruções no terminal para autenticar sua conta e selecionar o grupo do qual deseja extrair mensagens.

#### Os resultados serão salvos no arquivo data/messages.csv.

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença
Este projeto está licenciado sob a [Licença MIT](LICENSE).


## Tipos de commit e suas descrições
| Tipo       | Descrição                                                              |
|------------|------------------------------------------------------------------------|
| feat       | Uma nova feature foi adicionada ao código.                             |
| fix        | Correção de bugs.                                                      |
| docs       | Alterações na documentação.                                            |
| style      | Alterações que não afetam o comportamento do código.                   |
| refactor   | Refatorações de código, sem adição ou remoção de funcionalidades.      |
| perf       | Melhorias de desempenho.                                               |
| test       | Adições ou alterações em testes unitários.                            |
| build      | Alterações relacionadas ao sistema de build, dependências ou configurações. |
| ci         | Alterações relacionadas a configuração de integração contínua.        |
| chore      | Atualizações diversas que não se enquadram nas categorias anteriores.  |
