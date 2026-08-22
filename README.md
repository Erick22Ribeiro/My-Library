README.md
# My-Library

Aplicação web simples em Django para gerenciar uma biblioteca pessoal: cadastrar livros, marcar como "Quero ler", "Comprado" ou "Lido", e buscar livros por APIs (ex.: Google Books). Ideal para quem quer um catálogo pessoal de leitura com uma interface web leve.

## Stack
- **Languages:** Python, HTML, CSS
manage.py # CLI do Django requirements.txt # dependências my_library/ # configuração do projeto (settings, wsgi, asgi, urls) account/ # app para contas/usuários (views, urls, templates, static) core/ # app principal: modelos, views, templates, serviços (busca)

Code

Como se encaixa: o projeto é um site Django padrão. `my_library` contém as configurações e URLs do projeto; `core` implementa o modelo Livro, as views de listagem/busca e os serviços que consultam APIs externas; `account` contém a lógica relacionada à conta/administrativo. O fluxo principal: requisição → views em `core/views.py` → operações sobre o modelo `core.models.Livro` → templates para renderização.

## Requisitos
- Python 3.10+ (ou versão compatível com as dependências em `requirements.txt`)
- pip
- (opcional) Credenciais de API caso a integração de busca necessite de chave (ex.: Google Books API)

## Instalação rápida (exemplo)
Execute os comandos abaixo numa máquina Unix-like; no Windows adapte os comandos de virtualenv/variáveis.

```bash
git clone https://github.com/ErickRibeiroG/My-Library.git
cd My-Library

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt

# Variáveis recomendadas (opcional):
# export SECRET_KEY='sua_chave_secreta'
# export DEBUG=False
# export GOOGLE_BOOKS_API_KEY='sua_chave_se_for_necessaria'

python manage.py migrate
python manage.py createsuperuser   # criar usuário admin
python manage.py runserver
A aplicação ficará disponível em http://127.0.0.1:8000/.

Configuração importante
my_library/settings.py tem DEBUG=True por padrão e usa SQLite (db.sqlite3) — alterar para produção conforme necessário.
Proteja e gere um SECRET_KEY seguro em produção; não deixe chaves sensíveis no repositório.
Ajuste ALLOWED_HOSTS em produção.
Se usar um banco de dados diferente (Postgres, MySQL), atualize DATABASES em my_library/settings.py e instale as dependências correspondentes.
Rotas / Endpoints úteis
/ — página inicial (listagem por status)
/buscar/ — busca de livros (parâmetro q)
/livros/ — página de consulta/visualização (conforme templates)
/admin/ — painel de administração do Django
(Os nomes exatos podem ser verificados em core/urls.py e my_library/urls.py.)
