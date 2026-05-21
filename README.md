# 🛒 Ecommerce Django Project

Um e-commerce moderno inspirado em grandes marketplaces de tecnologia como a [KaBuM!](https://www.kabum.com.br?utm_source=chatgpt.com) e [TerabyteShop](https://www.terabyteshop.com.br?utm_source=chatgpt.com), desenvolvido com Django utilizando foco em performance, experiência do usuário e arquitetura escalável.

O projeto foi criado para simular uma loja real de componentes eletrônicos, permitindo navegação por produtos, gerenciamento de carrinho, autenticação de usuários e fluxo completo de compra.

---

# 🚀 Tecnologias Utilizadas

* Django
* Python
* HTML5
* CSS3
* JavaScript
* SQLite
* Bootstrap/Tailwind (dependendo da sua implementação)
* Git & GitHub

---

# 🎮 Funcionalidades

## 👤 Autenticação de Usuários

* Cadastro de usuários
* Login e logout
* Sessão autenticada
* Controle de usuários

## 🛍️ Catálogo de Produtos

* Listagem de produtos
* Página individual do produto
* Produtos de hardware e periféricos
* Interface inspirada em e-commerces gamers

## 🔎 Pesquisa e Navegação

* Busca de produtos
* Navegação por categorias
* Layout responsivo

## 🛒 Carrinho de Compras

* Adicionar produtos ao carrinho
* Remover produtos
* Atualizar quantidades
* Cálculo automático de subtotal e total

## 💳 Fluxo de Compra

Fluxo completo:

```text id="0jwgt3"
Carrinho → Compra → Realizar Pagamento
```

* Processamento de pedidos
* Salvamento de pedidos
* Associação do pedido ao usuário
* Registro de produtos comprados
* Controle de status do pedido

## 🎨 Interface Moderna

* Design dark tech
* Inspiração visual em lojas gamers
* Navbar moderna
* Cards interativos
* Hover effects suaves
* Responsividade mobile

---

# 📂 Estrutura do Projeto

```bash id="dhlwdr"
Ecommerce-Django-Project/
│
├── core/
├── products/
├── orders/
├── users/
├── static/
├── templates/
├── media/
├── manage.py
└── requirements.txt
```

---

# ⚙️ Como Executar o Projeto

## 1️⃣ Clone o repositório

```bash id="1zp30p"
git clone https://github.com/ccaiosantos/Ecommerce-Django-Project.git
```

---

## 2️⃣ Entre na pasta do projeto

```bash id="skqv7a"
cd Ecommerce-Django-Project
```

---

## 3️⃣ Crie um ambiente virtual

### Windows

```bash id="ujx6tl"
python -m venv venv
venv\Scripts\activate

---

## 4️⃣ Instale as dependências

```bash id="nepqdr"
pip install -r requirements.txt
```

---

## 5️⃣ Execute as migrations

```bash id="hrkj60"
python manage.py makemigrations
python manage.py migrate
```

---

## 6️⃣ Inicie o servidor

```bash id="rnisuf"
python manage.py runserver
```

---

## 7️⃣ Acesse no navegador

```text id="2k5pj1"
http://127.0.0.1:8000/
```

---

# 📸 Preview do Projeto

## 🖥️ Home

* Banner gamer
* Produtos em destaque
* Layout inspirado em marketplaces tech

## 🛒 Carrinho

* Atualização dinâmica de itens
* Resumo do pedido

## 💳 Checkout

* Finalização da compra
* Salvamento de pedidos

---

# 🎯 Objetivo do Projeto

Este projeto foi desenvolvido com o objetivo de:

* Aprimorar conhecimentos em Django
* Simular um e-commerce real
* Estudar arquitetura web
* Trabalhar autenticação e persistência de dados
* Construir uma aplicação escalável e moderna

---


# 📄 Licença

Este projeto é destinado para fins de estudo e portfólio.

---

# 👨‍💻 Autor

Desenvolvido por Caio Gabriel.

Baseado em conceitos modernos de e-commerce utilizando Django.
