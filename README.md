# 🎮 SalesDB – Sistema de Cadastro de Jogos com Automação

O **SalesDB** é um sistema web desenvolvido para **cadastro e visualização de dados de jogos**, integrado a uma **automação em Python** responsável por inserir automaticamente registros no sistema a partir de uma base de dados.

O projeto simula um **sistema real de uso interno**, unindo **front-end**, **JavaScript** e **automação com Python**, com foco em organização, UX e produtividade.

---

## 📌 Funcionalidades

### 🌐 Sistema Web
- 🔐 Tela de **login**
- 📝 Formulário de **cadastro de jogos**
- 📊 Tabela dinâmica de registros
- 📌 Tabela com altura fixa e scroll interno
- ❌ Sem scroll da página inteira
- 🧹 Limpeza da tabela
- 🎨 Layout organizado e responsivo

### 🤖 Automação em Python
- Leitura de base de dados (`.csv`)
- Preenchimento automático do formulário no site
- Simulação de interação humana
- Cadastro sequencial dos registros
- Redução de erros manuais
- Ideal para grandes volumes de dados

---

## 🧪 Base de Dados

A automação utiliza uma base de dados no formato `.csv`, contendo campos como:

- Ranking
- Nome do jogo
- Plataforma
- Ano de lançamento
- Gênero
- Editora
- Vendas totais

Cada linha do arquivo representa um cadastro no sistema.

---

## 🛠️ Tecnologias Utilizadas

### Front-end
- HTML5
- CSS3
- JavaScript (Vanilla)
- Bootstrap 5

### Automação
- Python 3
- Pandas
- PyAutoGUI
- WebDriver (Chrome/Edge)

### Ferramentas
- Git & GitHub
- VS Code

---

## ▶️ Como Executar o Projet

### 1️⃣ Executar o site
Abra o arquivo `index.html` em um navegador moderno.

### 2️⃣ Executar a automação
```bash
pip install -r requirements.txt
python app.py


