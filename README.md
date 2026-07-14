# learning-django

Este repositório é um projeto simples de estudo em Django, criado para praticar conceitos básicos de desenvolvimento web, como rotas, views, templates, arquivos estáticos e organização de aplicativos.

## Objetivo do projeto

O projeto tem como finalidade demonstrar, de forma prática, como montar uma aplicação Django com múltiplos módulos, onde é possível navegar entre uma página inicial e uma área de blog. Ele serve como base para aprender a estrutura padrão do Django e explorar a separação de responsabilidades entre apps, URLs, templates e arquivos estáticos.

## Funcionalidades principais

- Página inicial da aplicação, acessada em `/`
- Página de blog, acessada em `/blog/`
- Página de detalhes de um post, acessada dinamicamente por `/blog/<id>/`
- Página de exemplo para estudo de templates e renderização
- Uso de arquivos HTML reutilizáveis e partials para montar a interface

## Estrutura dos arquivos principais

### Arquivos de configuração do projeto

- `manage.py`: ponto de entrada para executar comandos do Django, como rodar o servidor e aplicar migrações.
- `project/settings.py`: configurações gerais do projeto, como apps instalados, banco de dados, templates e arquivos estáticos.
- `project/urls.py`: define as rotas principais da aplicação e inclui as URLs dos apps `home` e `blog`.

### App `home`

- `home/views.py`: contém a view `home`, responsável por renderizar a página inicial.
- `home/urls.py`: define a rota da home (`/`).
- `home/templates/home/index.html`: template da página inicial.
- `home/static/home/`: arquivos CSS, imagens e JavaScript específicos para a home.

### App `blog`

- `blog/views.py`: contém as views `blog`, `exemplo` e `post`, responsáveis por exibir a listagem de posts, uma página de exemplo e os detalhes de um post específico.
- `blog/urls.py`: define as rotas do blog (`/blog/`, `/blog/<id>/` e `/blog/exemplo/`).
- `blog/data.py`: arquivo com os dados dos posts utilizados para simular conteúdo do blog.
- `blog/templates/blog/`: templates responsáveis pela renderização das páginas do blog.

### Templates base

- `base/global/base.html`: template principal que serve como estrutura base para as páginas.
- `base/global/partials/`: arquivos reutilizáveis, como cabeçalho, menu e bloco de post.

## Como executar o projeto

1. Crie um ambiente virtual:
   `python -m venv .venv`
2. Ative o ambiente virtual:
   - Windows: `.venv\Scripts\activate`
3. Instale o Django:
   `pip install django`
4. Execute as migrações:
   `python manage.py migrate`
5. Inicie o servidor:
   `python manage.py runserver`

Depois, acesse no navegador:

- `http://127.0.0.1:8000/` para a home
- `http://127.0.0.1:8000/blog/` para o blog

## Observação

Este projeto é um exemplo inicial de aprendizado e pode ser expandido com modelos de banco de dados, formulários, autenticação e integração com templates mais completos.
