Ola, este e um pequeno projeto que tenho projeto, ainda esta pequeno mas acredito que va crescer muito ainda #laele

first, install virtual environmment (venv)

Linux
```
python3 -m venv .virt
source .virt/bin/activate
pip install flask
```

# Projeto Flask - Arquitetura MVC
Este projeto utiliza o framework Flask seguindo a arquitetura MVC (Model-View-Controller) para organizar o código de maneira clara e eficiente.

# O que é MVC?
A arquitetura MVC separa a aplicação em três componentes principais:

Model (Modelo): Responsável pela lógica de dados, como interação com o banco de dados e validação de regras de negócio. Isso garante que toda a manipulação de dados esteja centralizada e bem organizada.

View (Visão): Refere-se à interface de usuário, ou seja, o que o usuário vê e interage. No Flask, isso é representado pelos arquivos HTML que são renderizados dinamicamente com o motor de templates Jinja2. Todos os arquivos de visão estão na pasta templates.

Controller (Controlador): Atua como intermediário entre a View e o Model. Ele captura as requisições dos usuários (via rotas) e decide qual ação executar, seja acessar o banco de dados ou renderizar uma página HTML. As rotas e controladores estão na pasta controllers.

# Estrutura do Projeto
A organização dos diretórios segue a divisão do MVC para facilitar a manutenção e escalabilidade:

```
app/
├── controllers/    # Lida com as rotas e a lógica de controle
├── models/         # Contém os modelos e a lógica de dados
├── static/         # Arquivos estáticos (CSS, JS, imagens, etc.)
│   ├── css/
│   ├── img/
│   ├── js/
│   └── scss/
├── templates/      # Arquivos de template HTML (interface do usuário)
```

# Por que utilizar MVC?
Organização: Com a separação das responsabilidades em três camadas (Model, View, Controller), o código fica mais limpo e fácil de manter.
Escalabilidade: Facilita a adição de novos recursos sem comprometer a estrutura existente.
Reutilização de Código: Lógica de negócios (Model) e de interface (View) podem ser reutilizadas em diferentes partes do projeto.
Manutenção: Fica mais fácil de encontrar e corrigir bugs, já que as responsabilidades estão bem definidas.
