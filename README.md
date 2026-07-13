# TechFlow Task Manager

Sistema de gerenciamento de tarefas desenvolvido em **Python** utilizando o framework **Flask**, com aplicação de conceitos de **Engenharia de Software**, **Git/GitHub**, **UML** e **Metodologias Ágeis (Kanban)**.

---

## 📋 Descrição

O **TechFlow Task Manager** é uma aplicação web que permite gerenciar tarefas de forma simples e intuitiva.

O sistema oferece as operações básicas de **CRUD (Create, Read, Update e Delete)**, permitindo ao usuário criar, visualizar, editar e excluir tarefas através de uma interface desenvolvida em HTML e CSS.

Este projeto foi desenvolvido como atividade prática da disciplina de **Engenharia de Software** do curso de **Análise e Desenvolvimento de Sistemas** da **UNIFECAF**.

---

## 📷 Interface do Sistema

> *Adicione aqui um print da aplicação.*

Exemplo:

```md
![Tela do Sistema](docs/screenshot.png)
```

---

## 🚀 Funcionalidades

- ✅ Criar tarefas
- ✅ Visualizar tarefas cadastradas
- ✅ Editar tarefas
- ✅ Excluir tarefas
- ✅ Interface web simples e intuitiva
- ✅ Organização utilizando metodologia Kanban
- ✅ Testes automatizados
- ✅ Integração Contínua (GitHub Actions)

---

## 🛠 Tecnologias Utilizadas

- Python 3
- Flask
- HTML5
- CSS3
- Git
- GitHub
- GitHub Projects (Kanban)
- GitHub Actions (CI)

---

## 📁 Estrutura do Projeto

```text
techflow-task-manager/
│
├── docs/
│   ├── Diagrama de Casos de Uso.png
│   ├── Diagrama de Classes.png
│   └── screenshot.png
│
├── src/
│   ├── static/
│   ├── templates/
│   ├── app.py
│   └── models.py
│
├── tests/
│
├── requirements.txt
└── README.md
```

---

## ▶️ Como Executar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/danielnoimage-creator/techflow-task-manager.git
```

### 2. Acesse a pasta do projeto

```bash
cd techflow-task-manager
```

### 3. Crie um ambiente virtual (Opcional)

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Execute a aplicação

```bash
python src/app.py
```

Abra o navegador em:

```
http://127.0.0.1:5000
```

---

## ✅ Executando os Testes

Para executar os testes automatizados utilize:

```bash
pytest
```

Os testes verificam o funcionamento das principais funcionalidades da aplicação.

---

## 📌 Metodologia Ágil

Durante o desenvolvimento foi utilizada a metodologia **Kanban**, utilizando o **GitHub Projects** para organizar as atividades do projeto.

As tarefas foram distribuídas em três colunas:

- 📝 To Do
- 🚧 In Progress
- ✅ Done

Essa organização facilitou o acompanhamento da evolução do desenvolvimento e do cumprimento das etapas do projeto.

---

## 🔄 Integração Contínua (CI)

O projeto utiliza **GitHub Actions** para executar automaticamente os testes sempre que um novo commit é enviado ao repositório.

Essa prática garante maior confiabilidade e qualidade durante o desenvolvimento.

---

## 📚 Modelagem UML

Para auxiliar no planejamento e documentação do sistema foram desenvolvidos os seguintes diagramas:

- Diagrama de Casos de Uso
- Diagrama de Classes

Os arquivos encontram-se na pasta **docs/**.

---

## 🎯 Objetivo Acadêmico

Este projeto foi desenvolvido com o objetivo de aplicar na prática os conhecimentos adquiridos na disciplina de Engenharia de Software, envolvendo conceitos como:

- Engenharia de Software
- Desenvolvimento Web
- Git e GitHub
- Controle de Versão
- Metodologias Ágeis
- Kanban
- Modelagem UML
- Testes Automatizados
- Integração Contínua (CI)

---

## 👨‍💻 Autor

**Daniel Santos Silva**

Curso: **Análise e Desenvolvimento de Sistemas**

Instituição: **UNIFECAF**

---

## 📄 Licença

Projeto desenvolvido exclusivamente para fins acadêmicos