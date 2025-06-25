
# 💰 IR Expert - Simulador de Imposto de Renda (PF e PJ)

Projeto desenvolvido para a disciplina de Matemática Aplicada - Curso de Análise e Desenvolvimento de Sistemas.

## 🧠 Descrição
O **IR Expert** é uma aplicação que simula de forma precisa o cálculo de **Imposto de Renda de Pessoa Física (IRPF)** e **Pessoa Jurídica (IRPJ)**, utilizando dados reais e atualizados, com integração via API.

## 🚀 Funcionalidades
- ✅ Cálculo de IRPF com:
  - Salário bruto
  - Dependentes
  - Despesas médicas
  - Educação
  - Previdência

- ✅ Cálculo de IRPJ:
  - Lucro Presumido (comércio e serviços)
  - Lucro Real

- ✅ Consulta automática de CNPJ via **BrasilAPI**.
- ✅ Consulta de câmbio em tempo real via **AwesomeAPI**.
- ✅ Interface interativa e fácil de usar (Streamlit).

## 🔗 APIs Utilizadas
- [BrasilAPI - CNPJ](https://brasilapi.com.br/)
- [AwesomeAPI - Câmbio](https://docs.awesomeapi.com.br/api-de-moedas)

## 🏗️ Tecnologias
- Python
- Streamlit
- Requests
- Pandas
- Plotly
- FPDF

## 📦 Instalação

1. Clone este repositório:

```bash
git clone https://github.com/seuusuario/ir-expert.git
cd ir-expert
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute a aplicação:

```bash
streamlit run app.py
```

## 🖥️ Acesso
O app rodará localmente em:  
`http://localhost:8501`

## 📜 Licença
MIT License.

## 👥 Autores
- Davi Casari
- Gustavo Bravin
